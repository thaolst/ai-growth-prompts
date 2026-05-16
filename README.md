# ai-growth-prompts

<p align="center">
  <img src="https://img.shields.io/github/v/release/thaolst/ai-growth-prompts?label=version&color=4ade80&style=flat-square" alt="version" />
  <img src="https://img.shields.io/github/license/thaolst/ai-growth-prompts?color=60a5fa&style=flat-square" alt="license" />
  <img src="https://img.shields.io/github/last-commit/thaolst/ai-growth-prompts?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/ai-growth-prompts?style=flat-square&color=facc15&logo=github" alt="stars" />
  <img src="https://img.shields.io/badge/ai-growth--marketing-blue?style=flat-square" alt="topic" />
</p>

> Prompts được kiểm chứng từ chạy campaign thực tế, không template chung chung.
> Built from running loyalty and promotion campaigns where budget levels, channel constraints, and segment behavior actually matter.

---

# Tiếng Việt

## Mục lục

- [Cách dùng](#cách-dùng)
- [Cấu trúc](#cấu-trúc)
- [Nguyên lý](#nguyên-lý)

## Cách dùng

Mỗi prompt có 3 phần:

- **Khi nào dùng** — tình huống cụ thể
- **Prompt** — copy và điền `[...]` với context thực tế
- **Ví dụ output** — output đúng trông như thế nào

## Cấu trúc

### Campaign Toolbox — Prompt thực hành

| Thư mục | Mô tả |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Bắt đầu tại đây. Quyết định cấp độ S/M/L trước mọi thứ. |
| [`01-voucher-design`](./01-voucher-design) | Thiết kế voucher theo segment, không theo cảm tính. |
| [`02-segment-analysis`](./02-segment-analysis) | Target ai, can thiệp lúc nào, phân bổ ngân sách ra sao. |
| [`03-game-mechanics`](./03-game-mechanics) | Cơ chế game kéo user quay lại. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Communication planning và design brief theo từng cấp độ. |
| [`05-automation`](./05-n8n-automation) | Prompt xây automation cho growth: monitor đối thủ, campaign alert, feedback tracking. |

### Knowledge Base — Nền tảng lý thuyết

| Thư mục | Mô tả |
|---|---|
| [`06-growth-frameworks`](./06-growth-frameworks) | Mental model growth cốt lõi: AARRR, North Star, Growth Loops, Hook, ICE/RICE, JTBD |
| [`07-case-studies`](./07-case-studies) | Câu chuyện growth từ Duolingo, Canva, Notion, Spotify, Dropbox |
| [`08-glossary`](./08-glossary) | 80+ thuật ngữ growth marketing kèm định nghĩa thực tế |
| [`09-ai-growth`](./09-ai-growth) | AI đang thay đổi growth marketing thế nào: personalization, prediction, optimization |

### Resources

| File | Mô tả |
|---|---|
| [`references.md`](./references.md) | Sách, newsletter, podcast, influencer được tuyển chọn |
| [`trending.md`](./trending.md) | Xu hướng growth marketing hiện tại |

## Nguyên lý

Mọi campaign bắt đầu bằng quyết định level ([`00-campaign-level`](./00-campaign-level)). Level đó định nghĩa kênh, ngân sách, timeline bạn thực sự có. Các prompt trong `01-04` được thiết kế để hoạt động trong những ràng buộc đó, không phải điều kiện lý tưởng.

Knowledge Base (`06-09`) cung cấp nền tảng lý thuyết. Dùng để nâng cấp tư duy. Dùng Campaign Toolbox để ra kết quả.

*Cập nhật khi có prompt mới được kiểm chứng thực tế.*

## Tại sao repo này tồn tại

Hầu hết tài liệu growth marketing hoặc quá hàn lâm, hoặc quá tool-specific. Repo này là cầu nối, là thứ tôi thực sự dùng khi thiết kế campaign.

---

# English

## Table of Contents

- [How to Use](#how-to-use)
- [Structure](#structure)
- [Underlying Logic](#underlying-logic)

## How to Use

Each prompt has three parts:

- **When to use** — the specific situation it's built for
- **Prompt** — copy and fill in `[...]` with your actual context
- **Example output** — what a good output looks like

## Structure

### Campaign Toolbox

| Folder | Description |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Start here. Decide S/M/L before anything else. |
| [`01-voucher-design`](./01-voucher-design) | Design vouchers by segment, not by assumption. |
| [`02-segment-analysis`](./02-segment-analysis) | Who to target, when to intervene, how to allocate. |
| [`03-game-mechanics`](./03-game-mechanics) | Engagement loops that bring users back. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Communication planning and design briefs by level. |
| [`05-automation`](./05-n8n-automation) | Automation prompts for competitor monitoring, campaign alerts, feedback tracking. |

### Knowledge Base

| Folder | Description |
|---|---|
| [`06-growth-frameworks`](./06-growth-frameworks) | Core growth mental models: AARRR, North Star, Growth Loops, Hook, ICE/RICE, JTBD |
| [`07-case-studies`](./07-case-studies) | Public growth stories from Duolingo, Canva, Notion, Spotify, Dropbox |
| [`08-glossary`](./08-glossary) | 80+ growth marketing terms with practical definitions |
| [`09-ai-growth`](./09-ai-growth) | How AI is transforming growth: personalization, prediction, optimization |

### Resources

| File | Description |
|---|---|
| [`references.md`](./references.md) | Curated reading list: books, newsletters, podcasts, influencers |
| [`trending.md`](./trending.md) | What's hot in growth marketing right now |

## Underlying Logic

Every campaign starts with a level decision ([`00-campaign-level`](./00-campaign-level)). That level defines what channels, assets, and timeline you actually have. The prompts in `01-04` are calibrated to work within those constraints, not in ideal conditions.

The Knowledge Base folders (`06-09`) provide the theoretical foundation. Use them to level up your thinking. Use the Campaign Toolbox to get things done.

*Updated as new prompts are tested in practice.*

## Why This Exists

Most growth marketing resources are either too academic or too tool-specific. This repo bridges the gap — it's what I actually use when designing campaigns.

---

## License

MIT — use freely, share widely.

*If this helps you, [star the repo](https://github.com/thaolst/ai-growth-prompts) ⭐*
