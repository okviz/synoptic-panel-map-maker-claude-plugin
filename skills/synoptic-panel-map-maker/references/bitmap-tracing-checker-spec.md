# Bitmap Tracing Checker Specification

## Purpose

This is the independent QA specification for raster/bitmap-to-SVG tracing for
Synoptic Panel.

The tracer creates geometry. The checker does **not** draw or repair geometry.
It judges the actual candidate SVG against the original source bitmap and the
user's requested tracing inventory.

Technical SVG validity is necessary but never sufficient for tracing quality.

## Required inputs

1. Original source bitmap.
2. Candidate SVG.
3. Requested tracing scope.
4. Explicit exclusions.
5. Logical area inventory / intended granularity.
6. Prior accepted checkpoint when one exists.

## Pre-flight confidence

Assess four dimensions before tracing.

### Image quality
Sharpness, contrast, resolution, noise, and clutter.

### Semantic confidence
How reliably the requested objects/regions can be identified.

### Coverage confidence
How likely all requested targets can be found without silently dropping any.

### Boundary recoverability
How directly the requested perimeter is encoded in the source.

**Boundary recoverability strongly controls the overall recommendation.**

A bitmap may be very clean and semantically obvious while still being a poor
autonomous-tracing candidate if the requested area's exact perimeter is inferred
rather than explicitly represented.

## Routing

### AUTONOMOUS
Use when the requested regions have explicit, recoverable boundaries.

Typical examples:
- clean process/equipment boxes;
- rooms/stores with clear closed walls;
- clearly outlined parcels/zones;
- simple schematic regions.

### AI STARTING POINT
Use when boundaries are mostly recoverable but complex, interrupted, occluded,
or mechanically dense.

Typical examples:
- exploded machinery;
- technical line drawings;
- physical components with partial occlusion.

### DESIGNER-FIRST
Use when the exact perimeter is mainly a semantic/functional inference.

Typical examples:
- aerial parking lots without explicit outer boundaries;
- logistics yards/loading zones;
- circulation areas;
- many urbanistic/site-plan operational zones.

