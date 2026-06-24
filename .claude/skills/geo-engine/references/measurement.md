# Phases 0 & 4 — Measurement & reporting

The measurement layer is what makes GEO a *service* instead of a favor: it sets the baseline that proves your value, and the monthly report **is** the retainer deliverable and the case-study fuel for selling the next client. Stand it up in Phase 0; run it on a fixed cadence in Phase 4.

The honest framing for the client: AI answers are **non-deterministic and personalized** — the same prompt gives different answers across users and days. So we measure a **rate over a fixed prompt set across runs**, and track the **trend**, never a single lucky (or unlucky) snapshot.

---

## 1. Build the prompt-test set (do this in Phase 0)

The compass and the scoreboard, both. 15–30 **real questions** a buyer would actually ask an AI — the ones where this brand should be recommended. Cover:
- **Head terms:** "best [category] [region]", "[category] tool", "[service] in [city]".
- **Long-tail / specific:** "how much is [X]", "[product] vs [competitor]", "[service] for [audience]".
- **Languages**, if the brand serves more than one (CanPay tracks EN + ZH + FR).
- A few **branded** prompts ("is [brand] any good?") to see what AI already says about them.

Keep the set **fixed** once chosen — changing prompts breaks comparability. Add new ones in a clearly-marked second cohort if the strategy expands.

## 2. The manual method (always works — the floor)

Every month, ask each prompt in **ChatGPT, Perplexity, Gemini, Google AI Overviews, and Claude**, and record for each cell:
- **Mentioned?** (brand named at all)
- **Linked?** (a clickable link to the brand)
- **Rank/prominence** (first recommendation, in a list, footnote)
- **Alongside whom** (which competitors share the answer)
- **What got cited** (which domains/pages the engine used)

**Sample enough that the number isn't noise.** AI answers vary run-to-run, so a single ask per prompt is a coin-flip, not a measurement. Run **each prompt ~3× per engine per month**, in fresh/logged-out sessions, and record the per-cell rate as **hits ÷ runs**. Log the **model/version and region** per run (engines swap models constantly).

Tracker shape — one **append-only row per prompt × engine × run** (long format; every KPI and chart derives from this one file, so "archiving" = keeping it):

| date | month | prompt_id | engine | run | mentioned | linked | prominence | competitors | source_cited | model_version | region |
|---|---|---|---|---|---|---|---|---|---|---|---|

Derive the headline KPIs by **averaging**: mention rate / link rate = mean of per-prompt (hits ÷ runs), per engine and overall, per month. That trend line is the story you sell.

> **Read the trend, not the wobble.** With ~20 prompts a month-over-month swing under ~±5–10 points is mostly sampling noise — only a **sustained 3+ month move** is signal. Tell the client this up front so a noisy month doesn't spook anyone.

## 3. The instrumented method (Ahrefs Brand Radar — the enterprise backbone)

If the user has **Ahrefs Brand Radar** (or a comparable AI-visibility platform) connected, use it to make the report robust and scalable instead of hand-collected. Discover the tools at runtime — don't hardcode server names:

```
ToolSearch query: "brand radar ai responses share of voice cited domains"
```

That surfaces capabilities for:
- **AI mentions** — overview + history of how often the brand appears in AI answers.
- **Share of voice (SOV)** — the brand's share of AI mentions vs. named competitors, over time. This is the cleanest single enterprise KPI.
- **AI responses** — the actual prompts/answers where the brand (or competitors) shows up.
- **Cited domains / cited pages** — which sources the AI engines pull from for the niche (this tells you *exactly which off-site placements to chase* in Phase 3 — go get cited where the engines already look).
- **Prompts & reports management** — register the prompt-test set and schedule recurring reports.

Pull SOV + mentions history for the trend, and cited-domains for the niche to feed the off-site target list. Also useful from the same suite: **Search Console** tools (`gsc-*`) for impressions/clicks/query deltas (the retrieval path), and **web-analytics** for referral traffic. When a tool's response includes a `render_with` directive, call the specified render tool — don't dump raw rows.

## 4. Watch the logs (cheap corroboration)
- **AI-referral traffic** — ChatGPT Search sends `utm_source=chatgpt.com`; Perplexity and others send referrers. Track in GA4 / Vercel Analytics / server logs.
- **AI crawler hits** — watch for the AI bots (`OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`, `GPTBot`, … — full list in `onsite-sop.md` §1) in access logs; rising crawl = rising eligibility.
- **GSC** — impressions/clicks/queries and which pages rank (AI Overviews draw from this index).

---

## Deliverable — Monthly AI-Visibility Report (client-facing template)

Keep it one page of signal. Lead with the trend, then the why, then next month's plan.

```markdown
# AI-Visibility Report — [Brand] — [month]

## Headline
[1–2 sentences: mention rate this month vs last, SOV vs competitors, the single biggest move.]

## Scoreboard
| KPI | This month | Last month | Δ |
|---|---|---|---|
| Mention rate (all engines) |  |  |  |
| Link rate |  |  |  |
| Share of voice vs competitors |  |  |  |
| AI-referral sessions |  |  |  |
| Pages cited by AI |  |  |  |

## By engine
| Engine | Mention rate | Notable wins / losses |
|---|---|---|
| ChatGPT |  |  |
| Perplexity |  |  |
| Gemini |  |  |
| Google AI Overviews |  |  |
| Claude |  |  |

## What moved it
[The 2–3 actions that drove the change — a Reddit answer that ranks, a listicle inclusion,
a journalist citation, new original-data content getting picked up.]

## Where AI still recommends competitors
[Prompts we're losing, who's winning them, and what's earning them the spot — usually a
citation source we don't have yet.]

## Next month
[The 2–3 highest-leverage actions — almost always off-site citation building + one
original-data asset, occasionally an on-site gap.]

## Notes
AI answers are non-deterministic; figures are rates over a fixed prompt set. GEO compounds —
we track the trend over months. No guaranteed placements; we report the work and the trajectory.
```

> Archive every month's raw tracker. Six months of a rising SOV line on a real brand is the most persuasive sales asset you will ever have — it's exactly how CanPay and traviszhang become case studies for the next client.
