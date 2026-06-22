# Phase 1 — Audit (the sellable diagnostic)

Goal: see the brand the way an AI/non-JS crawler sees it, score it against the leverage hierarchy, and turn that into a prioritized roadmap. This is the cheap door-opener of a paid engagement — make it genuinely useful on its own.

## Step 1 — See what the bot actually sees

Most AI crawlers and answer engines fetch raw HTML and often **don't run JavaScript**. If content is JS-injected, it can be invisible to ChatGPT/Perplexity/Claude. This is the #1 GEO failure for modern sites — check it first.

```bash
DOMAIN=example.com

# 1) What a bot reads as clean text (renders the page to markdown):
curl -s "https://r.jina.ai/https://$DOMAIN" | sed -n '1,150p'

# 2) Are the key signals in raw HTML WITHOUT JS?
curl -sA "Mozilla/5.0" "https://$DOMAIN/" \
 | grep -iEo "<title>[^<]*|<h1[^>]*>|application/ld\+json|<meta name=.description" | head

# 3) Is it a JS-only SPA? (low word count in raw HTML = red flag)
curl -sA "Mozilla/5.0" "https://$DOMAIN/" \
 | python3 -c "import sys,re;t=re.sub('<[^>]+>',' ',sys.stdin.read());print('visible words in raw HTML:',len(t.split()))"

# 4) Do the GEO files exist?
for f in robots.txt sitemap.xml llms.txt; do echo -n "$f -> "; curl -s -o /dev/null -w "%{http_code}\n" "https://$DOMAIN/$f"; done

# 5) Are AI bots blocked? (look for Disallow targeting GPTBot/OAI-SearchBot/PerplexityBot/ClaudeBot)
curl -s "https://$DOMAIN/robots.txt"
```

If words-in-raw-HTML is tiny but the live page is full of content, you've found a JS-only site — that alone explains most invisibility, and the fix (author citable pages as static HTML) is the headline recommendation. See `onsite-sop.md`.

## Step 2 — Baseline the AI visibility

Before recommending anything, record where the brand stands today. For each target prompt from Phase 0, ask ChatGPT / Perplexity / Gemini / Google AI Overviews / Claude and log: **mentioned? linked? alongside which competitors? what got cited instead?** If Ahrefs Brand Radar (or similar) is connected, also pull AI share-of-voice and cited-domains. Full method + tracker in `measurement.md`. **No baseline = no proof of value later.**

## Step 3 — Score the rubric

Score each dimension **✅ OK / ⚠️ weak / ❌ missing**, grouped by the leverage hierarchy so the client sees *where the impact is*, not just a flat list. Note the evidence weight (🔑 strong / ◆ medium / ○ baseline).

### A. Off-site citation footprint 🔑 (the needle-mover — score honestly, it's usually the worst)
1. Does anyone independent cite/link the brand? (Reddit, forums, blogs, news, directories)
2. Is the brand in any "best [category]" listicle?
3. Does it have an entity in Wikidata / Wikipedia?
4. For local: Google Business Profile claimed? consistent across directories?
5. Are there original-data assets others *would want* to cite?

### B. Original data & content quality 🔑
6. Is there content with **specific, original numbers/stats/sources** (not generic guides)?
7. Or is the site padded with thin, AI-spun "X guide" filler? (a liability — note for pruning)
8. First-hand expertise / real examples / E-E-A-T present?

### C. Extractability ◆
9. **Crawlable text** — real copy in raw HTML, not JS-only? Any accidental `noindex`?
10. Answer-first — is the answer in the first sentence/paragraph (LLM-liftable)?
11. Question-shaped H2/H3; tables/lists/FAQs present?
12. One URL per money-topic (not everything behind `#anchors`)?
13. Internal links with descriptive anchors?

### D. Structured data ◆
14. Person/Organization (+ LocalBusiness/ProfessionalService if local) on homepage, linked by `@id`?
15. Service/Product + FAQPage + BreadcrumbList on key pages? Dataset (for tool/data brands)?
16. Do values match visible content (no fake ratings/reviews/data)? Validates?

### E. Entity & authority ◆
17. One canonical entity sentence used verbatim everywhere?
18. Consistent name/role/URL across site + LinkedIn/IG/X/GBP? (`sameAs` correct & live?)
19. Any profile *contradicting* the brand (e.g. a dev LinkedIn for a photographer)?
20. Two-name people reconciled (`alternateName`)?

### F. Crawl access & freshness ○
21. robots.txt allows Googlebot, Bingbot, **OAI-SearchBot**, GPTBot, PerplexityBot, ClaudeBot, Google-Extended, Applebot-Extended?
22. sitemap.xml present, canonical host, no internal 404s/redirects?
23. `llms.txt` present and accurate?
24. Current-year figures and dated updates (freshness)?
25. HTTPS, fast, mobile-clean, single host (www OR apex consistently)?

> Reminder of the OAI-SearchBot nuance: blocking `GPTBot` only stops training use, but **`OAI-SearchBot` is what lets ChatGPT Search cite you** — flag it as a problem only if the citation-driving bots are blocked.

## Step 4 — Prioritize (impact × effort)

Sort every ❌/⚠️ into two buckets:
- **Quick wins** (on-site, days, you can do them): robots/llms.txt, schema, answer-first rewrites, JS→static page authoring, entity-consistency fixes, internal links, indexing submission.
- **Strategic investments** (off-site, weeks–months, the real lever): original-data assets, Reddit/community program, journalist & listicle outreach, Wikidata entity, review building.

Lead the roadmap with the strategic investments by *impact*, even though the quick wins ship first by *sequence* — so the client understands where results actually come from.

---

## Deliverable — GEO Audit Report (client-facing template)

Use this exact structure. Keep it scannable; lead with the verdict.

```markdown
# GEO Audit — [Brand] — [date]

## Executive summary
[2–4 sentences: where they stand in AI answers today, the single biggest opportunity,
and the realistic trajectory. Honest, outcome-framed, no guarantees.]

## AI-visibility baseline
[Table: target prompt × engine → mentioned? linked? who was recommended instead?]
| Prompt | ChatGPT | Perplexity | Gemini | AI Overviews | Who AI recommended |
|---|---|---|---|---|---|

## Scorecard
[The rubric, grouped A–F, each dimension ✅/⚠️/❌ with a one-line note.
Show the group scores so the leverage picture is obvious.]

## What's costing you the most
[The 3–5 highest-impact gaps, each: the gap → why it matters for AI → the fix.]

## Roadmap
### Quick wins (on-site — week 1–2)
- [ ] ...
### Strategic investments (off-site & content — month 1–3+)
- [ ] ...

## Scope & expectations
GEO is compounding, not instant: indexing in days, AI citations over weeks–months.
We sell the work and a measurable visibility trend — never a guaranteed #1 or a
guaranteed AI mention. All data and markup will be real and verifiable.
```

> The same scorecard, re-run monthly, becomes the progress report (see `measurement.md`). Capturing it cleanly now pays off every month after.
