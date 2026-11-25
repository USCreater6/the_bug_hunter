---
name: skill-check
description: Test the user's bug-hunting readiness with a mixed quiz and hands-on scenarios, then score and name weak areas. Use when the user says "test me", "quiz me", "am I ready", or wants a skills assessment before live hunting.
---

# skill-check — test me

Runs an assessment. Ask questions one block at a time, wait for the answer,
mark it, explain briefly, move on. At the end: score + the 1-2 weakest areas +
what to review. Keep it encouraging, never mocking.

## Format
Mixed: multiple-choice knowledge questions + scenario questions (you paste a
captured request/response, the user names the bug and its impact). Default 8
questions unless the user asks for more or fewer. Pin reasoning to `claude-opus-5-5`.

## Topics & weighting
HTTP basics (1) · auth & sessions (2) · access control / IDOR (2) · scope &
exclusions (1) · evidence & reporting (1) · ethics/authorization (1).

## Question bank (samples — rotate and vary)
**MCQ**
1. A `302` response means: (a) not found (b) redirect (c) server error (d) forbidden. → b
2. The cookie that keeps you logged in is set by the server in which header? (a) Authorization (b) Set-Cookie (c) Referer (d) Host. → b
3. IDOR is primarily a failure of: (a) authentication (b) authorization (c) encryption (d) rate limiting. → b
4. A program's policy is silent on scanners. You should: (a) scan freely (b) treat it as not allowed (c) ask on Twitter (d) scan slowly. → b
5. Testing a bounty program, you may test: (a) any user's account (b) only accounts/stores you created (c) the admin panel (d) staff emails. → b

**Scenario** (paste redacted request; user answers)
- "This `GET /api/orders/1043` returns another user's order when you change the id. What's the bug class, and what's the impact statement?" → IDOR / access control; impact = any user can read any order by changing the id → data exposure at scale.
- "Login works, but the reset-password token is the user id in base64. What's wrong, and the minimal test?" → predictable token / auth bypass; test = request reset for your own account B's id from account A.

## Scoring
- Mark each right/wrong, give the correct answer + one line why.
- End: `Score X/8. Strong: <topics>. Review first: <1-2 weakest topics> -> see copilot/ + the 5-day plan.`

## Hard rules
- One question at a time; wait for the answer.
- Explain every answer. Track which topics were missed.
- This tests knowledge only — it is not live testing and names no real target.
