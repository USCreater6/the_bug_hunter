# Phase B — read-only code-review fleet + auto-flow

Phase B of the C -> B -> D plan. It automates the **safe** parts of hunting:
program triage, read-only code review, manual test-plan prep, and report drafting.
Live testing of any third-party target stays manual and yours.

## Two forms (you chose both)
- **Skills (now):** `phase_b/skills/` — work in Claude today, no server, no terminal.
- **MCP server (later):** `phase_b/mcp/` — the same tools on the cloud VM, when you provision it.

## The skills
| Skill | Does | Live traffic? |
| --- | --- | --- |
| `code-review-orchestrator` | Read-only source review across vuln classes -> candidates | No |
| `program-triage` | Reads a pasted policy -> scope, exclusions, worth-it | No |
| `test-plan-gen` | Hypothesis -> minimal MANUAL test plan | No (you run it) |
| `report-draft` | Validated finding -> report + fix | No (you submit) |
| `skill-check` | Tests YOU (quiz + scenarios), scores weak areas | No |

The auto-flow that chains them: `AUTO_FLOW.md`.

## Tracks
Open-source code review first (huntr / advisories — authorized source review,
best fit for the fleet), then small web/API programs.

## Hard rules
- Read-only on any third-party code. Active testing only on assets you own, by you.
- Nothing is auto-submitted. Every live step and every submission is a human gate.
- AI pinned to `claude-opus-5-5`.
- This is the automatable half; the manual half lives in `../copilot/` and the 5-day plan.
