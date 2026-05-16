# ai-growth-prompts

<p align="center">
  <img src="https://img.shields.io/github/v/release/thaolst/ai-growth-prompts?label=version&color=4ade80&style=flat-square" alt="version" />
  <img src="https://img.shields.io/github/license/thaolst/ai-growth-prompts?color=60a5fa&style=flat-square" alt="license" />
  <img src="https://img.shields.io/github/last-commit/thaolst/ai-growth-prompts?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/ai-growth-prompts?style=flat-square&color=facc15&logo=github" alt="stars" />
  <img src="https://img.shields.io/badge/ai-growth--marketing-blue?style=flat-square" alt="topic" />
</p>

> Prompts được kiểm chứng từ chạy campaign thực tế — không template chung chung.
> Built from running loyalty and promotion campaigns where budget levels, channel constraints, and segment behavior actually matter.

---

## Mục lục / Table of Contents

- [Cách dùng / How to Use](#cách-dùng--how-to-use)
- [Cấu trúc / Structure](#cấu-trúc--structure)
- [Nguyên lý / Underlying Logic](#nguyên-lý--underlying-logic)

---

## Cách dùng / How to Use

Mỗi prompt có 3 phần / Each prompt has three parts:

- **Khi nào dùng / When to use** — tình huống cụ thể / the specific situation it's built for
- **Prompt** — copy và điền `[...]` với context thực tế / copy and fill in `[...]` with your actual context
- **Ví dụ output / Example output** — output đúng trông như thế nào / what a good output looks like

---

## Cấu trúc / Structure

### Campaign Toolbox — Prompt thực hành

| Thư mục / Folder | Mô tả / Description |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Bắt đầu tại đây. Quyết định cấp độ S/M/L trước mọi thứ. / Start here. Decide S/M/L before anything else. |
| [`01-voucher-design`](./01-voucher-design) | Thiết kế voucher theo segment, không theo cảm tính. / Design vouchers by segment, not by assumption. |
| [`02-segment-analysis`](./02-segment-analysis) | Target ai, can thiệp lúc nào, phân bổ ngân sách ra sao. / Who to target, when to intervene, how to allocate. |
| [`03-game-mechanics`](./03-game-mechanics) | Cơ chế game kéo user quay lại. / Engagement loops that bring users back. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Communication planning và design brief theo từng cấp độ. / Communication planning and design briefs by level. |
| [`05-automation`](./05-n8n-automation) | Prompt xây automation cho growth: monitor đối thủ, campaign alert, feedback tracking. / Automation prompts for competitor monitoring, campaign alerts, feedback tracking. |

### Knowledge Base — Nền tảng lý thuyết

| Thư mục / Folder | Mô tả / Description |
|---|---|
| [`06-growth-frameworks`](./06-growth-frameworks) | Mental model growth cốt lõi — AARRR, North Star, Growth Loops, Hook, ICE/RICE, JTBD |
| [`07-case-studies`](./07-case-studies) | Câu chuyện growth từ Duolingo, Canva, Notion, Spotify, Dropbox |
| [`08-glossary`](./08-glossary) | 80+ thuật ngữ growth marketing kèm định nghĩa thực tế |
| [`09-ai-growth`](./09-ai-growth) | AI đang thay đổi growth marketing thế nào — personalization, prediction, optimization |

### Resources / Tài liệu tham khảo

| File | Mô tả / Description |
|---|---|
| [`references.md`](./references.md) | Sách, newsletter, podcast, influencer được tuyển chọn / Curated reading list |
| [`trending.md`](./trending.md) | Xu hướng growth marketing hiện tại / What's hot right now |

---

## Nguyên lý / Underlying Logic

Mọi campaign bắt đầu bằng quyết định level ([`00-campaign-level`](./00-campaign-level)). Level đó định nghĩa kênh, ngân sách, timeline bạn thực sự có. Các prompt trong `01-04` được thiết kế để hoạt động trong những ràng buộc đó — không phải điều kiện lý tưởng.

Every campaign starts with a level decision ([`00-campaign-level`](./00-campaign-level)). That level defines what channels, assets, and timeline you actually have. The prompts in `01-04` are calibrated to work within those constraints — not in ideal conditions.

[Knowledge Base](#cấu-trúc--structure) (`06–09`) cung cấp nền tảng lý thuyết. Dùng để nâng cấp tư duy. Dùng [Campaign Toolbox](#campaign-toolbox) để ra kết quả.

*Cập nhật khi có prompt mới được kiểm chứng thực tế / Updated as new prompts are tested in practice.*

---

## Tại sao repo này tồn tại / Why This Exists

Hầu hết tài liệu growth marketing hoặc quá hàn lâm, hoặc quá tool-specific. Repo này là cầu nối — là thứ tôi thực sự dùng khi thiết kế campaign.

Most growth marketing resources are either too academic or too tool-specific. This repo bridges the gap — it's what I actually use when designing campaigns.

---

## License

MIT — use freely, share widely.

*If this helps you, [star the repo](https://github.com/thaolst/ai-growth-prompts) ⭐*
