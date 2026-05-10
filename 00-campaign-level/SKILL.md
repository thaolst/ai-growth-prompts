# 00 · Xác định cấp độ campaign / Campaign Level

---

## 🇻🇳 Tiếng Việt

### Tổng quan

Bắt đầu tại đây. Level quyết định ngân sách, kênh, đầu việc, và timeline.
Chọn sai thì toàn bộ execution sau đó bị lệch. Sai lầm lớn nhất: coi
campaign M như thể nó chỉ là S, rồi giữa đường mới cuống lên.

### Framework

| Cấp độ | Ngân sách | Kênh | Đầu việc chính |
|---------|-----------|------|----------------|
| **S** | < 1B VND/tháng | In-app + owned out-app | Copy content + Design |
| **M** | > 1B VND media | Trên + 1–2 kênh paid | + Comm planning + Media plan |
| **L** | > 3B VND media | Full channels | + Concept creative + PM |
| **XL** | Campaign công ty | Full channels | + All of the above |

### Các cấp độ

**S** — BAU. Chỉ có in-app + owned, không paid.
Đầu ra = copy + design, không cần concept creative hay media planning.

**M** — Campaign cần nhiều hơn copy với banner: launch tính năng mới,
tiếp cận nhóm user mới, xây thói quen mới.

Đầu ra đi kèm:
- Communication framework (message hierarchy, audience x channel x phase)
- Media plan (kênh paid nào, ngân sách, phasing)
- Campaign creative idea
- Bộ asset: awareness (video + banner + social) + conversion (banner set)

Timeline: 4–6 tuần (không shoot), 4–8 tuần (có shoot). Tối đa 12 tuần.

**L & XL** — Vai trò chuyển từ người làm thành người cung cấp input.
Campaign có PM riêng, agency partners, cross-functional team.

Khi nào lên L:
- Strategic agenda của công ty, không chỉ promotion
- Budget > 3B VND/tháng chỉ riêng media
- Nhiều team tham gia (product, brand, comms, legal)
- Ảnh hưởng brand dài hạn

### Prompt: Phân loại campaign

**Khi nào dùng:** Ngay từ đầu, trước khi brief bất kỳ ai.

```
Phân loại campaign để xác định cấp độ phù hợp.

Tổng quan:
- Campaign là gì: [push voucher cho user inactive / launch game mới / promo mùa vụ]
- Ngân sách mỗi tháng: [số tiền]
- Thời gian dự kiến: [2 tuần / 1 tháng]
- Mục tiêu: [reactivate user lapsed / drive first-time redemption / ...]
- Độc lập hay thuộc initiative lớn hơn?

Bối cảnh hiện tại:
- Có campaign lớn nào chạy song song? [có / không]
- Team đang tải nặng không? [nhẹ / bình thường / nặng]

Yêu cầu:
1. Đề xuất level (S / M / L / XL) kèm lý do
2. Cảnh báo nếu budget và mục tiêu không khớp
3. Xác định ngày launch sớm nhất
4. Một việc cần quyết định trước khi brief
```

---

## 🇬🇧 English

### Overview

Start here. Get the level wrong and everything downstream is miscalibrated.
Biggest mistake: treating an M campaign like "just another S", then scrambling
halfway through.

### Framework

| Tier | Budget | Channels | Key deliverables |
|------|--------|----------|------------------|
| **S** | < 1B VND/month | In-app + owned out-app | Content copy + Design |
| **M** | > 1B VND media | Above + 1–2 paid channels | + Comm planning + Media plan |
| **L** | > 3B VND media | Full channels | + Concept creative + PM |
| **XL** | Company campaign | Full channels | + All of the above |

### Tiers

**S** — Business-as-usual. In-app and owned channels only.
Deliverables = content copy + design — no concept creative, no media planning.

**M** — Campaigns that need more than copy and a banner: launching a new
feature, entering a new segment, building a new habit.

Deliverables:
- Communication framework (message hierarchy, audience x channel x phase)
- Media plan (which paid channels, budget split, phasing)
- Campaign creative idea
- Asset set: awareness (video + banner + social) + conversion (banner set)

Prep timeline: 4–6 weeks (no shoot), 4–8 weeks (with shoot). Max 12 weeks.

**L & XL** — Your role shifts from executor to input provider. The campaign
has a dedicated PM, agency partners, and cross-functional team.

Escalate to L when:
- Strategic company agenda, not just a promotion
- Budget > 3B VND/month on media alone
- Multiple teams involved (product, brand, comms, legal)
- Long-term brand impact

### Prompt: Classify campaign level

**When to use:** At the very beginning, before briefing anyone.

```
Classify a campaign to determine the right level of execution.

Overview:
- What is it: [monthly voucher push / new game launch / seasonal promo]
- Estimated budget per month: [amount]
- Expected duration: [e.g. 2 weeks / 1 month]
- Business goal: [recover lapsed users / drive first-time redemption / ...]
- Standalone or part of a larger initiative?

Current context:
- Any large campaigns running in parallel? [yes / no]
- Team's current workload? [light / normal / heavy]

Based on this:
1. Recommend level (S / M / L / XL) with reasoning
2. Flag misalignment between budget and goals
3. Identify earliest realistic launch date
4. One thing to decide before briefing anyone
```

---

## Thảo luận / Discussion

Framework này được xây từ kinh nghiệm thực tế tại một công ty fintech
Việt Nam. Nhưng mỗi công ty phân loại khác nhau.

This framework is built from real experience at a Vietnamese fintech company.
Every company draws the lines differently.

**Câu hỏi cho bạn / Questions for you:**
- Ở công ty bạn, phân loại campaign thế nào?
  How do you classify campaigns where you work?
- Điều khó nhất khi xác định level là gì?
  What's the hardest part about getting the level right?
- Chia sẻ cách của bạn — mình rất muốn học hỏi.
  Share your approach — I'd love to learn.
