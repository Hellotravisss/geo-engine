# Phase 2 — Schema library: copy-paste JSON-LD

Machine-readable facts about the entity. **Only mark up what's visibly true on the page.** Google demotes fake/markup-only data, and false markup poisons the trust the whole strategy depends on. Replace `EXAMPLE.com`, names, handles. Use stable `@id` URLs so nodes reference each other (`worksFor`, `provider`, `founder`, `about`). Validate every page at **validator.schema.org** and **search.google.com/test/rich-results**.

## Which schema per archetype

| Archetype | Homepage | Key pages |
| --- | --- | --- |
| Service / local | `ProfessionalService`/`LocalBusiness` + `Person` | `Service` + `FAQPage` + `BreadcrumbList`; `ContactPage`; `CreativeWork`/`ImageObject` for projects |
| Data / tool | `Organization` + `WebApplication` | `Dataset` (+ license) + `FAQPage`; `Article` for data posts |
| SaaS / B2B | `Organization` + `SoftwareApplication` | `FAQPage`; `Article`; comparison pages |
| Ecommerce | `Organization` | `Product` + `Offer` + `Review`/`AggregateRating` (only if real) |
| Publisher | `Organization` | `Article` + `Person` (author) + `BreadcrumbList` |
| Directory / aggregator | `Organization` + `CollectionPage` | `CollectionPage` + `ItemList` (the listings) + `Dataset` (if you publish the data); per-item `LocalBusiness`/`Product`/`Organization` |

---

## Service / local business — homepage (Person + ProfessionalService)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://EXAMPLE.com/#business",
  "name": "BRAND — SERVICE",
  "image": "https://EXAMPLE.com/og.jpg",
  "url": "https://EXAMPLE.com/",
  "email": "info@EXAMPLE.com",
  "description": "ENTITY SENTENCE.",
  "address": { "@type": "PostalAddress", "addressLocality": "CITY", "addressRegion": "REGION", "addressCountry": "CC" },
  "areaServed": [ { "@type": "City", "name": "CITY" }, { "@type": "AdministrativeArea", "name": "REGION" } ],
  "sameAs": [ "https://instagram.com/HANDLE", "https://x.com/HANDLE", "https://www.linkedin.com/in/VANITY" ],
  "founder": { "@type": "Person", "@id": "https://EXAMPLE.com/#person" },
  "knowsAbout": [ "Topic 1", "Topic 2", "Topic 3" ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://EXAMPLE.com/#person",
  "name": "FULL NAME",
  "alternateName": "OTHER NAME",
  "url": "https://EXAMPLE.com/",
  "image": "https://EXAMPLE.com/og.jpg",
  "jobTitle": "ROLE",
  "description": "ENTITY SENTENCE.",
  "email": "info@EXAMPLE.com",
  "homeLocation": { "@type": "City", "name": "CITY" },
  "worksFor": { "@id": "https://EXAMPLE.com/#business" },
  "sameAs": [ "https://instagram.com/HANDLE", "https://x.com/HANDLE", "https://www.linkedin.com/in/VANITY" ],
  "knowsAbout": [ "Topic 1", "Topic 2", "Topic 3", "Topic 4" ]
}
</script>
```

## Service / local business — per page (Service + FAQPage + Breadcrumb)
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"Service",
  "name":"SERVICE in CITY","serviceType":"SERVICE",
  "url":"https://EXAMPLE.com/SLUG",
  "provider":{"@type":"Person","@id":"https://EXAMPLE.com/#person","name":"FULL NAME"},
  "areaServed":[{"@type":"City","name":"CITY"},{"@type":"AdministrativeArea","name":"REGION"}],
  "description":"META DESCRIPTION." }
</script>
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Q1?","acceptedAnswer":{"@type":"Answer","text":"A1."}},
    {"@type":"Question","name":"Q2?","acceptedAnswer":{"@type":"Answer","text":"A2."}}
  ] }
</script>
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://EXAMPLE.com/"},
    {"@type":"ListItem","position":2,"name":"SERVICE in CITY","item":"https://EXAMPLE.com/SLUG"} ] }
</script>
```
Every service/landing page should carry **3–6 real FAQs visible on the page**, mirrored in `FAQPage` — high-leverage because LLMs lift clean Q&A.

---

## Data / tool product — Organization + WebApplication (homepage)
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"Organization",
  "@id":"https://EXAMPLE.com/#org",
  "name":"BRAND","url":"https://EXAMPLE.com/","logo":"https://EXAMPLE.com/logo.png",
  "email":"info@EXAMPLE.com",
  "description":"ENTITY SENTENCE.",
  "founder":{"@type":"Person","name":"FOUNDER"},
  "sameAs":["https://www.linkedin.com/company/HANDLE","https://x.com/HANDLE"],
  "knowsAbout":["Topic 1","Topic 2"] }
