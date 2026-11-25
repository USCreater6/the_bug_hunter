# the_bug_hunter

A personalized copy of [USCreater6/Claude-BugHunter](https://github.com/USCreater6/Claude-BugHunter)
(by Sachin Sharma, MIT / CC BY 4.0), set up for a beginner, browser-first workflow.

## What changed from upstream

| Area | Upstream | Here | Why |
| --- | --- | --- | --- |
| Engine approvals | `bypassPermissions` (auto-approve) | `default` (asks first) | You stay in control of every action |
| Autopilot loop | On | Disabled (banner in `commands/autopilot.md`) | Manual, in-scope testing only |
| Live recon scanners | Run if installed | Off unless `THE_BUG_HUNTER_ENABLE_RECON=1` | No unattended traffic |
| AI model | `claude-sonnet-4-6` default | pinned `claude-opus-5-5` | Project requirement, no fallback |
| Added | — | `copilot/` kit | Manual-hunt copilot (Phase C) |

## How I'm meant to be used (the rules)

- Active testing only on (a) assets you own, or (b) a program you are enrolled in, within its written rules.
- No live-target testing as part of setup. No scanners against third-party sites.
- Claude explains, reviews and drafts; **you** send every request and decide what to submit.
- Nothing is auto-submitted.

## Where to start

1. Do the 5-day beginner plan (separate doc) — learn to read and resend a request.
2. Use `copilot/` for the manual-hunt loop and the scope/triage gates.
3. Keep research notes and evidence OUT of git (see `.gitignore`).

## Roadmap (C → B → D)

- **C (now):** manual hunting, Claude as copilot — this repo + the copilot kit.
- **B (next):** a read-only code-review MCP fleet, once you have HackerOne Signal.
- **D (later):** the same fleet pointed at paying customers' code, with their authorization.

## Attribution

Upstream work and all its skills/docs are by Sachin Sharma and contributors, under MIT (code)
and CC BY 4.0 (content). This copy does not claim authorship of that work. See `LICENSE`,
`LICENSE-CONTENT`, `NOTICE`, and `docs/credits.md`.
