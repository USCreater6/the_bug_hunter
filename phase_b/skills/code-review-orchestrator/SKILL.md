---
name: code-review-orchestrator
description: Read-only security code review over source you are allowed to read (your own code, or open-source in an authorized program like huntr). Fans out across vulnerability classes and produces candidate findings for you to manually validate. Never sends network traffic. Use when reviewing a repo or file for bugs.
---

# code-review-orchestrator

Read-only. This skill **reads source files** and reasons about them. It never
sends a request to any live target, never runs the code, and never tests a
third-party system. Active validation is always done by the human, separately.

## When to use
- You have source you are authorized to read: your own repos, or an open-source
  project in a platform that authorizes code review (e.g. huntr.dev, a program
  whose scope includes source).

## Inputs
- A path to a repo or file the user points you at, pinned to `claude-opus-5-5`.

## Review passes (one per class — the "fleet")
Run each pass as a focused read. For each, cite `file:line`.

1. **Access control / IDOR** — object lookups that trust a client-supplied id without an ownership check.
2. **Authentication** — password/reset/session flows; missing checks, weak token generation.
3. **Injection** — SQL/command/template built from unsanitized input.
4. **SSRF** — server-side fetches of user-controlled URLs.
5. **Deserialization / unsafe eval** — untrusted data into `pickle`, `yaml.load`, `eval`.
6. **Path traversal / file handling** — user input in file paths.
7. **Secrets / crypto** — hardcoded secrets, weak hashing, missing verification.
8. **Business logic** — state/price/quantity changes without server-side checks.

(The repo's upstream `hunt-*` skills hold deep per-class patterns — read them for detection detail, but keep this review read-only.)

## Output — one block per candidate
```
[class] file:line
What: <the pattern you see, in one sentence>
Why it may be a bug: <the missing check / the trust boundary crossed>
Confidence: low | medium | high
Manual validation needed: <the ONE test the human must run to confirm>
```

## Hard rules
- Read-only. No network, no execution, no live testing.
- A candidate is a **hypothesis**, not a finding, until a human validates it.
- Do not inflate confidence. "Looks like" is `low`.
- Feed confirmed candidates to `test-plan-gen`, then (after the human validates) `report-draft`.
