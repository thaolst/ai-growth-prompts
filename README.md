# ai-growth-prompts

<p align="center">
  <img src="https://img.shields.io/github/v/release/thaolst/ai-growth-prompts?label=version&color=4ade80&style=flat-square" alt="version" />
  <img src="https://img.shields.io/github/license/thaolst/ai-growth-prompts?color=60a5fa&style=flat-square" alt="license" />
  <img src="https://img.shields.io/github/last-commit/thaolst/ai-growth-prompts?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/ai-growth-prompts?style=flat-square&color=facc15&logo=github" alt="stars" />
</p>

> Prompts mình dùng thực tế trong công việc growth marketing. Không phải template chung chung - được xây từ kinh nghiệm chạy campaign loyalty và promotion thực chiến, nơi level ngân sách, giới hạn kênh, và hành vi từng segment thực sự ảnh hưởng đến kết quả.

## Mục lục

- [Cách dùng](#cách-dùng)
- [Cấu trúc](#cấu-trúc)
- [Logic xuyên suốt](#logic-xuyên-suốt)

## Cách dùng

Mỗi prompt có 3 phần:

- **Khi nào dùng** - tình huống cụ thể
- **Prompt** - copy và điền `[...]` theo context thực tế của bạn
- **Ví dụ output** - output đúng trông như thế nào

## Cấu trúc

| Folder | Mô tả |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Bắt đầu tại đây. Xác định level S/M/L trước mọi thứ. |
| [`01-voucher-design`](./01-voucher-design) | Thiết kế voucher theo segment, không theo cảm tính. |
| [`02-segment-analysis`](./02-segment-analysis) | Target ai, can thiệp lúc nào, phân bổ thế nào. |
| [`03-game-meu`](./03-game-meu) | Loop engagement giúp user quay lại. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Plan truyền thông và brief design theo từng level. |

## Logic xuyên suốt

Mọi campaign bắt đầu bằng việc xác định level (`00`). Level đó quyết định kênh, asset, và timeline bạn thực sự có. Các prompt từ `01-04` được thiết kế để hoạt động trong giới hạn đó - không phải trong điều kiện lý tưởng.

*Cập nhật khi có prompt mới được kiểm chứng thực tế.*

<details>
<summary>English version</summary>

> Prompts I use in real growth marketing work. Not generic templates - these come from running loyalty and promotion campaigns at scale, where budget levels, channel constraints, and segment behavior actually matter.

### How to use

Each prompt has three parts:

- **When to use** - the specific situation it's built for
- **Prompt** - copy and fill in `[...]` with your actual context
- **Example output** - what a good output looks like

### Structure

| Folder | Description |
|---|---|
| [`00-campaign-level`](./00-campaign-level) | Start here. Decide S/M/L before anything else. |
| [`01-voucher-design`](./01-voucher-design) | Design vouchers by segment, not by assumption. |
| [`02-segment-analysis`](./02-segment-analysis) | Who to target, when to intervene, how to allocate. |
| [`03-game-meu`](./03-game-meu) | Engagement loops that bring users back. |
| [`04-comm-and-brief`](./04-comm-and-brief) | Communication planning and design briefs by level. |

### Underlying logic

Every campaign starts with a level decision (`00`). That level defines what channels, assets, and timeline you actually have. The prompts in `01-04` are calibrated to work within those constraints - not in ideal conditions.

*Updated as new prompts are tested in practice.*

</details>
