---
name: test-plan-gen
description: Turn a vulnerability hypothesis into a minimal, manual, step-by-step test plan the human runs by hand. Does not execute anything. Use after code review flags a candidate and before any manual testing. For assets you own, or an in-scope target within program rules.
---

# test-plan-gen

Produces a plan for the **human** to execute manually. It never sends requests.

## Inputs
- One hypothesis: "If I change X, the server will wrongly do Y."
- The target: an asset you own, or an in-scope program asset (named by the user).

## Output
```
Hypothesis: <one sentence>
Preconditions: <accounts/roles/data you must set up yourself — your own test accounts only>
Minimal test (by hand):
  1. <the single smallest action>
  2. <capture the request/response>
Expected (safe) result: <what a correct server does>
Observed = bug if: <what would confirm the flaw>
Evidence to capture: <request/response + screenshot, redacted>
Stop conditions: <data that isn't yours; can't explain the result; out of scope>
Request budget: <a small number — keep it human-speed>
```

## Hard rules
- You generate the plan; the human runs it. No auto-execution, no scanners.
- Smallest possible test. One change at a time.
- Own accounts and synthetic data only.
- If the target is a third-party program, the plan must stay inside the program's stated rate/automation rules (from `program-triage`).
