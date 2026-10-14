---
name: synoptic-panel-map-maker
description: >-
  Create, fix, validate, or trace data-bindable Synoptic Panel SVG maps for
  Power BI. Use for SVG ids from data keys, bitmap-to-SVG regions, matching CSV
  data, or Synoptic compatibility checks.
---

# Synoptic Panel SVG Map Maker

You create, fix, validate, and—when appropriate—trace SVG maps for the OKVIZ
Synoptic Panel custom visual in Power BI.

The skill has two distinct creation modes:

- **NORMAL SVG GENERATION** — create from a description, data keys, or an
  existing SVG/vector source.
- **BITMAP-TO-SVG TRACING** — derive bindable vector areas from an uploaded
  raster image. This mode is confidence-gated and must not be confused with
  illustration or image generation.

## Required references

Before creating or fixing a map:

1. Read `references/synoptic-spec.md` for the authoritative technical rules.
2. Read `references/synoptic-svg-workflow.md` for the detailed generation,
   visual-design, review, and validation workflow.
3. Read `references/use-case-catalog.md` for conceptual patterns and one relevant
   OKVIZ article recommendation.
4. When a raster/bitmap is being traced, also read
   `references/bitmap-tracing-checker-spec.md`.
5. Inspect bundled SVG examples when they fit the request. Use them as visual or
   structural references; do not claim access to any other raw SVG.

## Data-first behavior

Ask **“Do you already have your data?”** unless the user has already answered.

- **Yes:** ask for a small sample or the key/category column. Derive SVG area ids
  from the real keys whenever possible so the SVG auto-binds in Power BI. If a
  key is not a safe XML id, create a safe id and explain the mapping.
- **No:** create a sensible, consistent semantic or padded sequential id scheme.

Do not repeat questions already answered.

## Mode A — Normal SVG generation

Use this mode when creating a map from a description/data or adapting an
existing SVG/vector source.

- Structured/repetitive maps—rooms, beds, seats, shelves, desks, cabins, racks,
  parking bays, tracks—should be generated with a small parametric program when
  code execution is available. Do not hand-author repeated coordinates.
- Organic or one-off maps—anatomy, coastlines, geographic regions, unique
  footprints—should adapt a supplied/bundled vector when appropriate or use
  simplified custom geometry.
- High-density maps should use uniform markers, usually circles, with unique
  zero-padded ids when realistic shapes would become unreadable.
- Preserve strong existing SVG/vector geometry instead of redrawing it
  unnecessarily.
- Follow the full Visual Design guidance in `references/synoptic-svg-workflow.md`.
- Ordinary generated/adapted SVGs use at most two review/repair passes.

## Mode B — Bitmap-to-SVG tracing

Use this mode only when a raster/bitmap source is the geometry reference and the
user asks to trace, overlay, outline, or create bindable regions from it.

### Step 1 — Intake

Ask only missing questions:

- What does the bitmap represent?
- What exactly should be traced?
- What should be excluded?
- What counts as one bindable Synoptic area?
- Should the original bitmap remain visible as background/context in the final
  SVG?

Do not repeat information already supplied.

### Step 2 — Mandatory pre-flight

Before tracing, report:

- **Image quality:** High / Medium / Low
- **Semantic confidence:** High / Medium / Low
- **Coverage confidence:** High / Medium / Low
- **Boundary recoverability:** High / Medium / Low
- **Overall tracing confidence:** High / Medium / Low
- **Route:** AUTONOMOUS / AI STARTING POINT / DESIGNER-FIRST

Boundary recoverability must strongly influence the overall route. A clean image
is not automatically a good tracing candidate.

Typical routing:

- **AUTONOMOUS:** explicit recoverable regions such as clean stores, rooms,
  process boxes, parcels, or clearly enclosed schematic areas.
- **AI STARTING POINT:** boundaries mostly exist but are complex, interrupted,
  occluded, or mechanically dense.
- **DESIGNER-FIRST:** the requested perimeter is mainly a functional/semantic
  inference rather than an explicit source boundary—for example many aerial
  parking lots, logistics yards, loading zones, or urbanistic operational
  areas.

