# Operator playbook — what the CONSULTANT does, in order

The other references answer *what moves AI recommendations*. This one answers a different
question, and the one that actually costs money when it's missed:

> **What must I ask the client for TODAY so I am not blocked three weeks from now?**

The distinction matters because the highest-leverage assets in local GEO are **not things the
consultant can touch**. They are owned by the client, and getting access takes real calendar
time. Describing Google Business Profile as "the #1 local lever" inside a strategy document is
useless if nobody said, on call #1, *"I need you to add me as a manager, here's how, do it today."*

> **This happened.** On one engagement GBP access was requested on day 1 and the entity work
> shipped in the first week. On another, the identical GBP section sat inside a long off-site
> plan as a tactic; access was only requested weeks later, and everything downstream of it —
> `sameAs`, the entity loop, the local baseline — sat idle the entire time. Same methodology,
> same consultant, weeks of difference. The gap was an operator instruction, not knowledge.

---

## The one rule

**Anything with a lead time you do not control goes in the FIRST conversation** — before the
audit, before the baseline, before a line of code. Everything else can be sequenced later.

Sort every task by **who can do it**, not by how much it moves the needle:

| Owner | When to raise it | Why |
| --- | --- | --- |
| 🔴 **Only the client can** | **Call #1, in writing** | Days-to-weeks of lead time. Blocks work you cannot start without it |
| 🟡 **Client must decide** | Call #1 if it shapes the build; otherwise when the data surfaces it | You can prepare options, but not decide |
| 🟢 **You can do alone** | Any time | Never let this crowd out the red items — it feels productive and blocks nothing |

---

## 🔴 Day-1 access checklist — send this before you do anything else

Every item is something **you cannot do for them**. Ask for all of it at once; chasing them one
at a time turns one week of lead time into four.

### Access

