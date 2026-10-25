#!/usr/bin/env python3
"""Builds assets/hero.svg and assets/engagement.svg — animated, self-contained SVGs for the README.

The leverage bars are an ORDER, not measurements: widths only show rank. Keep it that way —
this repo's whole argument is "never present a guess as a number".
Usage: python3 scripts/make-assets.py path/to/lighthouse-ink.png
"""
import base64, sys, pathlib

CREAM, INK, DIM, ORANGE, AMBER, BUTTER = "#FBF5E7", "#1A1408", "#7A6B4C", "#F0531C", "#F7C63F", "#FDF0C4"
SERIF = "Didot, 'Bodoni 72', 'Bodoni MT', 'Playfair Display', Georgia, 'Songti SC', serif"
SANS = "'Avenir Next', 'Helvetica Neue', 'PingFang SC', 'Noto Sans CJK SC', Arial, sans-serif"
MONO = "'SF Mono', 'JetBrains Mono', Menlo, Consolas, monospace"

# (lever, note, relative weight 0–1 — rank only)
LEVERS = [
    ("Third-party citations & mentions", "the dominant lever — Reddit, listicles, press, Wikidata", 1.0),
    ("Original data in your content", "the thing journalists and engines quote", .72),
    ("Extractable answer structure", "answer first, question-shaped headings", .58),
    ("Structured data", "schema.org that matches the visible page", .48),
    ("Entity & authority", "one consistent entity across GBP, Wikidata, profiles", .42),
    ("Freshness", "dated, maintained, re-crawled", .33),
    ("AI-crawler access", "eligibility, not advantage", .27),
    ("llms.txt", "ship it; never sell it", .08),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hero(img_b64: str) -> str:
    W, H, loop = 1200, 640, 12
    lx, ly = 250, 150  # lamp, in canvas coordinates
    rows, y0, rh, bx, bmax = [], 262, 38, 540, 560
    for i, (name, note, w) in enumerate(LEVERS):
        y = y0 + i * rh
        top = i == 0
        d = 1.2 + i * 0.22
        rows.append(f'''
  <text x="{bx - 14}" y="{y + 14}" text-anchor="end" class="num" style="fill:{ORANGE if top else DIM}">{i + 1}</text>
  <text x="{bx}" y="{y + 14}" class="nm" style="{'fill:' + ORANGE + ';font-weight:700' if top else ''}">{esc(name)}<tspan class="nt" dx="10">{esc(note)}</tspan></text>
  <rect x="{bx}" y="{y + 21}" width="{bmax}" height="5" fill="{BUTTER}"/>
  <rect x="{bx}" y="{y + 21}" width="{bmax * w:.0f}" height="5" fill="{ORANGE if top else INK}" class="grow" style="animation-delay:{d:.2f}s"/>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="geo-engine: the leverage hierarchy for getting named by AI answer engines, top lever first.">
<defs>
  <linearGradient id="beamR" x1="0" x2="1"><stop offset="0" stop-color="{AMBER}" stop-opacity=".75"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></linearGradient>
  <linearGradient id="beamL" x1="1" x2="0"><stop offset="0" stop-color="{AMBER}" stop-opacity=".75"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></linearGradient>
  <clipPath id="frame"><rect x="27" y="27" width="{W - 54}" height="{H - 54}"/></clipPath>
</defs>
<style>
  .t{{font-family:{SERIF};fill:{INK}}} .s{{font-family:{SANS};fill:{INK}}}
  .num{{font:400 22px {SERIF}}} .nm{{font:500 15px {SANS};fill:{INK}}} .nt{{font:400 12.5px {SANS};fill:{DIM}}}
  .grow{{transform-box:fill-box;transform-origin:left center;animation:grow {loop}s cubic-bezier(.2,.8,.2,1) infinite}}
  .bR{{transform-origin:{lx}px {ly}px;animation:sweepR 6s ease-in-out infinite}}
  .bL{{transform-origin:{lx}px {ly}px;animation:sweepL 6s ease-in-out infinite}}
  .glow{{animation:glow 6s ease-in-out infinite}}
  @keyframes grow{{0%{{transform:scaleX(0)}}12%{{transform:scaleX(1)}}88%{{transform:scaleX(1)}}96%,100%{{transform:scaleX(0)}}}}
  @keyframes sweepR{{0%,100%{{transform:scaleX(1);opacity:1}}50%{{transform:scaleX(.05);opacity:0}}}}
  @keyframes sweepL{{0%,100%{{transform:scaleX(.05);opacity:0}}50%{{transform:scaleX(1);opacity:1}}}}
  @keyframes glow{{0%,100%{{opacity:1}}25%,75%{{opacity:.55}}}}
  @media (prefers-reduced-motion:reduce){{.grow,.bR,.bL,.glow{{animation:none}}.bL{{opacity:0}}}}
</style>
<rect width="{W}" height="{H}" fill="{CREAM}"/>
<rect x="18" y="18" width="{W - 36}" height="{H - 36}" fill="none" stroke="{INK}" stroke-width="2"/>
<rect x="26" y="26" width="{W - 52}" height="{H - 52}" fill="none" stroke="{INK}" stroke-width=".7"/>
<g clip-path="url(#frame)">
<polygon class="bR" points="{lx},{ly - 6} {lx + 900},{ly - 120} {lx + 900},{ly + 90} {lx},{ly + 6}" fill="url(#beamR)" opacity=".9"/>
<polygon class="bL" points="{lx},{ly - 6} {lx - 230},{ly - 70} {lx - 230},{ly + 60} {lx},{ly + 6}" fill="url(#beamL)"/>
</g>
<image x="40" y="82" width="420" height="420" href="data:image/png;base64,{img_b64}"/>
<circle cx="{lx}" cy="{ly}" r="9" fill="{AMBER}" class="glow"/>
<text x="250" y="548" text-anchor="middle" class="s" style="font-size:11px;letter-spacing:4px;fill:{DIM}">WORK TOP-DOWN</text>
<text x="540" y="82" class="s" style="font-size:12px;letter-spacing:4px;fill:{ORANGE};font-weight:600">AVOWD · OPEN METHOD · MIT</text>
<text x="536" y="146" class="t" style="font-size:64px">geo-engine</text>
<text x="540" y="182" class="s" style="font-size:17px;fill:{DIM}">Get named when someone asks an AI. Not ranked — named.</text>
<text x="540" y="230" class="s" style="font-size:11px;letter-spacing:3px;fill:{DIM}">THE LEVERAGE HIERARCHY · BAR LENGTH = ORDER, NOT A MEASUREMENT</text>
{"".join(rows)}
<text x="40" y="{H - 44}" class="s" style="font-size:12px;fill:{DIM}">Measure first with <tspan style="fill:{INK};font-weight:600">does-ai-know-you</tspan> · then move the numbers with <tspan style="fill:{INK};font-weight:600">geo-engine</tspan> · a Claude Code skill</text>
</svg>
'''


def engagement() -> str:
    W, H = 1200, 250
    phases = [("0", "Scope & baseline", "target questions · month 0"),
              ("1", "Audit", "scored, prioritized roadmap"),
              ("2", "On-site", "eligibility: crawlers, schema, answers"),
              ("3", "Off-site", "the lever: citations & mentions"),
              ("4", "Measure & report", "same questions, every month")]
    xs = [140 + i * 230 for i in range(5)]
    cy = 120
    nodes = []
    for i, ((n, name, sub), x) in enumerate(zip(phases, xs)):
        hot = n == "3"
        nodes.append(f'''
  <g class="pop" style="animation-delay:{i * .9:.1f}s">
    <circle cx="{x}" cy="{cy}" r="34" fill="{ORANGE if hot else CREAM}" stroke="{INK}" stroke-width="1.6"/>
    <text x="{x}" y="{cy + 10}" text-anchor="middle" class="t" style="font-size:30px;fill:{CREAM if hot else INK}">{n}</text>
    <text x="{x}" y="{cy + 64}" text-anchor="middle" class="s" style="font-size:15px;font-weight:600">{esc(name)}</text>
    <text x="{x}" y="{cy + 84}" text-anchor="middle" class="s" style="font-size:12px;fill:{DIM}">{esc(sub)}</text>
  </g>''')
    path = f"M{xs[0]},{cy} L{xs[4]},{cy}"
    loop = f"M{xs[4]},{cy - 34} C{xs[4]},{cy - 100} {xs[3]},{cy - 100} {xs[3]},{cy - 34}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="The engagement: scope, audit, on-site, off-site, measure — then off-site and measure repeat monthly.">
<style>
  .t{{font-family:{SERIF};fill:{INK}}} .s{{font-family:{SANS};fill:{INK}}}
  .pop{{animation:pop 9s ease infinite}}
  @keyframes pop{{0%{{opacity:.25}}6%,90%{{opacity:1}}100%{{opacity:.25}}}}
  @media (prefers-reduced-motion:reduce){{.pop{{animation:none}}}}
</style>
<rect width="{W}" height="{H}" fill="{CREAM}"/>
<path d="{path}" stroke="{INK}" stroke-width="1.2" fill="none"/>
<path d="{path}" stroke="{ORANGE}" stroke-width="3" fill="none" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100">
  <animate attributeName="stroke-dashoffset" values="100;0;0;100" keyTimes="0;.45;.9;1" dur="9s" repeatCount="indefinite"/>
</path>
<path id="loop" d="{loop}" stroke="{ORANGE}" stroke-width="1.4" stroke-dasharray="4 5" fill="none"/>
<text x="{(xs[3] + xs[4]) / 2}" y="{cy - 92}" text-anchor="middle" class="s" style="font-size:11px;letter-spacing:3px;fill:{ORANGE}">EVERY MONTH</text>
<circle r="5" fill="{ORANGE}"><animateMotion dur="3s" repeatCount="indefinite" path="{loop}"/></circle>
{"".join(nodes)}
</svg>
'''


if __name__ == "__main__":
    img = base64.b64encode(pathlib.Path(sys.argv[1]).read_bytes()).decode()
    root = pathlib.Path(__file__).resolve().parent.parent / "assets"
    (root / "hero.svg").write_text(hero(img))
    (root / "engagement.svg").write_text(engagement())
    print("wrote", root / "hero.svg", root / "engagement.svg")
