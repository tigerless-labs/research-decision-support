---
tags: [methodology-repository]
---

# [GitHub] zarazhangrui/frontend-slides -- style-as-spec documents + three-tier progressive selection (~25k stars)

github.com/zarazhangrui/frontend-slides (24.9k stars, a Claude Code skill) · sister repo
github.com/zarazhangrui/beautiful-html-templates (3.5k stars, an agent-agnostic template library,
vendored wholesale into the skill as `bold-template-pack/`) · sampled 2026-07 · the author is
neither a programmer nor a designer.

Core logic: **the true form of an HTML template is design.md** -- each of the 34 styles is a
declarative spec (YAML frontmatter: colors / color-aliases / typography / components tokens +
signature-element prose), not finished HTML; `template.html` is only the fallback when the spec
lacks detail. Selection runs three-tier progressive loading: `selection-index.json`
(mood/formality/density/scheme + compact best_for/avoid_for metadata) -> `preview.md` for the
shortlist (small preview cards) -> the full `design.md` of the final pick only, with a
"never bulk-read" usage policy embedded in the index. Production method: AI generates + a human
gatekeeps taste against real design references; taste rules discovered in each iteration are
hardened into the specs (anti-AI-slop bans -- no purple gradients, no cliched fonts -- globalized
in SKILL.md).

**Relevance to this project**: "the human supplies taste, the agent supplies volume, and judgment
hardens into versioned specs" is isomorphic to this project's thesis. Its style-library
architecture was ported on 2026-07-09 as this skill's built-in style pack (`styles/`, validator
trust gate, since PR #3) -- the porting decision and the differences (agent-readable only,
mandatory light/dark dual palettes, red-team validation) are distilled in downstream idea and
output docs, not cited here (references point forward only).