</script>
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"WebApplication",
  "name":"TOOL NAME","url":"https://EXAMPLE.com/","applicationCategory":"FinanceApplication",
  "operatingSystem":"Web","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},
  "publisher":{"@id":"https://EXAMPLE.com/#org"},
  "description":"What the tool computes, free, no signup." }
</script>
```

## Data / tool product — Dataset (declare your data citable)
The CC-BY license is an explicit "you may cite this" — lowers the friction of being quoted.
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"Dataset",
  "name":"DATASET NAME (e.g. Take-home pay by province, 2026)",
  "description":"What it covers, source of the rules/figures, update cadence.",
  "url":"https://EXAMPLE.com/blog/DATA-ARTICLE",
  "creator":{"@id":"https://EXAMPLE.com/#org"},
  "license":"https://creativecommons.org/licenses/by/4.0/",
  "isAccessibleForFree":true,
  "temporalCoverage":"2026",
  "keywords":["keyword 1","keyword 2"] }
</script>
```

---

## SaaS / B2B — SoftwareApplication
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"SoftwareApplication",
  "name":"PRODUCT","applicationCategory":"BusinessApplication","operatingSystem":"Web",
  "url":"https://EXAMPLE.com/","publisher":{"@type":"Organization","name":"BRAND"},
  "offers":{"@type":"Offer","price":"PRICE","priceCurrency":"USD"},
  "description":"What it does, for whom." }
</script>
```

## Ecommerce — Product (+ Offer; Review/AggregateRating ONLY if real)
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"Product",
  "name":"PRODUCT","image":"https://EXAMPLE.com/p.jpg","description":"...",
  "brand":{"@type":"Brand","name":"BRAND"},
  "offers":{"@type":"Offer","price":"PRICE","priceCurrency":"USD","availability":"https://schema.org/InStock","url":"https://EXAMPLE.com/p"} }
</script>
```
> Never add `aggregateRating`/`review` you can't back with real, on-page reviews — fabricated ratings get manual actions.

## Publisher / data article — Article (+ author)
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"Article",
  "headline":"HEADLINE","datePublished":"2026-01-01","dateModified":"2026-01-01",
  "author":{"@type":"Person","name":"AUTHOR","url":"https://EXAMPLE.com/about"},
  "publisher":{"@type":"Organization","name":"BRAND","logo":{"@type":"ImageObject","url":"https://EXAMPLE.com/logo.png"}},
  "mainEntityOfPage":"https://EXAMPLE.com/blog/SLUG",
  "description":"The quotable finding in one line." }
</script>
```

## Directory / aggregator — CollectionPage + ItemList
For a listings/directory page, declare the list and its items so engines can lift the whole set as the answer.
```html
<script type="application/ld+json">
{ "@context":"https://schema.org","@type":"CollectionPage",
  "@id":"https://EXAMPLE.com/best-X-in-CITY",
  "name":"Best X in CITY (2026)","description":"What the list covers and how entries are chosen.",
  "isPartOf":{"@type":"WebSite","name":"BRAND","url":"https://EXAMPLE.com/"},
  "mainEntity":{ "@type":"ItemList","numberOfItems":3,
    "itemListElement":[
      {"@type":"ListItem","position":1,"item":{"@type":"LocalBusiness","name":"Entry One","url":"https://entry-one.com","address":{"@type":"PostalAddress","addressLocality":"CITY"}}},
      {"@type":"ListItem","position":2,"item":{"@type":"LocalBusiness","name":"Entry Two","url":"https://entry-two.com"}},
      {"@type":"ListItem","position":3,"item":{"@type":"LocalBusiness","name":"Entry Three","url":"https://entry-three.com"}}
    ] } }
</script>
```
Swap the inner item `@type` to what you actually list (`Product`, `Organization`, `Service`, …). If you publish the underlying data, add a `Dataset` too (see the data/tool block) — a downloadable, attributable list is highly citable.

## Common pitfalls
- Values must match visible text. No invented reviews/ratings/services/prices.
- **After any data/content change, re-check the schema VALUES still match the page** — it's not enough that the JSON-LD parses; stale schema numbers that contradict the visible page are a trust killer (a common bug after a content update).
- `@id` must be stable and reused so nodes link (don't mint a new `#person` per page).
- `sameAs` URLs must resolve. A dead/incorrect profile URL is worse than none.
- Re-validate after edits; one malformed block can void the page's structured data.
