#!/usr/bin/env python3
"""Validate an SVG for common OKVIZ Synoptic Panel requirements.

Standard library only. Decoration subtrees marked with
data-okviz-area-type="decoration" are excluded from the bindable-area count.
"""

from __future__ import annotations

import argparse
import collections
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

SVG_NS = "http://www.w3.org/2000/svg"
AREA_TAGS = {"circle", "ellipse", "line", "path", "polygon", "polyline", "rect", "g"}
UNSUPPORTED_TAGS = {"script", "foreignObject"}
VALID_AREA_TYPES = {"area", "link", "decoration"}
LOUD_FILL_RE = re.compile(
    r"^(?:#(?:f00|ff0000|0f0|00ff00|00f|0000ff|ff0|ffff00|f0f|ff00ff|0ff|00ffff)|"
    r"red|lime|blue|yellow|magenta|cyan)$",
    re.I,
)
OPEN_SVG_RE = re.compile(r"<svg\b[^>]*>", re.I | re.S)
XMLNS_RE = re.compile(r'\bxmlns\s*=\s*["\']http://www\.w3\.org/2000/svg["\']', re.I)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_number(value: str | None) -> float | None:
    if value is None:
        return None
    match = re.match(r"\s*(-?\d+(?:\.\d+)?)", value)
    return float(match.group(1)) if match else None


def iter_with_decoration(root: ET.Element) -> Iterable[tuple[ET.Element, bool]]:
    stack: list[tuple[ET.Element, bool]] = [(root, False)]
    while stack:
        elem, inherited = stack.pop()
        is_decoration = inherited or elem.get("data-okviz-area-type") == "decoration"
        yield elem, is_decoration
        children = list(elem)
        stack.extend((child, is_decoration) for child in reversed(children))


def simple_bbox(elem: ET.Element) -> tuple[float, float, float, float] | None:
    tag = local_name(elem.tag)
    if tag == "rect":
        x = parse_number(elem.get("x")) or 0.0
        y = parse_number(elem.get("y")) or 0.0
        w = parse_number(elem.get("width"))
        h = parse_number(elem.get("height"))
        return (x, y, x + w, y + h) if w is not None and h is not None else None
    if tag == "circle":
        cx = parse_number(elem.get("cx"))
        cy = parse_number(elem.get("cy"))
        r = parse_number(elem.get("r"))
        return (cx - r, cy - r, cx + r, cy + r) if None not in (cx, cy, r) else None
    if tag == "ellipse":
        cx = parse_number(elem.get("cx"))
        cy = parse_number(elem.get("cy"))
        rx = parse_number(elem.get("rx"))
        ry = parse_number(elem.get("ry"))
        return (cx - rx, cy - ry, cx + rx, cy + ry) if None not in (cx, cy, rx, ry) else None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Synoptic Panel SVG.")
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()

    path = args.svg
    errors: list[str] = []
    warnings: list[str] = []

    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read {path}: {exc}")
        return 1

    opening = OPEN_SVG_RE.search(raw)
    if not opening or not XMLNS_RE.search(opening.group(0)):
        errors.append('Root <svg> must declare xmlns="http://www.w3.org/2000/svg".')

    if "data-okviz-unbound" in raw:
        warnings.append(
            'Obsolete attribute data-okviz-unbound found; use '
            'data-okviz-area-type="decoration" for non-data elements.'
        )

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        print(f"ERROR: invalid XML: {exc}")
        return 1

    if local_name(root.tag) != "svg":
        errors.append("Root element is not <svg>.")
    if not root.get("viewBox"):
        errors.append("Root <svg> is missing viewBox.")

    ids: list[str] = []
    bindable_ids: list[str] = []
    bindable_elements: list[ET.Element] = []
    text_elements: list[ET.Element] = []

    for elem, is_decoration in iter_with_decoration(root):
        tag = local_name(elem.tag)
        elem_id = elem.get("id")
        area_type = elem.get("data-okviz-area-type")

        if area_type and area_type not in VALID_AREA_TYPES:
            warnings.append(
                f'{tag} id="{elem_id or ""}" has unsupported '
                f'data-okviz-area-type="{area_type}".'
            )

        if elem_id:
            ids.append(elem_id)
            if elem_id[0].isdigit():
                warnings.append(f'ID starts with a digit: "{elem_id}".')

        if tag in UNSUPPORTED_TAGS:
            errors.append(f"Unsupported element: <{tag}>.")

        for attr, value in elem.attrib.items():
            attr_name = local_name(attr)
            if attr_name.lower().startswith("on"):
                errors.append(f'Event handler "{attr_name}" found on <{tag}>.')
            if attr_name in {"href", "xlink:href"} and value.strip().lower().startswith("javascript:"):
                errors.append(f'javascript: URL found on <{tag}>.')

        if tag == "text":
            text_elements.append(elem)

        if tag in AREA_TAGS and elem_id and not is_decoration and area_type != "link":
            bindable_ids.append(elem_id)
            bindable_elements.append(elem)
            fill = (elem.get("fill") or "").strip()
            if fill and LOUD_FILL_RE.match(fill):
                warnings.append(f'Bindable area "{elem_id}" uses loud fill "{fill}".')

    duplicates = [key for key, count in collections.Counter(ids).items() if count > 1]
    if duplicates:
        warnings.append("Duplicate ids: " + ", ".join(sorted(duplicates)[:30]))

    # Conservative text-over-area check for simple shapes.
    simple_areas = [
        (elem.get("id") or "", bbox)
        for elem in bindable_elements
        if (bbox := simple_bbox(elem)) is not None
    ]
    for text in text_elements:
        x = parse_number(text.get("x"))
        y = parse_number(text.get("y"))
        if x is None or y is None:
            continue
        for area_id, (x1, y1, x2, y2) in simple_areas:
            if x1 <= x <= x2 and y1 <= y <= y2:
                errors.append(
                    f'Text at ({x:g}, {y:g}) appears inside bindable area "{area_id}".'
                )
                break

    print(f"Bindable areas detected: {len(bindable_ids)}")
    print(f"Total ids in file: {len(ids)} ({len(set(ids))} unique)")

    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"- {error}")
        print("\nRESULT: problems found.")
        return 1

    print("\nRESULT: clean (no hard errors). Ready for Synoptic Panel.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