| Ask for | Lead time | Blocks |
| --- | --- | --- |
| **Google Business Profile — manager access** | Instant if already claimed; **1–2 weeks if it needs postcard verification** | The single highest-leverage local asset. Also blocks `sameAs`, the entity loop, hours/category/photos/Q&A — i.e. most of local GEO |
| **Delivery-platform backends** (Fantuan / UberEats / DoorDash / etc.) | Days — often the owner's family member has the login | Putting the official site URL into the profiles the engines actually read |
| **Yelp / TripAdvisor / local directory claims** | Days–weeks (they verify by phone) | Correcting NAP; these turn up as cited sources constantly |
| **小红书 / 大众点评 business account** (Chinese cohort) | Days | The Chinese-engine leverage lives here, not on the website |
| **Google Search Console + Analytics** | Instant, if they have it | Impressions, AI-referral traffic, proof of movement |
| **Bing Webmaster Tools** | Instant — and BWT can import the property straight from GSC | **ChatGPT Search reads Bing's index.** Cheapest step with the largest AI-visibility payoff; sitemap submission here is a day-one action, not a nice-to-have |
| **Domain / DNS / hosting** (if you didn't build the site) | Days | Every on-site change, robots.txt, schema |
| **Written consent to publish a case study** | Ask early, use later | Your next sale. Much harder to ask for after the engagement cools |

> Frame it as one message: *"To start I need a short list — here's exactly where to click for
> each."* Make it clickable. An owner who has to research how to grant GBP access will postpone.

### Day-one submission checklist (do this on every engagement, before the clever work)

The cheapest AI-visibility wins are administrative, and they are the ones most likely to be skipped
because they feel like SEO chores rather than GEO. They are not chores: **ChatGPT Search retrieves
from Bing's index**, so a brand that is not in Bing is capped in the largest AI assistant regardless
of how good its schema is.

| Step | Needs client login? | Why it is first |
| --- | --- | --- |
| **IndexNow ping** | **No** — you host a key file on the site you control | Instant, free, works on day one even before any access is granted. `onsite-sop.md` §9 |
| **Bing Webmaster Tools** — add + verify + submit sitemap | Microsoft account (theirs or yours as a delegate) | The door into ChatGPT Search. BWT can import a property straight from Google Search Console, so do GSC first and this takes a minute |
| **Google Search Console** — verify + sitemap + request indexing | Google account | The Gemini / AI-Overviews side of the same job |
| **Confirm `OAI-SearchBot` is not blocked** | No — a `curl -A` is enough | Being in Bing is necessary but NOT sufficient: ChatGPT still fetches with its own agent, and a CDN rule can block it while robots.txt looks fine. `audit-rubric.md` #21 |

⚠️ **Verifying Bing index membership is a manual step.** Confirmed 2026-08-10: scripted checks are
blocked (curl gets a bot page for every domain, including a nonsense control; an automated browser
gets a CAPTCHA). Check `site:example.com` by hand in a browser, and read the result carefully —
Bing tends to silently rewrite a no-match `site:` query into unrelated results rather than saying
"no results", so unrelated pages mean *not indexed*, not "the check is broken".

### Facts only the owner knows — and that you WILL get wrong

Do not infer these from the storefront, the old website, or third-party listings. Ask, and write
the answers into the client's fact file as the single source of truth.

| Ask | Why it bites |
| --- | --- |
| **Exact founding date** | The website said 2013; GBP said **the following year**. "13 years" was in the hero copy and in every AI answer |
| **Which platforms are ACTUALLY live** | Six delivery stickers on the door; **only two were real** — the rest were stale promo material from years ago. Six wrong `sameAs` entries would have split the entity |
| **Current SKU list + prices** | Menus drift constantly; four items had been discontinued the week before |
| **Which attributes are configurable** | Recorded as "one heat level, not adjustable"; the owner said **three levels**. That single fact changes the FAQ, the schema, and the answer to the top complaint |
| **Who else holds the logins** | The person with the Yelp password is often a cousin, not the owner |

> **The pattern:** everything above was *observable and wrong*. Storefront signage, old sites and
> aggregator listings are all lagging copies. The owner is the only primary source — and a
> five-minute call replaces a week of confidently building on bad facts.

---

## How to explain GEO to an owner who already knows SEO (in one minute)

Most owners you sell to have paid for SEO before. That is an advantage — they understand
visibility — but it hands them a wrong mental model you must break early: **rank**.

Use the shape of the answer, not the theory:

> Search gives you ten results and a second page. Rank eighth and people still find you.
> An AI names three or four businesses. There is no fourth line and no next page.
> Not in those names = not in the conversation.

This is checkable in front of them in ten seconds, which is why it beats any explanation of
retrieval or embeddings. It also reframes the goal correctly: GEO is not "climb the ranking",
it is "be one of the few names".

Two things NOT to say:
- **"We guarantee you'll be recommended."** AI answers are non-deterministic. You raise
  probability, you don't buy placement. Say that out loud — owners assume paid placement exists
  and will suspect it either way.
- **"Customers stopped searching."** Absolute and unverifiable. "More and more people skip
  search and just ask an AI" is true and survives scrutiny.

---

## Timing you can honestly promise

Measured, not estimated:

| Step | Actual |
| --- | --- |
| Full audit, English-only site | ~10 minutes |
| Full audit, bilingual (9 engines) | ~20 minutes |
| Baseline measurement, 9 engines × ~11 prompts × 2 runs | ~1 hour |

Quote the upper end. Someone told "5 minutes" starts suspecting a broken system at minute twelve;
someone told "20 minutes" who gets it in fifteen is pleased. The cost of over-promising here is
paid in trust, not in time.

---

## 🟡 Decisions to put in front of the client

Prepare the options, present the evidence, **let them decide** — and record the decision so no
future session quietly overrides it.

- **Product/positioning problems the measurement surfaces.** When the engines consistently say
  something unflattering ("salty, not spicy enough, not cheap"), that is a *product* decision, not
  a marketing one. New content cannot paper over it. Bring it up plainly.
- **Copy that is factually loose.** If the hero says "13 years" and the real number is 12½, the
  client may still choose to keep it. That is their call — record it, and do not silently "fix" it.
- **Category / naming changes** (e.g. GBP category Restaurant → Deli). Reversible but disruptive;
  propose, then observe for ~4 weeks.

---

## ⚖️ Outreach is regulated — and in Canada the cap is $1M per violation

Phase 3 is built on emailing strangers: journalists, resource-page owners, listicle editors,
podcast hosts. **That is a commercial electronic message, and it is governed.** The skill's
"value-first, personalized, one-at-a-time" rule is good practice; it is not a legal basis.

**For a Canadian operator, CASL is the binding law, and it is materially stricter than the US
CAN-SPAM.** The essentials:

- **A website visit is not consent.** There is no "they came to my site" basis in the Act. Nor is
  a page view an "inquiry" — that requires an actual form fill or request, and it only lasts
  **6 months** (existing business relationship, s.10(10)).
- **The route that actually works is conspicuous publication (s.10(9)(b)), and it needs three
  things at once:** the address was published by that person or with their consent; the page
  carries **no** statement refusing unsolicited messages; and your message is **relevant to that
  person's role**. All three, every message.
- **Two traps that void it.** A **guessed or tool-derived address** (`first.last@company.com`) was
  never *published* by anyone — no exemption applies, no matter how correct the guess. And a
  scraped **`info@` / `contact@`** has no person behind it, so the role-relevance limb fails.
  Canadian case law is directly on point: *Blackstone* (CRTC CD 2016-428) — bulk-scraped
  addresses rejected, "conspicuous publication sets a higher standard than mere public
  availability"; *CompuFinder* (2020 FCA 103) — generic mailboxes carry no implied consent.
- **Every message needs** sender identification, a **mailing address**, contact info valid for
  **60 days**, and a working unsubscribe honoured within **10 business days**.
- **You carry the burden of proof (s.13).** So log it as you go: the URL the address was published
  on, a screenshot, the capture date, and one line on why the message fits that person's role.
  Retain **≥3 years** (s.26 limitation period). That log is the due-diligence defence (s.33) and
  the difference between $0 and a five-figure undertaking.
- **Penalties: up to $1,000,000 per violation for an individual**, $10M for an organization. A
  sole proprietor sits at the individual cap. Enforcement is real — CompuFinder $200k, Rogers
  $200k, Porter $150k, Hudson's Bay $120k, Blackstone $50k. **You are also vicariously liable
  for a contractor's sends (s.53)** — if you outsource outreach, their violations are yours.

**Operational consequences worth building around:**

- **Never send outreach from the primary domain.** It carries client mail, invoices, password
  resets and transactional sending. Domain reputation does not compartmentalize, and a burned
  root domain is a burned business.
- **Drafts, not auto-send.** Generate into the mailbox as a draft and let a human read it before
  it leaves. This is both the best-deliverability path (no bulk signature, no ESP fingerprint)
  and the design that makes the per-message consent check actually happen. With Gmail, request
  the **draft-creation scope only** — then auto-sending is impossible by construction, which is
  also the cleanest thing to be able to say to a regulator.
- **Volume ceiling is a feature.** Hand-reviewed sending caps out around 20–50/day. For a
  practice selling four-figure audits, that is the correct ceiling anyway — and blast tooling
  buys volume at the cost of the exemption you were relying on.
- **PIPEDA is not the obstacle** — its business-contact-information carve-out (s.4.01) covers
  emailing someone about their job, provided that is the **sole** purpose. Enrich, score or
  resell those contacts and the exemption drops away.
- **EU/UK:** don't run identification or tracking scripts on that traffic without prior opt-in;
  geo-gating is cheaper and cleaner than a consent banner. **China:** PIPL has no
  legitimate-interest basis and no business-contact carve-out, so a named individual's mailbox
  needs consent — but a genuinely corporate mailbox is out of scope, and the real constraint is
  deliverability, not enforcement. Use WeChat or a warm introduction instead.

> This is operator guidance, not legal advice. Before scaling outreach volume, spend an hour with
> a Canadian privacy lawyer on the evidentiary posture specifically — the rules above are
> straightforward, but s.13 means *proving* compliance is the part that bites.

---

## 🟢 What you do alone — in this order

1. **Baseline first, audit second.** The baseline rots (the site is being crawled daily); the
   audit does not. Auditing and fixing before measuring destroys your own before-picture.
2. On-site hygiene (crawler access, schema, answer-first copy) — makes them *eligible*.
3. **`sameAs` / entity loop** — but note this is 🔴-blocked: without GBP access there is no
   canonical identifier to point at.
4. Off-site citation work, aimed at the domains the baseline showed the engines actually reading.

---

## Before advising: VERIFY FROM THE SYSTEM, not from notes

Notes describe what someone recorded. **The system holds what is actually true.** On a live
engagement another session — or the client — acts between your sessions, so any status you carry
in memory is a claim about the past. Anything below is checkable in seconds and never stale:

| Question | Check | Never |
| --- | --- | --- |
| Is Search Console set up? | `dig +short TXT <domain> \| grep google-site-verification`, or a `<meta name="google-site-verification">` in the HTML | Assume from notes |
| Is the site indexable? | `curl -A "Googlebot/2.1"` the page, robots.txt, sitemap.xml; grep for `noindex` and `rel="canonical"` | Trust a previous audit |
| Is the copy actually crawlable? | Strip `<script>`/`<style>` with DOTALL, then check the marketing copy survives as real text. An i18n object like `window.I18N = {...}` means JS injection — Googlebot renders JS, **most AI crawlers do not** | Eyeball the rendered page in a browser |
| Is the entity loop closed? | Site's `sameAs` in the JSON-LD, and whether GBP's website field points back | Assume one direction implies the other |
| How old is the domain? | `whois <domain>` → Creation Date. Weeks-old domains simply have not been discovered yet | Diagnose "not ranking" before checking "not discovered" |
| What changed recently? | `git -C <project> log -8 --format="%ad %s" --date=short` | Rely on your memory of the last session |
| Is the site up / redirecting? | `curl -sI -L` for status and final URL | — |

> **This is not a substitute for your notes; it is what makes them safe.** Write durable facts
> and decisions to the client's fact file (those are not checkable — "the owner chose to keep '13 years'" lives
> nowhere else). But for anything a command can answer, run the command. A stale note produces
> confident wrong advice; a command produces the truth in two seconds.
>
> Real cost of skipping this: a full recommendation to "go set up Search Console" for a client who
> had already verified it — the TXT record was sitting in DNS the whole time, one `dig` away.

## The standing status question

Every engagement should be answerable, at any moment, in this shape:

```
🔴 Waiting on client:   GBP manager access (asked 3 days ago, no reply) · delivery-app backend login
🟡 Waiting on decision: the top complaint in AI answers is a product issue — change the product or not?
🟢 I'm doing:           off-site citations (Yelp / Xiaohongshu) · automated measurement on the 1st
```

If the 🔴 row is empty because nobody ever asked, that is the failure this document exists to
prevent. **Chase red items weekly and say so out loud** — "GBP access is still the thing holding
us up" is a legitimate, useful status update, and it moves the client.