For DESIGNER-FIRST, recommend
[Synoptic Designer](https://synoptic.design/). Produce a rough AI starting SVG
only if the user explicitly chooses to proceed after the limitation is explained.

## Candidate accounting

Before filtering, enumerate every plausible target candidate.

Every plausible candidate must become exactly one of:

- `TRACE`
- `EXCLUDE`
- `UNCERTAIN`

Nothing may silently disappear.

## Topology inventory

For each logical area, track when relevant:

- id / label;
- whole-object requirement;
- whether disconnected pieces are allowed;
- whether an inner hole must be preserved;
- whether limited occlusion reconstruction is allowed;
- semantic ownership notes.

One logical Synoptic area does not always require one contiguous SVG path.
Multiple source-derived visible pieces may belong to one logical area when that
is more faithful than inventing unsupported connecting geometry.

## Hard tracing invariants

### 1. No image generation
Do not generate, redraw, repaint, or reinterpret the source as a new image.

### 2. No guessed final geometry
Manual points may help define an ROI or semantic anchor, but delivered
boundaries must be source-supported and checked against the original image.

### 3. No convenient primitive substitution
Do not use fitted circles, ellipses, rectangles, bounding boxes, convex hulls,
generic polygons, or straight-chord closures merely because they are convenient.

A simple SVG primitive is valid when the source itself genuinely has that
geometry.

### 4. Granularity does not reduce fidelity
“Coarse” means fewer logical areas, not rougher tracing.

### 5. Do not force topology
Do not connect disconnected visible pieces simply to manufacture one filled
path.

### 6. Occlusion reconstruction is limited
Hidden geometry may be minimally reconstructed only inside a genuine occlusion
caused by another identified component. Never invent a boundary across visible
unsupported space.

### 7. Preview must be deterministic
If an internal preview is needed, it must render the exact SVG candidate
geometry over the original source. Never use a separately generated or
illustrated preview.

Do not expose preview files to the user unless explicitly requested.

## Blocking checks

### Candidate completeness
Every plausible requested region must be accounted for as TRACE, EXCLUDE, or
UNCERTAIN. Missing an obvious requested candidate is a FAIL.

### Semantic identity
Each bindable area must correspond to the intended object/region, not merely a
nearby strong edge or visually similar shape.

### Correct placement
At full-image scale, the SVG area must actually lie over the intended source
region. Correct count with wrong placement is a FAIL.

### Whole-perimeter correctness
Judge the complete perimeter, not only anchor points or vertices.

Flag:
- unsupported long chords;
- boundaries that leave the intended object;
- boundaries following unrelated nearby detail;
- excessive jaggedness caused by cars, trees, shadows, annotations, parking
  stripes, dimension lines, or internal mechanical detail.

### Correct edge class
**Edge proximity is not evidence of boundary correctness.**

A polygon segment touching a real edge is not enough. The edge must represent
the correct semantic boundary for the requested area.

### Functional-boundary check
For operational zones—parking lots, yards, loading areas, storage zones,
circulation areas—determine whether the source actually provides a defensible
outer boundary.

If the perimeter is mainly inferred from context, the result cannot receive
FINAL PASS merely because the area is easy to recognize.

### Region separability / no merge
Physically distinct requested regions must remain distinct.

Flag merged:
- parking lots connected through a road/circulation zone;
- neighboring rooms/stores/components;
- unrelated physical regions grouped as one catch-all area.

### Interior contamination
Flag substantial inclusion of excluded neighboring content such as roads,
buildings, common corridors, landscaping, service areas, or unrelated
components.

### Topology correctness
Verify:
- solid regions are appropriately closed;
- required holes are preserved;
- open structures are represented appropriately;
- disconnected pieces are used only when the inventory allows them.

### Whole-object completeness
For physical components, verify the intended whole component is represented at
the selected granularity rather than only one side/face/fragment.

### Suspicious closure
Inspect explicit and implicit path closures. A closure that exists only to force
a path closed and is not supported by source geometry or genuine occlusion is a
FAIL.

### Preservation
Accepted checkpoint geometry should not be modified unless the checker flags it
or the user requests a revision.

### Human-plausibility / gestalt
At full-map scale ask:

> Would a competent human comparing the source and overlay immediately agree
> that these areas are on the right objects and shaped like those
> objects/regions?

If clearly no, the candidate FAILS regardless of count, edge-distance metrics,
or XML validity.

### Synoptic technical validity
Verify:
- `xmlns` and `viewBox`;
- stable ids;
- decoration uses `data-okviz-area-type="decoration"`;
- neutral resting styles;
- no text on bindable areas;
- no script, foreignObject, event handlers, or javascript URLs.

## Outcome

### FINAL PASS
No blocking failures; requested inventory is accounted for; geometry and
placement are trustworthy enough to deliver as final.

### DRAFT / UNCERTAIN
The SVG is useful as a starting point, but one or more boundaries remain
ambiguous. Name the limitation clearly.

### FAIL
Wrong placement, missing requested region, merged areas, unsupported/invented
boundary, gross contamination, topology failure, or visually implausible
overlay.

A FAIL must not be presented as final.

## Bounded review cycle

1. Trace.
2. Inspect/render the actual SVG candidate against the original source.
3. Checker.
4. Fix only flagged FAIL/UNCERTAIN areas.
5. Recheck every modified area.
6. Perform a final full-map check.

Maximum: **3 trace/check/fix cycles**.

After the third cycle:
- deliver as final only with FINAL PASS;
- deliver as a starting-point SVG only with DRAFT / UNCERTAIN;
- if blocking FAIL remains, stop and recommend
  [Synoptic Designer](https://synoptic.design/) rather than continuing to guess.

## Calibration patterns

These are confidence calibration examples, not geometry templates.

- **Clean process/equipment diagram:** usually AUTONOMOUS.
- **Mall/store plan with explicit closed store units:** usually AUTONOMOUS after
  semantic intake and candidate completeness checks.
- **Complex exploded machinery:** usually AI STARTING POINT.
- **Realistic aerial or urban/site-plan parking zones without explicit outer
  perimeters:** usually DESIGNER-FIRST or at best DRAFT / UNCERTAIN.

Do not award High confidence merely because the source looks clean.
