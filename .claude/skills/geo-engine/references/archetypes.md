# Archetypes — map a brand to its GEO playbook

The archetype set in Phase 0 decides the **priority order** of everything else. Confirm it explicitly with the user, then weight the engagement toward that archetype's top levers. Most brands map cleanly to one; some blend two (e.g. a SaaS with a free data tool — run both).

## Quick selector

| Archetype | You're it if… | Top 2–3 levers | Schema focus |
| --- | --- | --- | --- |
| **Service / local business** | You sell a service, often tied to a place (photographer, lawyer, clinic, agency, trades) | Service+location pages · entity consistency (GBP, sameAs) · reviews & local citations | ProfessionalService/LocalBusiness, Service, FAQPage, Person |
| **Data / tool product** | You offer a free tool, calculator, dataset, or API | **Original-data assets** → Reddit answers + journalist/listicle outreach · Dataset schema | Dataset, Organization, WebApplication, FAQPage |
| **SaaS / B2B** | You sell software/subscriptions to businesses | Comparison & "alternatives" pages · listicle inclusion · community presence (Reddit/HN/Slack) · docs | Organization, SoftwareApplication, FAQPage, Article |
| **Ecommerce / product** | You sell physical/digital products | "Best X" listicles · marketplace & review-site presence · Product/Review schema | Product, Offer, Review, Organization |
| **Publisher / content** | You're a media/content site monetizing attention | Answer-first articles with original reporting/data · author E-E-A-T · broad citation footprint | Article, Person (author), Organization |

## How the levers shift by archetype

- **Service/local:** AI recommends *consistent, well-described local entities*. The win is one URL per service×location, airtight entity consistency across the web (site + Google Business Profile + LinkedIn + directories all agreeing), and real reviews. Off-site = local citations + "best [service] in [city]" lists + niche community mentions.
- **Data/tool:** AI cites *specific numbers*. The win is publishing original, citable data (the thing nobody else has), then getting it quoted on Reddit, in journalist coverage, and in listicles. Your data is simultaneously your on-page content AND your outreach bait. This archetype has the highest off-site ceiling.
- **SaaS/B2B:** buyers ask AI "best tool for X" / "X vs Y" / "X alternatives". The win is owning comparison/alternatives pages on your own site *and* being present in third-party listicles, Reddit/HN threads, and review platforms (G2/Capterra) — those are what the LLM reads.
- **Ecommerce:** AI shopping answers lean on review aggregators, marketplaces, and "best of" roundups far more than on the brand's own site. Win the off-site review/listicle footprint first; Product/Review schema second.
- **Publisher:** you ARE the content. Win by being the most extractable, original, author-credentialed answer on your topics, cited widely enough to enter training data.

---

# Case study 1 — traviszhang.com (service / local business)

The build the on-site method was hardened on. Use as a worked example and as sales proof.

**Client:** Travis Zhang (Qi Zhang) — Vancouver architectural, interior & hospitality photographer. Goal: be the name AI gives when someone asks "who's a good architectural photographer in Vancouver?" and get hired by Vancouver designers/architects.

**Before (the typical GEO failure state):**
- A beautiful **one-page** portfolio — but galleries/projects rendered by **JavaScript**, so invisible to AI crawlers.
- Homepage stats were JS counters that read **"0"** in raw HTML.
- Everything behind `#anchors` → no per-topic URLs to cite.
- `/contact` 404'd; old Adobe Portfolio URLs lingering; mixed www/apex signals.
- LinkedIn headline said "Machine Operator & AI Developer" — the entity was *fighting* the brand.

**What was done (on-site + entity):**
- **On-page:** keyword title; a visually-hidden real H1; fixed "0"→real numbers (21 yrs / 200+ projects / 33 countries) in static text; unified canonical to the apex.
- **Structured data:** `ProfessionalService` + `Person` (with `alternateName: "Qi Zhang"`) + per-page `Service` + `FAQPage` + `BreadcrumbList`.
- **Architecture:** 4 real static service pages (`/architectural-`, `/interior-`, `/hospitality-`, `/commercial-photography-vancouver`) + a real `/contact`, reusing existing CSS — **design unchanged**. Homepage cards became internal links.
- **Crawlability:** robots.txt explicitly welcoming OAI-SearchBot/GPTBot/PerplexityBot/ClaudeBot/etc.; full sitemap; `llms.txt`.
- **Identity:** `sameAs` (IG + X + LinkedIn) with correct URLs; LinkedIn headline/About/role reframed to "photographer".
- **Submit:** GSC verified + sitemap + request-indexing; IndexNow ping (202); Google Business Profile created.

**Result shape:** "one long image poster" → a multi-page, AI-readable authority site with one consistent entity.

**Lessons baked into the skill:**
1. JS-only content is the silent GEO killer — author citable pages as **static HTML**.
2. The "0 stats" trap — counters need real text fallbacks.
3. Don't redesign — **add** pages + invisible signals.
4. Entity consistency (especially LinkedIn) matters as much as on-site work.
5. You can't log into the client's Google — but you CAN do IndexNow + host verification files + give exact click steps.

---

# Case study 2 — CanPay Insights (data / tool product)

The build the off-site / original-data method came from. Different archetype, different top lever.

**Brand:** CanPay Insights (canpayinsights.ca) — free Canadian payroll / take-home-pay calculator, from a transparent rules engine, in EN/FR/ZH. Goal: be cited when someone asks ChatGPT/Perplexity "how much is 60k after tax in Ontario?" or "best Canadian salary calculator".

**The core insight:** a calculator can compute **original data nobody else has published** — e.g. take-home pay for minimum wage across all 13 provinces/territories. That data is *both* the on-page content *and* the outreach hook. This is the data/tool archetype's superpower.

**What was done:**
- **On-site technical:** robots welcoming AI crawlers; `llms.txt` with the brand's one-liner, key 2026 facts, and citable-data links; `Organization` + `Dataset` schema (Dataset declared with a **CC-BY license** = an explicit "you may cite this").
- **Content discipline:** pruned **52 → 20** pages — deleted ~32 generic "salary guide" / generic-tips pages with no unique data, because thin AI-spun content gets ignored by LLMs and flagged low-value by Google. Kept the pages with original numbers.
- **Original-data assets:** "minimum-wage take-home, all 13 provinces 2026", "how much CPP/EI will I pay 2026 (by salary)", "CPP2 explained", province comparisons — each with a quotable headline stat (e.g. "Nunavut worker keeps $34,098 vs Alberta $26,478 — a $7,620 gap").
- **Off-site (the real lever):** Reddit answers in r/PersonalFinanceCanada using the brand's real numbers (value-first, link as source only), journalist outreach via Featured/Qwoted leading with the data, resource-page/listicle inclusion, and a French-Québec angle competitors ignore.
- **Early signal:** ChatGPT Search began sending referral traffic — proof the retrieval path was working before the off-site program had even matured.

**Lessons baked into the skill:**
1. **Original data is the #1 weapon** for this archetype — it's content and outreach bait in one.
2. **Fewer, denser pages win.** Pruning thin content is real GEO work, not destruction.
3. **Off-site citations (esp. Reddit) are ~80% of the game** — the on-site work just makes you eligible.
4. **Declare a license** (Dataset + CC-BY) to lower the friction of being cited.
5. A brand-new, low-authority domain *can* start getting cited by AI within weeks if the data is genuinely original and the off-site work is real.
