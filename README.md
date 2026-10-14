# Synoptic Panel SVG Map Maker — Claude Plugin

Create, trace, fix, and validate data-bindable SVG maps for the OKVIZ Synoptic Panel custom visual in Power BI.

This Claude plugin packages the canonical **Synoptic Panel Map Maker** Agent Skill. It supports normal SVG generation from descriptions, data keys, or existing vector sources; guarded bitmap-to-SVG tracing when source boundaries are sufficiently recoverable; Synoptic compatibility validation; matching CSV structures; and relevant OKVIZ use-case recommendations.

The plugin is intentionally **skills-only** and does not require an MCP connector.

## Included skill

`skills/synoptic-panel-map-maker/`

The bundled skill contains:

- `SKILL.md` — workflow and behavioral instructions
- `references/` — Synoptic technical rules, SVG workflow, bitmap tracing checker specification, and use-case catalog
- `scripts/validate_synoptic_svg.py` — deterministic Synoptic SVG validator
- `examples/` — good and aspirational SVG examples

## Test locally in Claude

Upload the ZIP from:

**Claude → Customize → Plugins → Add → Upload plugin**

With Claude Code you can also run:

```bash
claude plugin validate ./synoptic-panel-map-maker
claude --plugin-dir ./synoptic-panel-map-maker
```

Suggested test prompts:

1. “Create a Synoptic Panel SVG map for a hospital ward. I do not have data yet.”
2. “I have data already. Help me create an SVG map whose IDs match my data keys.”
3. “Trace the bindable regions in this bitmap into a Synoptic Panel SVG.”

## Source

Canonical project: https://github.com/okviz/synoptic-panel-map-maker

## License

MIT © 2026 OKVIZ
