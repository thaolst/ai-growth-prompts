# ai-growth-prompts

<p align="center">
  <img src="https://img.shields.io/github/v/release/thaolst/ai-growth-prompts?label=version&color=4ade80&style=flat-square" alt="version" />
  <img src="https://img.shields.io/github/license/thaolst/ai-growth-prompts?color=60a5fa&style=flat-square" alt="license" />
  <img src="https://img.shields.io/github/last-commit/thaolst/ai-growth-prompts?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/ai-growth-prompts?style=flat-square&color=facc15&logo=github" alt="stars" />
  <img src="https://img.shields.io/badge/ai-growth--marketing-blue?style=flat-square" alt="topic" />
  <a href="https://github.com/thaolst/ai-growth-prompts/discussions"><img src="https://img.shields.io/badge/💬-Discussions-8b5cf6?style=flat-square" alt="discussions" /></a>
</p>

<p align="center">
  <a href="https://star-history.com/#thaolst/ai-growth-prompts&Date"><img src="https://api.star-history.com/svg?repos=thaolst/ai-growth-prompts&type=Date" width="400" alt="Star History" /></a>
</p>

> Prompts được kiểm chứng từ chạy campaign thực tế, không template chung chung.
> Built from running loyalty and promotion campaigns where budget levels, channel constraints, and segment behavior actually matter.

💡 **Mới:** [AI Growth Agents for Marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) - bản nâng cấp có Python + CI/CD + Agent Skills. Prompt từ repo này đã được đóng gói thành agent chạy được.

# Tiếng Việt

## Mục lục

