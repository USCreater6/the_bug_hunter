# Phase B — the auto-flow

An orchestrated pipeline. The automated steps are read-only or drafting. The
**live steps are yours** — the flow stops and hands them to you. Nothing is
auto-submitted. AI pinned to `claude-opus-5-5`.

## The flow

```
1. program-triage        (auto)   policy text -> scope, exclusions, worth-it
        |
2. code-review           (auto)   read-only source review -> candidate findings
        |
   >>> HUMAN GATE <<<     you pick which candidates are worth testing
        |
3. test-plan-gen         (auto)   candidate -> minimal MANUAL test plan
        |
   >>> HUMAN GATE <<<     YOU run the test by hand, on your own/in-scope accounts
        |
4. (manual validation)   (you)    reproduce 3x, pass copilot/03_TRIAGE_GATE.md
        |
5. report-draft          (auto)   validated finding -> report + suggested fix
        |
   >>> HUMAN GATE <<<     YOU decide to submit (or shelve). Never auto-submitted.
```

## Two tracks

**Open-source first (best fit for the fleet).**
Platforms that authorize source review (e.g. huntr.dev) + published advisories.
Steps 1-2 and 5 do most of the work; the "live test" is often just building a
local PoC against code you are allowed to run.

**Web/API second.**
Small HackerOne/Bugcrowd programs. Step 2 reviews any in-scope source; the live
test (step 3-4) is fully manual, in Burp, on your own test accounts, within the
program's rate rules.

## Where it runs
- **Now:** the `phase_b/skills/` skills, invoked in Claude. No server.
- **Later:** the `phase_b/mcp/` server on your VM runs steps 1, 2, 3, 5 as tools.

## The one rule that never bends
Steps 1, 2, 3, 5 automate reading and drafting. The live request to any
third-party target is step 4 — manual, yours, in-scope, human-speed. Small
programs ban automated scanning exactly as large ones do.