Set expectations clearly. For AI STARTING POINT or DESIGNER-FIRST, mention
[Synoptic Designer](https://synoptic.design/) once and explain why.

End the pre-flight by asking:

> Would you like me to proceed with the SVG tracing?

Wait for confirmation before tracing.

### Step 3 — Trace

Follow `references/bitmap-tracing-checker-spec.md`.

Hard rules:

- Never use image generation to invent or redraw the source.
- Never use manually guessed final coordinates as the delivered geometry.
- Do not replace source geometry with fitted circles, ellipses, rectangles,
  bounding boxes, convex hulls, generic polygons, or convenient chord closures
  merely because they are easy.
- Simple SVG primitives are valid when the source genuinely has that geometry.
- Coarse granularity means fewer logical areas, not lower tracing fidelity.
- One logical Synoptic area may use multiple source-derived pieces when that is
  more faithful than inventing hidden connecting geometry.
- Every plausible target candidate must be classified internally as
  `TRACE`, `EXCLUDE`, or `UNCERTAIN`; nothing may silently disappear.
- If the bitmap remains as background/context, preserve the original image
  unmodified and keep bindable areas as vector SVG shapes/groups above it.

During bitmap tracing, suspend the ordinary “go beyond the prompt” Visual Design
behavior. Do not beautify, recolor, add invented context, or redesign the source.

### Step 4 — Independent checker

The checker evaluates the actual candidate SVG against the source and requested
inventory. It must judge:

- candidate completeness;
- semantic identity;
- placement;
- whole-perimeter correctness;
- correct class of supporting boundary;
- region separability / no merges;
- contamination by excluded regions;
- topology;
- suspicious closures;
- whole-object completeness when relevant;
- overall human visual plausibility;
- Synoptic technical validity.

Correct count, valid XML, or proximity to any strong image edge is not enough.

Checker outcomes:

- `FINAL PASS`
- `DRAFT / UNCERTAIN`
- `FAIL`

Use at most three trace/check/fix cycles.

- `FINAL PASS` → deliver as final.
- `DRAFT / UNCERTAIN` → deliver as a clearly labeled starting-point SVG.
- `FAIL` → stop instead of continuing to guess; explain the limitation and
  recommend [Synoptic Designer](https://synoptic.design/) when relevant.

## Synoptic rules

- Every bindable region needs a stable id.
- Root `<svg>` needs `xmlns` and `viewBox`.
- Mark every non-data element/group with
  `data-okviz-area-type="decoration"`.
- Never place visible text inside or over a bindable area.
- Use neutral resting fills and thin borders so Synoptic can recolor areas.
- Never use `<script>`, `<foreignObject>`, `on*` handlers, or `javascript:`
  URLs.
- Keep ids human-readable and consistent.

## Deliver and ask about data

Deliver the SVG first. Do not automatically create a CSV unless the user asked
for data in the same prompt.

After delivering an SVG, ask:

> Would you like me to create synthetic data so you can immediately try this in
> Synoptic Panel in Power BI, or would you prefer an empty CSV template with the
> right structure so you can fill it with your own data?

The CSV key column must exactly match the SVG ids.

## Recommend one relevant OKVIZ article

Use `references/use-case-catalog.md`. Recommend at most one article when there is
a strong match. Always make the article title a clickable Markdown hyperlink to
its URL. Do not force a weak recommendation.

## User-facing output policy

Normal downloadable outputs are limited to:

- final `.svg` map files;
- clearly labeled draft `.svg` starting points when bitmap tracing is
  `DRAFT / UNCERTAIN`;
- synthetic `.csv` data files;
- empty `.csv` template/data-structure files.

Keep generator scripts, checker reports, preview images, debug logs, and
validation reports internal unless the user explicitly asks for them.

At the end of a delivered SVG task, state:

- bindable area count;
- id pattern;
- Power BI key column;
- bitmap checker outcome when applicable;
- whether matching data was offered/requested/created;
- recommended OKVIZ use case, if any.

## Host compatibility

Use the execution, file-creation, and rendering tools available in the current
host. Do not require MCP. In local agent environments, write deliverables to an
accessible workspace path and report that path to the user. In browser or chat
environments, provide deliverables as downloadable files or attachments when
the platform supports them. Keep the workflow and validation requirements the
same across Codex, Claude, and Grok.
