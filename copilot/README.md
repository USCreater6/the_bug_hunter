# Copilot Kit — Phase C (manual hunt, Claude as copilot)

This is Phase C of the C → B → D plan.

- **C (this kit):** you hunt manually and in-scope; Claude assists each step — explains traffic, stress-tests your hypothesis, checks exclusions, drafts the report. Nothing runs unattended. Nothing is submitted without your decision.
- **B (next build):** a read-only code-review MCP fleet, once you have HackerOne Signal.
- **D (later):** the same fleet pointed at paying customers' code, with their authorization.

## How to use it

1. Finish the 5-day plan first (separate doc). This kit assumes you can read a request and use Burp Repeater.
2. Before touching any target, run `00_SCOPE_GATE.md`. If any answer is "no", stop.
3. Hunt using the loop in `01_WORKFLOW.md`.
4. At each step, paste the matching prompt from `02_COPILOT_PROMPTS.md` into a Claude chat. Claude explains and reviews; **you** click, type, and send every request.
5. Before you even consider submitting, run `03_TRIAGE_GATE.md`.
6. Draft with `04_REPORT_TEMPLATE.md`. You decide whether to submit.

## Hard rules (non-negotiable)

- Active testing only on (a) assets you own, or (b) a program you are enrolled in, within its written rules.
- On any bounty program: use your `@wearehackerone.com` test account, on a store/account you created.
- No scanners, no automated traffic, no Intruder runs against live third-party sites.
- Claude never sends live requests to a third-party target for you. It explains, reviews, and drafts only.
- Nothing is auto-submitted. Ever.

## What this kit is not

It is not an exploit tool and not an automated hunter. It is a discipline layer + a copilot prompt set, so your manual work is in-scope, well-evidenced, and reportable.
