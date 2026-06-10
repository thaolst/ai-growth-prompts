# Changelog

All notable changes to this project are documented here.

## [0.6.0] - 2026-06-10

### Changed
- **Renumbered folders to remove duplicates** - Knowledge Base moved to 08-11 (growth-frameworks, case-studies, glossary, ai-growth), execution folders moved to 12-13 (n8n-growth-workflows, content-agent). Campaign Toolbox keeps 00-07. All internal links updated.
- Removed duplicate 13-content-agent row in English README table.

### Added
- Cross-repo positioning table clarifying when to use ai-growth-prompts, ai-growth-agents-for-marketers, and growth-mcp.

## [0.5.0] - 2026-06-03

### Added
- **11-content-agent** — content agent for personal brand automation (Python). Agent scans repo, suggests 3 topic ideas daily with angle + hook ideas + folder reference. Does not write content — only suggests. Supports LinkedIn, Facebook, Threads format suggestions.
- **11-content-agent/README.md** — full docs in VI + EN with sample output and screenshot
- **11-content-agent/config.example.json** — config template (no tokens)
- **Content pipeline** — Research → Suggest → Track flow for personal brand content

### Changed
- **content-agent.py** — v0.5: Idea Suggester mode. Removed all content-writing logic. Scans repo folders for approved content only.
- **README.md** — added 11-content-agent link in both VI + EN sections

### Fixed
- No tokens in repo (config.json → .gitignore)
- Format: no dashes, no quotes, no slang in generated content

---

## [0.4.0] - 2026-06-03

### Added
- **10-n8n-growth-workflows/SKILL.md** — 5 prompts for workflow selection, customization, pipeline building, debugging, and feature extension. Resolution of the only structural gap (all other folders had SKILL.md).
- **09-ai-growth/SKILL.md** — Added 3 new prompts (total: 08 → 11):
  - Prompt 09: AI growth agent design (autonomous campaign monitoring & decision)
  - Prompt 10: AI content & video script generator for campaigns
  - Prompt 11: AI churn prediction & win-back automation system
  - English versions for prompts 07, 08, 09, 10, 11
- **08-glossary/SKILL.md** — Expanded from a single prompt to a full glossary with 40+ growth marketing terms (VI + EN) organized by category: Strategy & Frameworks, Metrics & Measurement, Optimization & Experimentation, Economics & Loyalty, Growth & Acquisition, Technical & Automation.
- **trending.md** — Refreshed for June 2026: 7 new trends (AI agents, zero-engagement retention, super-app creep, AI personalization at scale, video-first growth loops, privacy-first stack, n8n as default automation). Updated Monthly Signals section with 2026 data.

---

## [0.3.0] - 2026-05-16

### Fixed
- **05-n8n-automation/** - Rewritten completely. Removed flight search workflow reference + tác giả bên ngoài. Nội dung mới: 3 prompt automation thuần growth (competitor monitor, campaign alert, feedback sentiment).
- **Encoding mojibake** - Fixed UTF-8/cp1252 mojibake across 6 files: README.md, 06-growth-frameworks, 07-case-studies, 08-glossary, 09-ai-growth, references.md, trending.md. Em dashes (-), arrows (→), emoji, box-drawing characters restored.
- **Bilingual (VI + EN)**:
  - README.md: Added full Vietnamese section at top (parallel with English)
  - 06-09 folders: Added VI intro lines to every README
  - CONTRIBUTING.md: Updated folder structure to include 05-09
- Removed all external references (Nguyen Thieu Toan, n8n community template)

---

## [0.2.0] - 2026-05-11

### Added
- `05-n8n-automation/` - n8n workflow automation skill
  - SKILL.md: phân tích workflow flight search (Gemini + SerpAPI + Telegram)
  - Adapt pattern cho growth marketing: competitor monitor, campaign tracking, feedback alert
  - Prompt thiết kế workflow automation + cost estimate + scale guide
- `.markdownlint.json` - allowed to be empty

---

## [0.1.0] - 2026-05-10

### Added
- CONTRIBUTING.md - contribution guidelines
- .gitignore - standard ignores for OS and IDE artifacts
- GitHub Actions workflow - markdown lint + link check on push/PR
- Issue templates - bug report & prompt request
- Pull request template

### Fixed
- Renamed `03-game-mechanics` → `03-game-mechanics` folder name

---

## [0.0.1] - 2026-05-03

### Added
- Initial release with 5 prompt folders:
  - 00-campaign-level - S/M/L campaign classification
  - 01-voucher-design - segment-based voucher design
  - 02-segment-analysis - target & intervention analysis
  - 03-game-mechanics - engagement game mechanics
  - 04-comm-and-brief - communication planning & briefs
- Bilingual README (VI + EN)
- SKILL.md prompt files with "when to use / prompt / example output" structure
- Bonus files: SKILL-retention.md, SKILL-game-economy.md
