# GEO Audit — CanPay Insights (canpayinsights.ca) — 2026-06-21

> Archetype: **data / tool product.** Its single biggest GEO weapon is original, citable payroll data; its single biggest lever is being **cited off-site**. This audit grades the site against six GEO dimensions, establishes an AI-visibility baseline for six target prompts, and gives an impact-ordered roadmap. All findings are verifiable from the live site or from the searches recorded below.

---

## Executive summary

CanPay Insights is, on the technical side, one of the cleanest small-site GEO builds you will see: it explicitly welcomes every major AI crawler, ships a real `llms.txt`, server-renders answer-first content, and carries rich, layered schema (Organization, WebApplication, **Dataset**, FAQPage, BreadcrumbList, Person) across ~414 indexable URLs. Despite that, it is **effectively invisible in today's AI answers** for all six target prompts — it does not surface in any of the competitive search results that feed AI retrieval, and a brand-name search returns *only its own homepage* while the established, unrelated payroll-software company "CanPay" (canpay.com) owns the namespace around it.

The single biggest opportunity is **off-site**: the site has near-zero independent citations (no Reddit, no "best calculator" listicles, no journalist/data mentions, no Wikidata entity), and its best asset — original 2026 payroll data — is published only as on-page tables, never packaged as a downloadable, attributable dataset that others would cite. Two on-site issues compound the problem: there is **no crawlable Chinese surface at all** (so the Chinese prompt is currently unwinnable), and the high-traffic body content still leads with **2025 figures** (with at least one internal contradiction) even though every target prompt asks about **2026**.

Realistic trajectory: the on-site fixes are days of work and will make the site *eligible and trustworthy*; the off-site citation and original-data work is the part that actually moves AI recommendations, and it compounds over weeks–months with no guaranteed placements.

---

## AI-visibility baseline

For each target prompt: my own best answer (does the brand belong in it?), whether the brand currently surfaces in the retrieval-proxy search, who is recommended instead, and what got cited.

