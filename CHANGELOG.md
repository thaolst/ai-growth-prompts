# Changelog

All notable changes to this project are documented here.

## [0.3.0] — 2026-05-16

### Fixed
- **05-n8n-automation/** — Rewritten completely. Removed flight search workflow reference + tác giả bên ngoài. Nội dung mới: 3 prompt automation thuần growth (competitor monitor, campaign alert, feedback sentiment).
- **Encoding mojibake** — Fixed UTF-8/cp1252 mojibake across 6 files: README.md, 06-growth-frameworks, 07-case-studies, 08-glossary, 09-ai-growth, references.md, trending.md. Em dashes (—), arrows (→), emoji, box-drawing characters restored.
- **Bilingual (VI + EN)**:
  - README.md: Added full Vietnamese section at top (parallel with English)
  - 06-09 folders: Added VI intro lines to every README
  - CONTRIBUTING.md: Updated folder structure to include 05-09
- Removed all external references (Nguyen Thieu Toan, n8n community template)

---

## [0.2.0] — 2026-05-11

### Added
- `05-n8n-automation/` — n8n workflow automation skill
  - SKILL.md: phân tích workflow flight search (Gemini + SerpAPI + Telegram)
  - Adapt pattern cho growth marketing: competitor monitor, campaign tracking, feedback alert
  - Prompt thiết kế workflow automation + cost estimate + scale guide
- `.markdownlint.json` — allowed to be empty

---

## [0.1.0] — 2026-05-10

### Added
- CONTRIBUTING.md — contribution guidelines
- .gitignore — standard ignores for OS and IDE artifacts
- GitHub Actions workflow — markdown lint + link check on push/PR
- Issue templates — bug report & prompt request
- Pull request template

### Fixed
- Renamed `03-game-mechanics` → `03-game-mechanics` folder name

---

## [0.0.1] — 2026-05-03

### Added
- Initial release with 5 prompt folders:
  - 00-campaign-level — S/M/L campaign classification
  - 01-voucher-design — segment-based voucher design
  - 02-segment-analysis — target & intervention analysis
  - 03-game-mechanics — engagement game mechanics
  - 04-comm-and-brief — communication planning & briefs
- Bilingual README (VI + EN)
- SKILL.md prompt files with "when to use / prompt / example output" structure
- Bonus files: SKILL-retention.md, SKILL-game-economy.md
