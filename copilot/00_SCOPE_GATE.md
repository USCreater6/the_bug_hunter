# 00 — Scope Gate (run BEFORE every session)

Answer every line. One "no" = stop. This is the authorization spine of the whole kit.

## Authorization

- [ ] I am enrolled in this program (account created, rules read today).
- [ ] The exact asset I will test is **explicitly listed in scope** on the program's policy page.
- [ ] The bug class I'm chasing is **not** on the program's exclusions list.
- [ ] I am using my `@wearehackerone.com` alias (or the program's required test identity).
- [ ] For Shopify-style programs: I am testing **only a store/account I created myself**.

## Rules of engagement

- [ ] I have read the program's rules on automated tools and rate limits, and I will stay inside them.
- [ ] I will send requests at human speed, by hand, from one browser/Repeater — no scanners, no Intruder on live sites.
- [ ] I will only use my own test accounts and synthetic data.
- [ ] If I see data that isn't mine, I will stop, not copy it, and follow the program's data-handling rule.

## Session limits

- [ ] Request budget for this session (write a number): ______. Stop at it.
- [ ] One target this session. (No cross-target context bleed.)

## If testing my own asset instead (owned-asset mode)

- [ ] The domain/app is one I own (GauriLabs / my Shopify test store). No program rules apply, but I still log everything.

**Did every box get ticked? If not, do not proceed. Ask Claude what's missing before testing.**