| # | Target prompt | Does CanPay surface? | Who/what is recommended instead (observed) | What got cited |
|---|---------------|----------------------|---------------------------------------------|----------------|
| 1 | best take-home pay / paycheck calculator Canada | **No** | Established, high-authority tools dominate: <cite index="8-1">QuickBooks Canada's free online payroll calculator (2026)</cite>, <cite index="62-1">ADP Canada's after-tax payroll calculator</cite>, <cite index="66-2">PaymentEvolution's (PayEvo) "Canada's most loved" free payroll calculator</cite>, plus talent.com, WOWA, salaryaftertax.com | Vendor/brand homepages; no CanPay mention anywhere |
| 2 | how much is $60,000 after tax in Ontario (2026) | **No** | <cite index="21-1">CareerBeacon: ~$47,385/yr take-home</cite>; <cite index="23-1">talent.com: $43,126/yr</cite>; <cite index="25-2">FilingTaxes: ~$43,126</cite>; <cite index="22-1">aftertaxpay.ca</cite>; <cite index="30-2">takehomecalculator.net's "$60,000 Salary in Ontario… (2026)" page</cite> | CareerBeacon, talent.com, FilingTaxes, aftertaxpay.ca — CanPay's own page ($47,147) absent |
| 3 | 加拿大工资税后怎么算 / 哪个计算器好用 | **No** (and not even eligible) | Chinese-Canadian community tools already rank: <cite index="32-1">aclasssoft advtax (加拿大收入税计算器, lang=zh)</cite>; <cite index="33-1">大温本地网 VanHere</cite>; <cite index="34-1">wpcins.com/zh</cite>; <cite index="37-1">华人网 (Huaren)</cite>; <cite index="38-1">Dealmoon 个税指南</cite> | Chinese community portals; CanPay has **no crawlable Chinese page** to be cited |
| 4 | Canadian salary after tax calculator 2026 | **No** | <cite index="11-1,11-4">salaryaftertax.com/ca (updated June 2026, sources CRA & Revenu Québec)</cite>; <cite index="13-1">salarycalculator.ca by MITEY (all 13 provinces, 2026 rates)</cite>; <cite index="15-1">moneymetrics.ca (CPP+CPP2, updated April 2026)</cite>; <cite index="17-1">WOWA.ca (2024–2026)</cite> | These calculators' own pages, all leading with clean 2026 rates |
| 5 | calculateur de salaire net Québec | **No** (despite having a `/fr/` page) | <cite index="41-1">calculconversion.com (2026)</cite>; <cite index="42-1">talent.com/fr (2026)</cite>; <cite index="43-1">salairequebec.com (2026)</cite>; <cite index="44-2">christophefuret.com (a Montréal broker's calculator)</cite>; <cite index="47-2">maplesalary.com</cite>; <cite index="50-2">SalaireNet.ca</cite> | Dedicated French Québec calculators; CanPay's `/fr/calculateur-salaire-net-quebec` absent |
| 6 | how much CPP / EI will I pay in 2026 | **No** | Accounting firms and dedicated tools with correct 2026 numbers: <cite index="53-1">jwcga.ca (CPP $74,600, CPP2 $85,000, EI $68,900)</cite>; <cite index="51-1">smrcpa.ca ($74,600 YMPE / $85,000 YAMPE)</cite>; <cite index="58-1">eicppcalculator.com (5.95% to $74,600, max $4,230.45)</cite>; <cite index="55-1">catax.tools</cite>; plus Canada.ca (CRA) | CRA pages and accountant/tool blogs with 2026 figures; CanPay's CPP/EI blog (2025 figures) absent |

**Baseline read:** Across all six prompts the brand does **not** appear in the retrieval-proxy results. Prompts 1/4/6 are dominated by household-name brands AI assistants already trust (QuickBooks, ADP, PaymentEvolution, WOWA, CRA). Prompts 3 and 5 are lost to language-native competitors — and for Chinese, CanPay is not even *eligible* because no Chinese URL exists. Prompt 2 is winnable (CanPay's $47,147 is in the same range as CareerBeacon's $47,385) but the page is invisible and its competitors are entrenched.

---

## Scorecard (A–F)

### A. Crawl access & freshness — **mostly strong, freshness weak**
- **OK — robots welcomes AI bots.** `robots.txt` has explicit `Allow: /` blocks for `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `Google-Extended`, `PerplexityBot`, `Perplexity-User`, `ClaudeBot`, `Claude-User`, `anthropic-ai`, `Applebot-Extended`, `CCBot` (only `Disallow: /api/`). Crucially **OAI-SearchBot is allowed**, which is what lets ChatGPT cite the site.
- **OK — sitemap present & clean.** `sitemap.xml` returns 200, valid XML, **414 `<loc>` entries**, all 13 provinces/territories × 27 income levels, with current `lastmod` (`2026-06-21`).
- **OK (strong) — llms.txt present.** `/llms.txt` (200) is a model file: product summary, calculator list, an "Original, citable data articles" section, "Key 2026 facts," and an explicit citation grant ("The data is free to cite — please attribute and link to https://canpayinsights.ca").
- **WEAK — current-year figures.** The target prompts all say **2026**, but the visible body content largely runs on **2025** numbers. The homepage states *"the yearly maximum ($73,200 in 2025), for a maximum employee contribution of about $4,034"* and *"CPP2 — an extra 4% on income between $73,200 and roughly $81,200."* The money pages are titled e.g. *"$60,000 After Tax in Ontario: $47,147 Take-Home (2025/26)."* The CPP blog leads *"In 2025, most workers pay 5.95% CPP on earnings between $3,500 and $71,300"* and footnotes *"Figures use 2025 CRA ceilings."* Meanwhile leading competitors lead clean with 2026: <cite index="53-2">the CPP maximum pensionable earnings increase from $71,300 to $74,600 and EI maximum insurable earnings rise from $65,700 to $68,900 for 2026</cite>.
- **WEAK (accuracy) — internal contradiction.** The homepage says the **2025** YMPE is **$73,200**; the CPP blog says the **2025** YMPE is **$71,300**. The same figure for the same year contradicts itself across pages — and <cite index="53-2">the actual 2025 maximum pensionable earnings was $71,300</cite>, so the homepage value is wrong. For a data product whose entire moat is being a trustworthy numbers source, self-contradiction is a credibility risk.
- **OK — HTTPS & single canonical host.** `http://` → `https://` is a 308; `https://www` → apex is a 308; `<link rel="canonical" href="https://canpayinsights.ca">`; HSTS (`strict-transport-security: max-age=63072000`) is set. One clean canonical host (apex).

### B. Extractability — **strong in English, missing in Chinese**
- **OK — real text in raw HTML.** The interactive calculator is client-rendered (`BAILOUT_TO_CLIENT_SIDE_RENDERING`), but all the *content that matters* is server-rendered: homepage H2 sections, money-page narratives, tables, and FAQ are present in `curl` output and in the clean Jina text (no JS required).
- **OK — answer-first.** `/60000-after-tax-ontario` opens: *"If you earn $60,000 per year in Ontario, your estimated take-home pay is about $47,147 — $3,929 per month or $1,813 every two weeks."* The CPP blog opens with a "Quick Answer" block. This is exactly how to be extractable.
- **OK — question-shaped headings.** e.g. *"How CPP deductions work in 2025/2026," "What affects $60,000 take-home pay in Ontario?," "How much CPP will I pay in 2026?"*
- **OK — tables / lists / FAQs.** Deduction-breakdown tables, pay-frequency tables, cross-province comparison tables, and `FAQPage` schema on the homepage and money pages.
- **OK — one URL per money-topic.** 414 dedicated, indexable URLs (e.g. `/60000-after-tax-ontario`, `/cpp-ei-calculator`); no `#anchor` traps, nothing `noindex`.
- **MISSING — Chinese is not crawlable.** `/zh` and `/zh/...` return **404**, there are **zero `/zh` entries in the sitemap**, and there is **no CJK text in the raw HTML** — yet the schema claims `"inLanguage":["en","fr","zh"]` and the About page advertises "English, French, or Chinese." The Chinese experience exists only as client-side button state, so an AI crawler reading raw HTML sees English only. (French, by contrast, is real: **28 crawlable `/fr/` URLs** in the sitemap with `hrefLang="fr-CA"`, e.g. `/fr/calculateur-salaire-net-quebec`.)

### C. Structured data — **rich, but with mismatches and a hollow Dataset**
- **OK — Organization/Person linked by `@id`.** Homepage carries `Organization` (`@id":"https://canpayinsights.ca/#org"`, `founder` Person "Travis Zhang"), with `WebApplication` referencing `"publisher":{"@id":".../#org"}`.
- **OK — deep schema on key pages.** `/60000-after-tax-ontario` includes `BreadcrumbList`, `Dataset`, `FAQPage`, `WebApplication`, `SoftwareApplication`, `Person`, `WebPage`, `WebSite`, `ImageObject`, `Offer`.
- **WEAK — schema values disagree with visible content.** The homepage `FAQPage` schema uses **2026** figures (*"YMPE, about $74,600 in 2026… YAMPE, about $85,000"*) while the visible homepage body uses **2025** figures (*"$73,200 in 2025… up to roughly $81,200"*). Schema and body should match.
- **WEAK / MISSING — the `Dataset` is hollow.** The homepage declares a `Dataset` ("Canadian Take-Home Pay & Payroll Deductions 2025–2026," CC BY 4.0, `isAccessibleForFree`) — but it has **no `distribution`, `contentUrl`, or `downloadUrl`**, and `/api/` is blocked in robots. There is no actual machine-readable file behind the claim. For a data product, this is the schema equivalent of advertising a store with nothing on the shelves.

### D. Entity & authority — **consistent self-description, but isolated and name-colliding**
- **OK — one consistent entity sentence.** "Free Canadian payroll / take-home pay calculator covering federal tax, provincial tax, CPP/CPP2, EI, and Quebec QPP/QPIP" is repeated near-verbatim across the homepage schema, About page, and `llms.txt`.
- **MISSING — `sameAs` is empty everywhere.** No `Organization` or `Person` `sameAs` on the homepage or About page. No links to LinkedIn, GitHub, Crunchbase, X, or a Wikidata item. The entity has no external corroboration graph.
- **WEAK — name collision with an established brand.** A brand search surfaces *only* CanPay Insights' own homepage; everything else is the unrelated, established **"CanPay" payroll software** company — <cite index="3-1">CanPay's cloud-based payroll service</cite> and <cite index="2-2">"CanPay provides Payroll and HR software for thousands of companies across Canada"</cite>, which also holds <cite index="4-1">a LinkedIn company page</cite> and <cite index="7-1">a YouTube channel</cite>. This older "CanPay" owns the namespace and risks entity conflation in AI systems.
- **WEAK — the named person isn't reinforced.** The founder "Travis Zhang" appears only in JSON-LD; the visible About page says merely *"built and maintained by an independent developer based in Vancouver, British Columbia"* — unnamed, no bio, no credentials, no `sameAs`. The person entity is neither reconciled in visible text nor externally verifiable.

### E. Off-site citation footprint — **near-zero (the weakest dimension and the biggest lever)**
- **MISSING — independent citations/links.** No Reddit threads, blog mentions, news/journalist references, or directory listings for CanPay Insights surfaced in any search. The brand-name and "best calculator / review" searches returned only the site's own homepage plus the unrelated CanPay payroll company.
- **MISSING — "best [category]" listicles.** Absent from every "best Canadian paycheck/salary calculator" result set, which is instead populated by <cite index="8-1">QuickBooks</cite>, <cite index="62-1">ADP</cite>, <cite index="66-2">PaymentEvolution</cite>, talent.com, salaryaftertax.com and WOWA.
- **MISSING — Wikidata / Wikipedia entity.** None found.
- **WEAK (good foundations, unused) — citation enablers exist.** The site already has (a) 2026 original-data studies in `llms.txt` (e.g. `/blog/minimum-wage-take-home-pay-canada-2026`, `/blog/how-much-cpp-will-i-pay-2026`, `/blog/how-much-ei-will-i-pay-2026`), (b) a **CC BY 4.0** license on the Dataset, and (c) a purpose-built `/link-to-canpay` page with ready-made blurbs and an HTML snippet ("Use the snippets below when adding the calculator to a job offer guide, HR resource page, newcomer checklist…"). These are exactly the right hooks — but nobody has used them yet.

### F. Original data & content quality — **genuinely good content, weak E-E-A-T signals**
- **OK — specific, original numbers.** The data blog posts carry real, salary-by-salary tables (e.g. CPP by income: `$40,000 → $2,172 … $90,000+ → $4,341 (maximum)`), marginal-rate explainers, and "when CPP maxes out" detail — not thin AI filler.
- **WEAK — thin/templated pages exist.** `/compare-provinces` is ~562 words and still titled "…2025." The 414 money pages are templated, and near-identical programmatic competitors already rank for the same queries (<cite index="22-1">aftertaxpay.ca</cite>, <cite index="30-2">takehomecalculator.net</cite>), so the format alone is not a differentiator.
- **WEAK — E-E-A-T / first-hand expertise.** No named author byline, credentials, or `sameAs`. Compare the French SERP, where <cite index="44-2">a calculator is fronted by a named Montréal real-estate broker who answers this question for clients daily</cite> — first-hand authority CanPay currently lacks.
- **WEAK — accuracy/consistency** (see Dimension A): the YMPE contradiction and the 2025/2026 blending undercut the trust a data product depends on.

**Group picture:** A is strong except freshness; B is strong in English but has a hole in Chinese; C is impressive but partly cosmetic (hollow Dataset, schema/body mismatch); **D and E are where the site is weak, and E is both the weakest and the highest-leverage**; F is good content sitting on weak authority signals.

---

## What's costing the most (ranked by impact)

1. **Near-zero off-site citation footprint — the brand isn't in the rooms where AI looks.** AI recommendations for "best calculator" queries are assembled from listicles, Reddit, and high-authority finance sites; CanPay appears in none of them, while <cite index="8-1">QuickBooks</cite>, <cite index="62-1">ADP</cite>, <cite index="66-2">PaymentEvolution</cite> and WOWA do. **Fix:** a sustained earned-citation campaign (data-led — see roadmap). This is ~80% of what will actually move the needle.
2. **No crawlable Chinese surface — prompt #3 is unwinnable as built.** `/zh` is 404 and absent from the sitemap, so the site can't be retrieved for Chinese queries even though Chinese-Canadian competitors already rank (<cite index="33-1">大温本地网</cite>, <cite index="37-1">华人网</cite>, <cite index="38-1">Dealmoon</cite>). **Fix:** ship real `/zh/` pages (mirroring the working `/fr/` pattern) with `hreflang`, and seed Chinese-community citations.
3. **The data product's core weapon isn't packaged for citation.** The `Dataset` schema has no downloadable distribution, and `/api/` is blocked. Original payroll data is the one thing a tool like this can offer that AI loves to cite, and right now it's trapped in HTML tables. **Fix:** publish a real, attributable dataset (CSV/JSON) + `DataDownload` + a "methodology" page, under the existing CC BY 4.0 license.
4. **2026 freshness gap + internal contradiction erodes the trust signal for the exact (2026) prompts targeted.** Body content leads with 2025 numbers while competitors lead with correct 2026 figures (<cite index="53-1">CPP $74,600 / CPP2 $85,000 / EI $68,900</cite>; <cite index="58-1">max CPP $4,230.45</cite>), and the homepage's "$73,200 (2025)" contradicts the blog's "$71,300 (2025)." **Fix:** roll all body content to 2026 and reconcile the numbers.
5. **Weak entity/authority graph (empty `sameAs`, unnamed author, name collision, no Wikidata).** Nothing externally anchors the brand or distinguishes it from the older "CanPay" payroll company. **Fix:** add `sameAs`, name and credential the author, and create a Wikidata item.

---

## Roadmap (impact-ordered; off-site & original-data led first)

### Strategic investments — off-site & content (compounds over weeks–months; the real levers)
1. **Turn the 2026 data studies into earned citations.** Pitch the minimum-wage-after-tax-by-province and CPP/EI-by-salary studies (already written) as ready-to-cite data to Canadian personal-finance writers, newsletter authors, and journalists who cover paycheque/CPP changes — the audience already exists (note how accounting firms like <cite index="51-1">smrcpa.ca</cite> and <cite index="53-1">jwcga.ca</cite> publish exactly this and get surfaced). Drive every pitch to `/link-to-canpay`.
2. **Publish a real, downloadable, attributable dataset.** Export the engine's province × income × year tables as CSV/JSON, wire up the `Dataset` `distribution`/`DataDownload`, add a methodology/sources page, and keep the CC BY 4.0 license. This converts the "data product" claim into an asset others can embed and cite — the highest-ceiling move for this archetype.
3. **Seed community answers where these questions are actually asked.** Provide genuinely useful, non-spammy answers (with the calculator as one of several references) in r/PersonalFinanceCanada and r/cantax for the English prompts, and in Chinese communities (大温本地网, 华人网, Dealmoon, 小红书/RedNote) for prompt #3 — these communities already rank for the Chinese query.
4. **Get into the "best calculator" listicles.** Identify the roundup pages AI cites for prompts 1/4 and request inclusion, leading with the differentiators (trilingual, CPP2/QPP/QPIP coverage, transparent methodology, free, no signup).
5. **Build the entity graph.** Create a **Wikidata** item for CanPay Insights (disambiguated from the canpay.com payroll company), and add consistent `sameAs` profiles (LinkedIn, GitHub, App Store listing, Crunchbase). This both raises authority and fixes the name-collision risk.

### Quick wins — on-site (days; make the site eligible, accurate, and complete)
6. **Reconcile the numbers and move body content to 2026.** Fix the YMPE contradiction (use the correct figures: <cite index="53-2">$71,300 for 2025, $74,600 for 2026</cite>), and update the homepage H2 paragraphs, money-page titles ("2025/26" → 2026), and the CPP/EI blog tables to lead with 2026 (CPP2 to $85,000, EI 1.63% / MIE $68,900). Make schema and body agree.
7. **Ship crawlable `/zh/` pages.** Mirror the working `/fr/` model: a Chinese calculator landing page plus Chinese versions of the homepage and top money pages, all in the sitemap with `hreflang` (`zh-Hans` ↔ `en` ↔ `fr-CA`). Add `hreflang` reciprocity to the English money pages (e.g. `/60000-after-tax-ontario` currently has none).
8. **Name and credential the author.** Add a visible byline/bio for the founder on About and key articles, and add `Person` `sameAs` (LinkedIn/GitHub) — turning "an independent developer" into a verifiable expert entity.
9. **Strengthen thin pages.** Expand `/compare-provinces` (currently ~562 words, "2025") with a current 2026 data table and unique analysis so it can stand on its own as a citable comparison.

---

## Scope note

GEO compounds on different clocks: the on-site quick wins (freshness, `/zh` pages, schema fixes, author identity) can be indexed within **days**; the off-site citations and dataset adoption that actually drive AI recommendations accrue over **weeks to months**. AI answers are non-deterministic and personalized, so **no placement or recommendation can be guaranteed** — this work raises the *probability* of being retrieved, cited, and recommended, it does not promise it. Every finding above is verifiable: on-site claims are quoted from the live HTML, `robots.txt`, `sitemap.xml`, `llms.txt`, and JSON-LD as observed on 2026-06-21; competitive/baseline claims are cited to the search results that act as a proxy for the AI retrieval path. Read-only audit — nothing on the site or any third-party platform was modified.
