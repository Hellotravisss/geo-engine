# Phase 2 — On-site implementation

On-site work makes the brand **eligible and extractable**. It rarely wins the recommendation alone (that's Phase 3), but skipping it caps everything else. Do the work in the repo, reuse the existing design, and verify with the bot-view commands after every change.

Grounding truth to tell the client: **GEO is still SEO.** A page must be crawlable, render real text, be genuinely useful, and describe a clear entity — *then* AI can surface it. Five pillars: crawlable · entity · useful first-hand content · structured data · cited elsewhere. If a change doesn't move one of these, cut it.

## Hard rules (trust is the product)
- **No fabrication.** Never invent clients, projects, reviews, ratings, prices, or credentials. Structured data must match visible, true page content — Google demotes fake/markup-only data. If unsure, leave it out.
- **Real numbers in static text.** Put true stats in the HTML text node, not only in JS counters.
- **Don't break the design.** Add pages and invisible signals; reuse existing CSS. Don't redesign what works.
- **One entity sentence**, used verbatim everywhere.

---

## 1. Crawl access — robots.txt (welcome the AI bots)

Default-allow and name the AI crawlers explicitly so there's no ambiguity; always link the sitemap.

```
User-agent: *
Allow: /

# Search crawlers (AI Overviews & ChatGPT/Perplexity search rely on these)
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /

# AI answer engines
User-agent: OAI-SearchBot      # ChatGPT Search — drives ChatGPT citations
Allow: /
User-agent: ChatGPT-User       # ChatGPT browsing on a user's behalf
Allow: /
User-agent: GPTBot             # OpenAI crawler (training/index)
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot   # Claude web search — drives Claude citations
Allow: /
User-agent: Claude-User        # Claude browsing on a user's behalf
Allow: /
User-agent: Google-Extended    # Gemini/Vertex training opt-in (does NOT affect Search/AI Overviews)
Allow: /
User-agent: Applebot
Allow: /
User-agent: Applebot-Extended  # Apple Intelligence
Allow: /
User-agent: CCBot              # Common Crawl — feeds many models' training data
Allow: /

Sitemap: https://EXAMPLE.com/sitemap.xml
```

> This is the **canonical, complete bot list** for the whole skill — other files point here rather than re-listing (lists churn; keep one source). The AI-bot roster changes often; re-check against a maintained list (e.g. the official OpenAI/Anthropic/Perplexity crawler docs) when you run an engagement.

- **Critical nuance:** blocking `GPTBot` only stops *training* use; **`OAI-SearchBot` is what lets ChatGPT Search cite you** — keep it allowed if you want AI citations. Same logic: `Googlebot`/`Bingbot` power AI Overviews and Copilot, so don't block them in the name of "AI opt-out". `Google-Extended` governs only Gemini *training*, not AI Overviews crawling.
- **Training-bot tradeoff (an informed choice, not a default):** allowing `GPTBot`/`CCBot`/`Google-Extended` feeds the slow *memory* path (good for long-term recall) but gives content to model training. For most brands seeking visibility, allow them. If the client has IP concerns, you can allow the *search* bots (OAI-SearchBot, Googlebot, PerplexityBot, ClaudeBot) while disallowing the *training* bots — explain the trade.
- **⚠️ Check your own auth gate first — it outranks the CDN as a cause.** On any app-framework site (Next.js middleware, Rails/Django auth, Vercel/Netlify password protection, a "coming soon" gate), the login gate often matches `/*` and **307s `/robots.txt`, `/sitemap.xml` and `/llms.txt` to `/login`**. Every AI crawler is then told "sign in" instead of being told what it may read, and the site is invisible while the repo looks perfect. Explicitly allowlist those paths in the gate, then verify with the curl block below — a `307`/`302` on any of them is the bug. Check this *before* blaming the CDN: it is the same silent failure, one layer earlier, and it is entirely inside code you control.
- **⚠️ Verify on the LIVE site, not just the repo file — this is the #1 silent failure.** Many hosts/CDNs **override or inject** robots.txt: Cloudflare's *AI Crawl Control / "Managed robots.txt"* and "Block AI bots" toggle, or Vercel/Netlify/Webflow settings, or a WAF user-agent rule, can serve a *different* robots — or block AI bots at the edge — no matter what you deployed. **Fetch the live robots AS an AI bot** and confirm it matches what you shipped:
  ```bash
  for ua in "OAI-SearchBot" "GPTBot" "ClaudeBot" "PerplexityBot"; do
    echo "== $ua =="; curl -sA "$ua" "https://EXAMPLE.com/robots.txt" | head -40
  done
  curl -sA "OAI-SearchBot" -o /dev/null -w "key page as AI bot -> %{http_code}\n" "https://EXAMPLE.com/"
  ```
  If the AI-UA response differs from your file (an extra `Disallow: /`, a `Content-Signal: ai-train=no`, or a 403), the block is at the **CDN/host** — fix it in *that dashboard* (e.g. Cloudflare → AI Crawl Control → turn off Managed robots / Block AI bots), not in the repo. (This is exactly the failure mode where a perfect repo robots.txt is silently overridden at the edge.) Google Search Console → URL Inspection is a solid first-party render check.

## 2. sitemap.xml
List every real page with the **canonical host**. No redirects/404s inside. Update when you add pages. Reference it in robots.txt.

## 3. llms.txt — the machine-readable front door
A markdown file at `/llms.txt`. Cheap and harmless; don't oversell it (no major engine has confirmed ranking use). Spec: github.com/AnswerDotAI/llms-txt. Lead with the entity sentence — it's the line most likely to be quoted. Two proven shapes:

**Service / local business:**
```markdown
# NAME — ROLE in CITY

> ENTITY SENTENCE (who, what, where) + 1–2 proof points (certifications, publications,
> years/scale). One tight paragraph an LLM can quote directly. Contact: info@EXAMPLE.com.

## Services
- [Service 1 in CITY](https://EXAMPLE.com/service-1-city): one-line description.
- [Service 2 in CITY](https://EXAMPLE.com/service-2-city): one-line description.

## About & Contact
- [Selected projects](https://EXAMPLE.com/#work): what the portfolio shows.
- [About NAME](https://EXAMPLE.com/about): background, credentials, recognition.
- [Contact](https://EXAMPLE.com/contact): info@EXAMPLE.com
```

**Data / tool product** (lead with what's citable):
```markdown
# BRAND

> One-paragraph: what the tool does, coverage, languages, and that the data is free to
> cite — please attribute and link to https://EXAMPLE.com.

## Tools
- [Primary tool](https://EXAMPLE.com/): what it computes.

## Original, citable data
- [Headline data article](https://EXAMPLE.com/blog/...): the quotable finding.

## Key facts
- [Current-year fact 1 with a real number.]
- [Current-year fact 2 with a real number.]

## About
- [About](https://EXAMPLE.com/about) — [Contact](https://EXAMPLE.com/contact): info@EXAMPLE.com
```
Link only real, live pages. Update llms.txt whenever you add pages.

## 4. On-page fundamentals (small edits, big impact)

- **`<title>`** — `Primary Keyword + Place | Brand`, <~60 chars, unique per page.
- **Meta description** — ~150–160 chars, keyword + place + who it's for. AI may quote it.
- **Exactly one H1** carrying the core keyword. If the visible hero is a poetic line you don't want to change, keep the design with a visually-hidden real H1 — **but it must restate genuine visible content, never inject keywords that appear nowhere else on the page (that's cloaking, and it gets penalized):**
  ```html
  <h1 class="sr-only">Vancouver Architectural & Interior Photographer — Brand</h1>
  ```
  ```css
  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;}
  ```
- **Headings** read like the questions people ask AI ("How an interior shoot works", "What's included", "How much does X cost?"). Keyword in intro + ≥2 H2s, never stuffed.
- **Image alt text** describes the real subject + context, not "image 01".
- **Canonical & host** — collapse every duplicate that splits the entity: force **ONE host** (apex *or* www), **ONE scheme** (https), and **ONE trailing-slash** convention; all other variants `301`/`308` to the canonical. Set `<link rel="canonical">`, `og:url`, sitemap, and internal links to it. Verify: `for u in http://EXAMPLE.com https://www.EXAMPLE.com https://EXAMPLE.com/page; do curl -sI "$u" | grep -iE "^HTTP|^location"; done` — each non-canonical variant should redirect, not return 200.
- **Multi-locale (only if genuinely multilingual)** — one URL per locale; reciprocal `hreflang` between them **including `x-default`**; a **self-referential canonical per locale** (never canonicalize `/fr` → `/en`); translate the facts, don't contradict them across locales.

## 5. The two silent killers (check on every site)

- **JS-only content.** Galleries/copy injected by JavaScript can be invisible to AI. **Escape hatch:** don't rely on the JS app for GEO — author the citable pages as **plain static HTML** (fully crawlable) with the real text in source. The fancy JS homepage can stay.
- **The "0 stats" trap.** Animated counters often render `0` to non-JS crawlers. Put the true value in the text node and let JS animate over it:
  ```html
  <span class="num" data-count="21">21</span>   <!-- not >0< -->
  ```

## 6. Answer-first content structure (what makes you quotable)

Every key page and article should:
- **Give the answer in the first sentence** — lead with the number/conclusion, then explain. ("A $60,000 salary in Ontario takes home **$47,147** in 2026 — here's the breakdown…")
- Use **question-shaped H2/H3** matching how people ask AI.
- Put data in **tables / lists / FAQs** (LLMs lift clean Q&A and tables readily).
- Include **specific, original numbers** with sources — this is the single biggest content lever (Princeton GEO study: cite/quote/stat-rich content is cited markedly more).
- **Internal-link** to related pages and the core tool/CTA.

## 7. Site architecture — one URL per money-topic

AI associates a *question* with a *URL*. A single-page site gives nothing specific to cite.
- One clean URL per high-value service/topic (`/interior-photography-vancouver`).
- Static, crawlable HTML; reuse existing CSS/nav/footer.
- Internal links everywhere with descriptive anchors (home → topic, topic ↔ topic, → contact). Turn existing homepage cards into real `<a href>` links without changing the look.
- **Don't over-fragment:** 4–6 strong pages beat 15 thin ones.
- Service-business skeleton: `/` · `/<service>-<city>` ×4 · `/projects/<name>` (case studies — the strongest asset) · `/about` · `/journal/<slug>` · `/contact`.

## 8. Content to build (and what to prune)

**Build:**
1. **Money/topic pages** — answer the transactional question; who-it's-for / what's-included / true ranges / 3–6 FAQs / CTA.
2. **Original-data assets** — the thing nobody else has (for data/tool brands this is #1; for service brands it's case studies + cost/process articles with real numbers). Each doubles as outreach bait (Phase 3).
3. **Case studies** — one page per real project; needs real client info, never fabricated.

**Prune:** thin, AI-spun "X guide"/generic-tips pages with no unique data. They get ignored by AI and flagged low-value by Google (and ad networks). CanPay cut 52→20 and improved. Fewer, denser, data-backed pages win.

## 9. Submit & index your own pages

Getting indexed fast is on-site work (earning third-party citations is Phase 3).
- **Google Search Console** — verify (HTML-file or DNS; you can host the verification file for the client), submit `sitemap.xml`, `URL Inspection → Request indexing` for key pages.
- **Bing Webmaster Tools** — add the site, verify, submit `sitemap.xml`. ⚠️ **Treat this as a
  top-priority step, not a Bing-traffic afterthought:** ChatGPT Search retrieves from Bing's index
  (confirmed by OpenAI at launch; third-party analysis of 500+ ChatGPT citations found ~87% matched
  Bing's top organic results for the same query). Copilot rides the same index.
  **Being in Bing is necessary but not sufficient** — ChatGPT still fetches the page with
  `OAI-SearchBot`, so a site that ranks on Bing while blocking that agent stays invisible in ChatGPT.
  Check both, always: index membership AND crawler access (§1).
  BWT can import verified properties straight from Google Search Console — do GSC first and this
  takes about a minute.
- **IndexNow** (instant ping to Bing & others — no client login needed). Two portability traps,
  both hit for real on 2026-08-10 while wiring this up for avowd.ai:
  · **The key file must be publicly fetchable.** If the site has an auth gate, its allow-list needs
    the key file by name, or verification fetches a login redirect — and the ping still returns
    202, so the failure is completely silent.
  · **Do not strip the sitemap tags with `sed 's|</\?loc>||g'`** — `\?` is a GNU extension that
    BSD sed (macOS) ignores, so `<loc>` survives into the payload and IndexNow answers 400.
    Strip in the JSON-building step instead. (Working script: `GEO/dashboard/scripts/indexnow.sh`.)
  ```bash
  KEY=$(uuidgen | tr 'A-Z' 'a-z' | tr -d '-')
  printf "%s" "$KEY" > site/$KEY.txt           # host the key file, then deploy
  curl -s -X POST "https://api.indexnow.org/indexnow" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "{\"host\":\"EXAMPLE.com\",\"key\":\"$KEY\",
         \"keyLocation\":\"https://EXAMPLE.com/$KEY.txt\",
         \"urlList\":[\"https://EXAMPLE.com/\",\"https://EXAMPLE.com/page-1\"]}"
  # 200/202 = accepted
  ```
- **Host quirk:** many static hosts 308-redirect `/page.html` → `/page`. Link the clean URL and confirm it returns **200 directly** (some verifiers don't follow redirects).

## 9b. Google preferred sources — worth adding, and worth explaining honestly

Google lets a searcher nominate sites they want more of. Those sites then carry a **"preferred" badge** for that person in **Top Stories, AI Overviews and AI Mode** — the last two make it a GEO surface, not just a news one. Confirmed by Google 2026-08-20; English-global from Dec 2025, all languages from 2026-04-30.

**⚠️ It is NOT a ranking signal, and you will be asked otherwise.** A widely-shared video read *Search Engine Journal*'s headline ("now a global SEO signal") as "global ranking weight." "Global" there means **geographically available everywhere**. The mechanism is **personalized**: it changes what an opted-in reader sees, and nothing about what anyone else sees. Selling it as a ranking factor is a debt that comes due — say plainly what it does and does not do, on the page itself if you can.

**Eligibility is wider than people assume:** domain and subdomain level sites only (no subdirectories), and **no Google News membership or news-publisher status is required**.

**Two ways to install it — prefer the second:**

```html
<!-- Google's official embed: pulls a third-party script onto every page carrying it -->
<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
<div google-add-preferred-source-btn></div>
```

```
Documented deeplink — same result, no script, your own styling:
https://www.google.com/preferences/source?q=EXAMPLE.com
```

Use the deeplink unless the client specifically wants Google's chip. The embed costs a render-blocking third-party request and an extra tracking surface charged to the visitor, and drops Google's branding into the client's design system. Draw the button yourself.

**Set expectations before building it.** Value scales with existing audience — it converts loyal readers into durable visibility, it does not acquire readers. On a site nobody visits yet, nobody clicks it. **The right moment to install is immediately before a traffic event** (a launch, a campaign, a press hit), never after — the visitors who arrive during the spike are the only ones who can opt in, and they only come once. Put it where recurring content lives (a notes/blog/updates index), because "show me more of this source" only means something next to something that recurs.

## 10. Render check after deploy (always)
```bash
curl -sA "Mozilla/5.0" https://EXAMPLE.com/<page> | grep -i "<h1\|key phrase"
curl -s "https://r.jina.ai/https://EXAMPLE.com/<page>" | head -60   # what a bot reads
```
Confirm the real text and schema are present in fetched HTML. JSON-LD blocks live in `schema-library.md`.

---

## Entity consistency (cross-cutting — do it here, verify off-site in Phase 3)

AI builds confidence in "who you are" from **agreement across sources**. One inconsistency and the model hedges — and the consistent competitor gets the recommendation.

- **The entity sentence:** `<Name> is a <city>-based <role> working with <audience> across <region>.` The single most important entity signal. Write it once, reuse verbatim on the site, in schema, and on every profile.
- **Put the same name + role + URL on:** website (visible + `Person.sameAs`), LinkedIn (**Headline + About + current position + Industry** — set the real role, keep side jobs in history, don't let them define the headline), Instagram/X (display name + bio + link), Google Business Profile, every directory/press bio/podcast blurb.
- **`sameAs`** lists the real, current, resolving profile URLs (a wrong LinkedIn vanity URL points the entity at nothing). **Skip profiles that contradict the brand** — they add noise, not authority.
- **Two-name people:** `"name":"Travis Zhang","alternateName":"Qi Zhang"` so AI knows it's one entity.
- **Conflicting-identity fix:** if a profile describes a different job that fights the brand, reframe the headline to lead with the target role (turn off "share profile updates" before editing so you don't spam connections).