- [Cách dùng](#cách-dùng)
- [Cấu trúc](#cấu-trúc)
- [Nguyên lý](#nguyên-lý)
- [Tham gia](#tham-gia--join-the-community)

## Cách dùng

Mỗi prompt có 3 phần:

- **Khi nào dùng** - tình huống cụ thể
- **Prompt** - copy và điền `[...]` với context thực tế
- **Ví dụ output** - output đúng trông như thế nào

## Cấu trúc

### Campaign Toolbox - Prompt thực hành

| Thư mục | Mô tả |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Bắt đầu tại đây. Quyết định cấp độ S/M/L trước mọi thứ. |
| [`01-voucher-design`](./01-voucher-design) | Thiết kế voucher theo segment, không theo cảm tính. |
| [`02-segment-analysis`](./02-segment-analysis) | Target ai, can thiệp lúc nào, phân bổ ngân sách ra sao. |
| [`03-game-mechanics`](./03-game-mechanics) | Cơ chế game kéo user quay lại. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Communication planning và design brief theo từng cấp độ. |
| [`05-automation`](./05-n8n-automation) | **Thiết kế** automation logic (tool-agnostic): competitor monitor, campaign alert, sentiment tracker. Dùng n8n/Make/Zapier/Python đều được. |
| [`06-retention-strategy`](./06-retention-strategy) | Retention loop, Xu economy, churn prediction, re-engagement. |
| [`07-experiment-design`](./07-experiment-design) | A/B test, hypothesis design, statistical analysis, experiment framework. |
| [`12-n8n-growth-workflows`](./12-n8n-growth-workflows) | **Thực thi** ngay: 5 workflow n8n có file JSON import sẵn. Cần cài n8n. Dùng sau khi đọc `05`. |
| [`13-content-agent`](./13-content-agent) | **Tự động** personal brand: Python script Research → Queue → Draft → Track. LinkedIn, Facebook, Twitter. |

### Knowledge Base - Nền tảng lý thuyết

| Thư mục | Mô tả | Skill |
|---|---|---|
| [`08-growth-frameworks`](./08-growth-frameworks) | Mental model growth cốt lõi: AARRR, North Star, Growth Loops, Hook, ICE/RICE, JTBD | [`SKILL.md`](./08-growth-frameworks/SKILL.md) |
| [`09-case-studies`](./09-case-studies) | Câu chuyện growth từ Duolingo, Canva, Notion, Spotify, Dropbox | [`SKILL.md`](./09-case-studies/SKILL.md) |
| [`10-glossary`](./10-glossary) | 80+ thuật ngữ growth marketing kèm định nghĩa thực tế | [`SKILL.md`](./10-glossary/SKILL.md) |
| [`11-ai-growth`](./11-ai-growth) | AI đang thay đổi growth marketing thế nào: personalization, prediction, optimization | [`SKILL.md`](./11-ai-growth/SKILL.md) |

### Resources

| File | Mô tả |
|---|---|
| [`references.md`](./references.md) | Sách, newsletter, podcast, influencer được tuyển chọn |
| [`trending.md`](./trending.md) | Xu hướng growth marketing hiện tại |

## Hệ sinh thái repo

Mình có 3 repo phục vụ 3 mục đích khác nhau:

| Repo | Là gì | Dùng khi nào |
|---|---|---|
| [ai-growth-prompts](https://github.com/thaolst/ai-growth-prompts) (repo này) | Thư viện prompt theo chủ đề, copy-paste được ngay | Cần prompt cho 1 task cụ thể: thiết kế voucher, phân tích segment, viết brief |
| [ai-growth-agents-for-marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) | Workflow nhiều bước dạng prompt + script, có skill cài cho Claude Code | Muốn chạy quy trình end-to-end: lập kế hoạch MEU, phân tích A/B test |
| [growth-mcp](https://github.com/thaolst/growth-mcp) | MCP server đóng gói logic growth thành tool | Muốn Claude/Cursor gọi tool trực tiếp thay vì paste prompt |

## Nguyên lý

Mọi campaign bắt đầu bằng quyết định level ([`00-campaign-level`](./00-campaign-level)). Level đó định nghĩa kênh, ngân sách, timeline bạn thực sự có. Các prompt trong `01-04` được thiết kế để hoạt động trong những ràng buộc đó, không phải điều kiện lý tưởng.

Knowledge Base (`08-11`) cung cấp nền tảng lý thuyết. Dùng để nâng cấp tư duy. Dùng Campaign Toolbox để ra kết quả.

*Cập nhật khi có prompt mới được kiểm chứng thực tế.*

# English

## Table of Contents

- [How to Use](#how-to-use)
- [Structure](#structure)
- [Underlying Logic](#underlying-logic)

## How to Use

Each prompt has three parts:

- **When to use** - the specific situation it's built for
- **Prompt** - copy and fill in `[...]` with your actual context
- **Example output** - what a good output looks like

## Structure

### Campaign Toolbox

| Folder | Description |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Start here. Decide S/M/L before anything else. |
| [`01-voucher-design`](./01-voucher-design) | Design vouchers by segment, not by assumption. |
| [`02-segment-analysis`](./02-segment-analysis) | Who to target, when to intervene, how to allocate. |
| [`03-game-mechanics`](./03-game-mechanics) | Engagement loops that bring users back. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Communication planning and design briefs by level. |
| [`05-automation`](./05-n8n-automation) | **Design** automation logic (tool-agnostic): competitor monitor, campaign alert, sentiment tracker. Works with n8n, Make, Zapier, or Python. |
| [`06-retention-strategy`](./06-retention-strategy) | Retention loops, point economy, churn prediction, re-engagement. |
| [`07-experiment-design`](./07-experiment-design) | A/B testing, hypothesis design, statistical analysis, experiment framework. |
| [`12-n8n-growth-workflows`](./12-n8n-growth-workflows) | **Execute** immediately: 5 n8n workflows with importable JSON files. Requires n8n. Read `05` first for the logic. |
| [`13-content-agent`](./13-content-agent) | **Automate** personal brand: Python script for Research → Queue → Draft → Track. LinkedIn, Facebook, Twitter. |

### Knowledge Base

| Folder | Description | Skill |
|---|---|---|
| [`08-growth-frameworks`](./08-growth-frameworks) | Core growth mental models: AARRR, North Star, Growth Loops, Hook, ICE/RICE, JTBD | [`SKILL.md`](./08-growth-frameworks/SKILL.md) |
| [`09-case-studies`](./09-case-studies) | Public growth stories from Duolingo, Canva, Notion, Spotify, Dropbox | [`SKILL.md`](./09-case-studies/SKILL.md) |
| [`10-glossary`](./10-glossary) | 80+ growth marketing terms with practical definitions | [`SKILL.md`](./10-glossary/SKILL.md) |
| [`11-ai-growth`](./11-ai-growth) | How AI is transforming growth: personalization, prediction, optimization | [`SKILL.md`](./11-ai-growth/SKILL.md) |

### Resources

| File | Description |
|---|---|
| [`references.md`](./references.md) | Curated reading list: books, newsletters, podcasts, influencers |
| [`trending.md`](./trending.md) | What's hot in growth marketing right now |

## Repo ecosystem

I maintain 3 repos serving different purposes:

| Repo | What it is | When to use |
|---|---|---|
| [ai-growth-prompts](https://github.com/thaolst/ai-growth-prompts) (this repo) | Topic-based prompt library, ready to copy-paste | You need a prompt for one specific task: voucher design, segment analysis, campaign brief |
| [ai-growth-agents-for-marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) | Multi-step workflows as prompts + scripts, installable as Claude Code skills | You want an end-to-end process: MEU planning, A/B test analysis |
| [growth-mcp](https://github.com/thaolst/growth-mcp) | MCP server packaging growth logic as callable tools | You want Claude/Cursor to call tools directly instead of pasting prompts |

## Underlying Logic

Every campaign starts with a level decision ([`00-campaign-level`](./00-campaign-level)). That level defines what channels, assets, and timeline you actually have. The prompts in `01-04` are calibrated to work within those constraints, not in ideal conditions.

The Knowledge Base folders (`08-11`) provide the theoretical foundation. Use them to level up your thinking. Use the Campaign Toolbox to get things done.

*Updated as new prompts are tested in practice. Latest version: v0.5.0.*

## Tham gia / Join the community

- [💬 GitHub Discussions](https://github.com/thaolst/ai-growth-prompts/discussions) - hỏi đáp, chia sẻ prompt, góp ý
- [📝 Contributing](./CONTRIBUTING.md) - hướng dẫn đóng góp prompt mới
- [🐛 Report issue](https://github.com/thaolst/ai-growth-prompts/issues) - báo lỗi hoặc đề xuất

## License

MIT - use freely, share widely.

*If this helps you, [star the repo](https://github.com/thaolst/ai-growth-prompts) ⭐*
