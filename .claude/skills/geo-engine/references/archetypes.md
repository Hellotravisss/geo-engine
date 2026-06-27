# Phase 0 — Archetypes: map a brand to its GEO playbook

The archetype set in Phase 0 decides the **priority order** of everything else. Confirm it explicitly with the user, then weight the engagement toward that archetype's top levers. Most brands map cleanly to one; some blend two (e.g. a SaaS with a free data tool — run both).

## Quick selector

| Archetype | You're it if… | Top 2–3 levers | Schema focus |
| --- | --- | --- | --- |
| **Service / local business** | You sell a service, often tied to a place (photographer, lawyer, clinic, agency, trades) | Service+location pages · entity consistency (GBP, sameAs) · reviews & local citations | ProfessionalService/LocalBusiness, Service, FAQPage, Person |
| **Data / tool product** | You offer a free tool, calculator, dataset, or API | **Original-data assets** → Reddit answers + journalist/listicle outreach · Dataset schema | Dataset, Organization, WebApplication, FAQPage |
| **SaaS / B2B** | You sell software/subscriptions to businesses | Comparison & "alternatives" pages · listicle inclusion · community presence (Reddit/HN/Slack) · docs | Organization, SoftwareApplication, FAQPage, Article |
| **Ecommerce / product** | You sell physical/digital products | "Best X" listicles · marketplace & review-site presence · Product/Review schema | Product, Offer, Review, Organization |
| **Publisher / content** | You're a media/content site monetizing attention | Answer-first articles with original reporting/data · author E-E-A-T · broad citation footprint | Article, Person (author), Organization |
| **Directory / aggregator** | You aggregate *others'* entities — a listings site, marketplace, or "best of" hub | Be the canonical cited list: comprehensive / fresh / deduped coverage · per-listing structure · get the directory *itself* cited & into "best directories" lists | CollectionPage, ItemList, Dataset, Organization |
| **Personal brand / entity** | You ARE the product — a person or brand name with **no website, or a thin one that isn't the lever** (founder, expert, KOL, local doctor/lawyer/photographer, a product/brand name with little owned web presence) | **Clean knowledge-graph entity** (Wikidata + 百度百科) · consistent name/bio/headshot across every profile with `sameAs` · earned third-party mentions (interviews, bylines, podcasts, "top-X" listicles, awards) | Person *or* Organization/Brand, ProfilePage; entity-IDs over site schema |

## How the levers shift by archetype

- **Service/local:** AI recommends *consistent, well-described local entities*. The win is one URL per service×location, airtight entity consistency across the web (site + Google Business Profile + LinkedIn + directories all agreeing), and real reviews. Off-site = local citations + "best [service] in [city]" lists + niche community mentions.
- **Data/tool:** AI cites *specific numbers*. The win is publishing original, citable data (the thing nobody else has), then getting it quoted on Reddit, in journalist coverage, and in listicles. Your data is simultaneously your on-page content AND your outreach bait. This archetype has the highest off-site ceiling.
- **SaaS/B2B:** buyers ask AI "best tool for X" / "X vs Y" / "X alternatives". The win is owning comparison/alternatives pages on your own site *and* being present in third-party listicles, Reddit/HN threads, and review platforms (G2/Capterra) — those are what the LLM reads.
- **Ecommerce:** AI shopping answers lean on review aggregators, marketplaces, and "best of" roundups far more than on the brand's own site. Win the off-site review/listicle footprint first; Product/Review schema second.
- **Publisher:** you ARE the content. Win by being the most extractable, original, author-credentialed answer on your topics, cited widely enough to enter training data.
- **Directory/aggregator:** AI loves to cite one comprehensive, well-structured list for "best/top/list of X" questions. The win is being *the* canonical — most complete, freshest, deduplicated — list in your niche, marked up with `ItemList`/`CollectionPage` so engines parse every entry, and itself cited in "best [category] directories" roundups. **Disambiguation:** a brand that aggregates *others'* entities is a directory **first**, even if it's also local — don't mis-route it to service/local; its lever is coverage + being cited, not its own reviews/GBP.
- **Personal brand / entity:** there is *no site to optimize* — the **entity is the product**. AI recommends an entity it can resolve cleanly (one consistent person/brand across the knowledge graph and every profile) and that authoritative third parties keep mentioning. The win is a clean Wikidata (+ 百度百科) item plus airtight name/bio/role consistency everywhere, then a steady stream of earned mentions (interviews, bylines, podcasts, "top-X" listicles, awards, association directories). On-site work is near-irrelevant; **link rate is near-zero by design** — weight *mention rate* and *entity correctness* instead. See the detailed section below.

---

# Personal brand / entity — when there's no website to optimize

The rest of this skill assumes an owned site you can edit. This archetype is the case where **the client is a person or a brand name, not a website** — a founder, expert, KOL, local professional (doctor, lawyer, photographer), or a product/brand with little or no owned web presence. The whole method shifts: you can't restructure pages or ship schema on a site you don't have. **The entity itself is the surface you optimize.**

