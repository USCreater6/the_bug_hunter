---
name: report-draft
description: Draft a bug-bounty report from a finding the human has already validated, using the standard template. Keeps impact factual, never inflates severity, never auto-submits. Use after manual validation passes the triage gate.
---

# report-draft

Drafts a report from a **validated** finding. The human decides whether to submit.

## Precondition
The finding has passed `copilot/03_TRIAGE_GATE.md` (reproduced 3x, in scope, real
impact, not a known exclusion, evidence redacted). If it hasn't, say so and stop.

## Output (fill the template)
```
Title: <class> on <asset> allows <impact in a few words>
Affected asset: <exact in-scope URL/endpoint>
Severity: <Low/Medium/High/Critical — matched to demonstrated impact>
Prerequisites: <accounts/conditions, all your own test accounts>
Steps to reproduce (minimal):
  1. ...
Expected vs observed:
  - Expected: ...
  - Observed: ...
Impact: <concrete harm — who, what data/action, scale. No inflation.>
Evidence: <redacted request/response + screenshot/video>
Suggested remediation: <the fix in 1-3 sentences, where justified>
```

## Hard rules
- Never invent evidence or steps you weren't given.
- Severity matches demonstrated impact, not potential.
- One finding per report unless the program says otherwise.
- **Never auto-submit.** Output the draft; the human submits.
