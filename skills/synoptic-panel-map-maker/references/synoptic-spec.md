# Synoptic Panel SVG — Technical Reference

This file is the authoritative spec the skill relies on. It is distilled from the
OKVIZ Synoptic Panel documentation (SVG Format page) and from analysis of three
known-good production maps (human body, US states, ship sections).

Source: https://docs.okviz.com/visuals/synoptic-panel/concepts/maps/svg-format

---

## 1. What an "area" is

> In Synoptic Panel, an area is a shape or group of shapes that has been linked
> to a specific data point.

An SVG element becomes a bindable area when ANY of these is true:
- it has an `id` attribute, OR
- it has a `data-okviz-strong` attribute, OR
- it was bound manually in the visual's Map Editor.

The map's job is therefore simple: **every region the user wants to color or
highlight with data must be a single shape (or a group) carrying a stable `id`.**

## 2. Shapes that can be areas

`<circle>`, `<ellipse>`, `<line>`, `<path>`, `<polygon>`, `<polyline>`, `<rect>`,
or a `<g>` group enclosing any of those.

`<path>` is by far the most common for real maps. `<rect>` is common for
grid-like regions (e.g. ship cabins) and for invisible label placeholders.

## 3. The `id` attribute — rules (critical)

- Must be a valid XML ID: start with a letter or underscore, then letters,
  digits, hyphens, underscores, colons, periods.
- Spaces are technically allowed but NOT recommended.
- **If an id would start with a digit, escape it with a leading underscore**
  (`1` becomes `_1`). This is the rule most often gotten wrong.
- Each `id` should be UNIQUE within the map.
  - If several elements share one id, they all bind to the same data point.
    That is occasionally desired (e.g. left+right "lung" → one "lung" row).
    When it is intentional, prefer giving each element a unique id and binding
    them together with `data-okviz-strong` instead, so the file stays valid.

### Naming strategy depends on how data will bind

There are two legitimate approaches, both seen in the examples:

A. **Semantic ids that match a data column** (US map: `US-NY`, `US-CA`;
   body: `head`, `neck`, `foot`). Best when the Power BI category field
   contains those same strings — Synoptic then auto-binds with zero manual work.

B. **Sequential numeric ids** (`_1`, `_2`, … or just `1`, `2`, … which Synoptic
   tolerates on import). Best for many near-identical regions (ship cabins,
   parking spots, seats) where the data is keyed by number. Remember the
   leading-underscore rule for strict XML validity.

## 4. Custom OKVIZ attributes (optional, powerful)

All are optional. Custom attributes OVERRIDE the visual's UI settings.

**Current decoration rule:** mark every non-data shape or group with `data-okviz-area-type="decoration"`.

| Attribute                    | Put it on          | What it does |
|------------------------------|--------------------|--------------|
| `data-okviz-strong`          | any shape/group    | (string) force-bind this element to a named data point regardless of its id |
| `data-okviz-drill-url`       | any area           | (string) URL of a remote SVG to load when drilling into this area |
| `data-okviz-link-url`        | any shape          | (string) clicking navigates to this URL |
| `data-okviz-svg-author`      | `<svg>` root       | (string) shows author name in the visual |
| `data-okviz-svg-attribution` | `<svg>` root       | (string) shows attribution text in the visual |
| `data-okviz-autofetch`       | `<svg>` root       | (string/bool) enables Auto-Fetch; `true` means use the `id` attribute |
| `data-okviz-no-labels`       | `<svg>` or an area | (bool) turn off all labels, or labels on one area |
| `data-okviz-area-type`       | any shape/group    | (string) sets element behavior: `area`, `link`, or `decoration`; use `decoration` for every non-data element |


Most useful in generation: `data-okviz-area-type="decoration"` on background/outline layers so
they never accidentally pick up data color, and `data-okviz-strong` when you
want two shapes to share one data point while keeping unique ids.

## 5. UNSUPPORTED — will be stripped or cause rejection

Do NOT emit any of these (security/performance):
- Event handlers: `onclick`, `onload`, `onerror`, etc.
- `href` using the `javascript:` protocol
- `<script>`
- `<foreignObject>`

Also avoid:
- External stylesheets or `<style>` blocks that hard-code `fill` on areas.

### Raster images inside an SVG

Prefer vector-only maps when possible. In the bitmap-tracing workflow, however,
the user's original bitmap may remain as non-bindable background/context when
the user explicitly wants it preserved.

When retaining a bitmap:
- keep the source image unmodified;
- place it behind the vector bindable areas;
- put it in a group marked `data-okviz-area-type="decoration"`;
- keep the actual data-bindable regions as vector SVG shapes/groups with stable
  ids;
- avoid unnecessary raster duplication or derived/edited image layers.

A bitmap background is context only; it never replaces vector bindable areas.

## 6. Coloring — leave room for the data

Synoptic colors *matched* areas at render time. The fill you put in the file is
only the resting/unmatched look. Therefore:
- Give areas a **neutral resting fill** (the examples use light greys/blues like
  `#D9DDEF`, `#F4F6FA`, `#D9D9D9`). Avoid strong colors that imply data.
- It is fine — and recommended — to keep a thin `stroke` so region borders are
  visible (examples use `stroke="#6978BE"` or `#0B0000`, `stroke-width` 1.5–2).
- Per-area inline `fill`/`stroke` attributes are fine. Avoid CSS `!important`
  or stylesheet rules that would fight the visual's dynamic colors.

## 7. Structural conventions observed in the good files

- Root `<svg>` always declares `xmlns="http://www.w3.org/2000/svg"` and a
  `viewBox`. Width/height are optional but harmless. A `viewBox` is what makes
  the map scale crisply, so ALWAYS include one.
- A single outer `<g>` wrapping the whole drawing is common and fine (the body
  and ship files use `<g id="Ship C detail">` / `<g id="Human Body Synoptic">`).
- Background or outline-only artwork is separated into its own group
  (`<g id="SVG background">` in the ship) and is NOT meant to be data — mark
  such groups `data-okviz-area-type="decoration"`.
- Decorative or duplicate sub-shapes that should not bind can be left with a
  generic id (the body file uses `id="Vector"` for these) or, more explicitly,
  given `data-okviz-area-type="decoration"`.
- Invisible `<rect>` "placeholders" (nearly transparent stroke) are used purely
  to anchor a label in empty space — e.g. `id="nose placeholder"`. Optional.

## 8. Minimal valid template

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
  <!-- background / outline: not data -->
  <g id="outline" data-okviz-area-type="decoration">
    <rect x="0" y="0" width="400" height="300" fill="#FFFFFF" stroke="none"/>
  </g>
  <!-- data areas: each one stable id, neutral fill, thin stroke -->
  <rect id="zone_a" x="20"  y="20" width="160" height="120"
        fill="#D9DDEF" stroke="#6978BE" stroke-width="1.5"/>
  <rect id="zone_b" x="220" y="20" width="160" height="120"
        fill="#D9DDEF" stroke="#6978BE" stroke-width="1.5"/>
  <path id="zone_c" d="M20 180 H380 V280 H20 Z"
        fill="#F4F6FA" stroke="#6978BE" stroke-width="1.5"/>
</svg>
```


## 9. Bitmap tracing note

Bitmap tracing does not relax the technical SVG rules in this file.

The source bitmap may be used for geometric reference and, when explicitly
requested, retained as decoration/context. The final Synoptic areas must still
be vector shapes/groups with stable ids.

Use `bitmap-tracing-checker-spec.md` for pre-flight confidence, boundary
recoverability, tracing invariants, and QA.