> Core thesis, restated for this case: *off-site footprint is still the dominant lever — but the on-site half of the playbook is replaced by **building and cleaning the entity** so engines can resolve "who/what is this" with confidence.* An entity AI can't resolve cleanly never gets recommended, no matter how many mentions it has.

## The three levers (in priority order)

**1. Build & clean a knowledge-graph entity** 🔑 *(strong)* — the closest thing this archetype has to "on-site", and the foundation everything else points at.
- **Wikidata item** (+ **百度百科** for CN). Set **`P31` instance-of** (human / business / brand), **`P856` official website** *if any*, and **external-ID properties** (LinkedIn, Crunchbase, GitHub, ORCID, IMDb, app-store IDs) as `sameAs` anchors — **every statement referenced** to an independent source. ⚠️ Bare promotional items with no independent sources get flagged and deleted — only create one you can reference.
- **Profile consistency across every surface** — identical **name, one-line bio, headshot, and role/title** on LinkedIn, Crunchbase, GitHub, app stores, professional directories, association pages, social profiles. Cross-link them (`sameAs`/profile links) so they reinforce one entity instead of splitting it. A photographer listed as "Machine Operator" on LinkedIn is an entity fighting its own brand (see Case study 1).
- This is where the discipline from `onsite-sop.md`'s "entity sentence" applies — write one canonical entity sentence and use it **verbatim** everywhere.

**2. Earn authoritative third-party mentions** 🔑 *(strong)* — the dominant lever, same as every archetype, but here it carries even more weight because there's no owned content to fall back on. The kinds AI engines actually cite:
- Interviews, guest bylines / op-eds, podcast appearances, "best/top {role/topic}" listicles, awards, and **inclusion in association / professional directories**.
- Run **Front 1 (community)** and **Front 2 (original-data / editorial outreach)** from `offsite-sop.md` exactly as written — value-first, one-at-a-time, never fabricated. The person's own expertise (a quotable take, a real credential, original analysis) is the bait in place of a data asset.

**3. Platform content for CN / bilingual** *(strong, when relevant)* — per `references/i18n.md`: 小红书 笔记 / 知乎 answers / B站 视频 / 公众号 文章 that the domestic engines retrieve, plus **百度百科** as the entity anchor and **高德 / 百度地图** business listing for local people (doctor, lawyer, photographer). Same value-first rules, different venues.

## The anchor problem (this archetype's defining move)

With no owned site, the entity has **no surface you control to verify itself** — every profile is on someone else's platform. So **designate ONE controllable anchor** as the self-citation hub: a single landing page (even a one-pager / link-in-bio) **or**, if there's truly no site, the **LinkedIn** profile **or** the **百度百科** entry. Point every other profile's `sameAs`/link at it, and use it as `P856` on Wikidata. The anchor is what lets engines (and Wikidata reviewers) tie the scattered profiles into one resolvable entity. One anchor, consistent everywhere — not five half-maintained ones.

## Target questions (the Phase-0 prompt set for a person)

- **best / top {role} in {place}** — "best architectural photographer in Vancouver", "top startup lawyer in SF".
- **who is the expert on {topic}** — "who should I follow on {niche}", "leading voice in {field}".
- **branded-name disambiguation** — "who is {Name}", "is {Name} the {role}" — especially when the name is common or collides with others. Getting the engine to return *your* person for the name is half the battle.

## Measurement (it still applies — just re-weighted)

Same machinery as `measurement.md` (mention rate / SOV / link rate per engine, fixed prompt set, monthly cadence) — but **link rate may be near-zero by design** (no site to link). Don't read that as failure. **Weight mention rate and entity correctness instead**: is the engine returning *this* person/brand for the name and the "best {role}" prompts, with accurate bio/role/affiliation? Entity correctness (right person, right facts, no confusion with a namesake) is a first-class KPI here, not link rate.

## Red lines (reinforced for this archetype)

- ❌ **No fabricated credentials, awards, or reviews.** A person's authority is the whole asset — one invented credential that gets caught burns it permanently, and editors/engines increasingly catch it.
- ❌ **No buying or spamming engagement** to manufacture mentions.
- ⛔ **Recognition is not recommendation.** A grey-hat tactic in the CN market: paying crowds to open 豆包 and query a brand/person so the engine "sees" the name a lot. **This is NOT the method.** It manufactures *recognition*, not *recommendation* — it's gameable, leaves no durable citation, and the engines discount coordinated query patterns the same way Google discounts link schemes. The durable play is **earned citations + a clean entity** — those survive the next model update; faked query volume doesn't.

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
3. **Off-site citations (esp. Reddit) are the dominant lever** — the on-site work just makes you eligible.
4. **Declare a license** (Dataset + CC-BY) to lower the friction of being cited.
5. A brand-new, low-authority domain *can* start getting cited by AI within weeks if the data is genuinely original and the off-site work is real.
