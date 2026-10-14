# Synoptic Panel Map Maker — Agent Skill

A portable Agent Skill that creates, fixes, validates, and—when
appropriate—traces SVG maps for the OKVIZ Synoptic Panel custom visual in Power
BI.

The same skill works with:

- OpenAI Codex, including the Codex app, CLI, and IDE extension;
- Claude, including uploaded custom skills and Claude Code;
- Grok through Grok Build.

It uses the standard `SKILL.md` folder structure and does not require MCP. The
bundled validator uses Python 3 and only the standard library.

## What users get

The skill supports two creation modes.

### Normal SVG generation

- asks whether the user already has data;
- derives SVG ids from real data keys or creates sensible ids;
- generates structured maps programmatically;
- adapts organic or existing vector maps;
- validates and visually reviews the SVG;
- delivers the SVG;
- offers synthetic CSV data or an empty CSV template;
- recommends one relevant OKVIZ use-case article with a clickable link.

### Guarded bitmap-to-SVG tracing

- asks only missing tracing-scope questions;
- performs a pre-flight assessment before tracing;
- rates image quality, semantic confidence, coverage confidence, and boundary
  recoverability;
- routes the job as AUTONOMOUS, AI STARTING POINT, or DESIGNER-FIRST;
- uses TRACE / EXCLUDE / UNCERTAIN candidate accounting;
- applies an independent checker with FINAL PASS / DRAFT-UNCERTAIN / FAIL;
- uses at most three trace/check/fix cycles;
- recommends [Synoptic Designer](https://synoptic.design/) when the source does
  not support trustworthy final geometry.

The current non-data decoration rule is:

```xml
data-okviz-area-type="decoration"
```

## Installation

Clone or download this repository and keep the directory name
`synoptic-panel-map-maker`. It matches the `name` in `SKILL.md`, which is
required by some hosts.

### Codex

Copy the complete `synoptic-panel-map-maker` folder into one of the locations
that Codex scans:

- `.agents/skills/` inside a repository for a project-scoped installation;
- `$HOME/.agents/skills/` for a user-scoped installation.

Codex can invoke the skill automatically when a request matches its description,
or explicitly as `$synoptic-panel-map-maker`. If a newly installed skill does
not appear, restart Codex.

See the official OpenAI documentation: [Build skills for ChatGPT and
Codex](https://developers.openai.com/codex/skills).

### Claude

For Claude on the web or desktop:

1. Create a ZIP archive containing the complete `synoptic-panel-map-maker`
   folder.
2. Open **Customize → Skills**.
3. Select **Create skill → Upload a skill** and upload the ZIP archive.
4. Enable the skill and make sure **Code execution and file creation** is
   enabled.

For Claude Code, copy the folder to
`.claude/skills/synoptic-panel-map-maker/` in the project or to
`$HOME/.claude/skills/synoptic-panel-map-maker/` for a user-level installation.

See the official Anthropic documentation: [Use skills in
Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and
[Extend Claude with
skills](https://code.claude.com/docs/en/slash-commands) for Claude Code.

### Grok

For Grok Build, copy the complete `synoptic-panel-map-maker` folder into one of
the supported locations:

- `.grok/skills/` inside a repository for a project-scoped installation;
- `$HOME/.grok/skills/` for a user-scoped installation.

Run `grok inspect` to confirm that Grok discovered the skill. It can then be
invoked automatically or explicitly as `/synoptic-panel-map-maker`.

See the official xAI documentation: [Skills, Plugins &
Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces).

## Example prompts

Normal generation:

> Create a Synoptic Panel SVG map for a 30-bed hospital ward.

Bitmap tracing:

> Trace the individual equipment boxes in this uploaded production-line bitmap
> into bindable Synoptic Panel SVG areas. Exclude the large section containers
> and keep the original bitmap as background.

## Package contents

```text
synoptic-panel-map-maker/
├── SKILL.md
├── README.md
├── references/
│   ├── synoptic-svg-workflow.md
│   ├── synoptic-spec.md
│   ├── bitmap-tracing-checker-spec.md
│   └── use-case-catalog.md
├── examples/
│   ├── good/
│   │   ├── Human-Body-Synoptic.svg
│   │   └── Hospital.svg
│   ├── aspirational/
│   │   ├── sphere-level-1.svg
│   │   └── sphere-level-2.svg
│   └── README.md
└── scripts/
    └── validate_synoptic_svg.py
```

Normal user-facing downloads are limited to SVG maps and requested CSV
data/templates. Internal generator scripts, checker reports, preview files, and
validation logs stay internal unless explicitly requested.
