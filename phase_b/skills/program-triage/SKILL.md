---
name: program-triage
description: Read a bug-bounty program's policy text and decide if it's worth a beginner's time. Extracts in-scope assets, exclusions, paid vulnerability classes, automation/rate rules, and a worth-it verdict for small programs. Use before testing any program. Answers only from the pasted policy.
---

# program-triage

Reads a program policy the user pastes and summarizes it. Answers **only** from
the pasted text — if something isn't stated, say "not stated", never guess.

## Inputs
- The full policy text, pasted by the user. (Do not fetch it yourself for a third party.)

## Output
```
Program: <name>
In-scope assets: <list, exactly as stated>
Paid classes & bands: <severity -> reward, as stated>
Top exclusions (beginner traps): <the 5-8 most likely to catch a newcomer>
Automation / scanner rules: <quote the rule, or "not stated">
Rate limits: <stated limit, or "not stated">
Test-account / identity rule: <e.g. alias email, own-store-only>
Eligibility / country notes: <as stated>
Worth-it for a beginner: yes / marginal / no  — <one-sentence reason>
```

## Worth-it heuristic (state your reasoning, don't just assert)
- **Marginal/No** if: scanners banned AND the surface is huge and crowded; or lowest band is $0; or it requires invitation.
- **Yes** if: clear scope, a defined low/medium band, and a bug class that suits manual testing (IDOR, access control, auth).

## Hard rules
- Only the pasted text is ground truth. No memory, no assumptions.
- Silence about automation is **not** permission — mark it "not stated" and treat as restrictive.
- This is triage, not authorization to test. Authorization comes from enrolling and following the rules.
