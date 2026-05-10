# 00 · Xác định cấp độ campaign / Decide campaign level first

Bắt đầu tại đây. Chọn sai level thì toàn bộ execution sau đó bị lệch.
Sai lầm lớn nhất: xử lý campaign M như thể nó chỉ là S, rồi giữa đường mới cuống lên.

Start here. Get the level wrong and everything downstream is miscalibrated.
Biggest mistake: treating an M campaign like "just another S", then scrambling
halfway through.

## Framework

```
Cấp độ  Ngân sách           Kênh                          Đầu việc chính
──────  ──────────────────  ────────────────────────────  ───────────────────────────────
S       < 1B VND/tháng      In-app + owned out-app        Copy content + Design
M       > 1B VND media      Trên + 1–2 kênh paid          + Comm planning + Media plan
L       > 3B VND media      Full channels                 + Concept creative + PM
XL      Campaign công ty    Full channels                 + All of the above
```

```
Tier    Budget              Channels                      Key deliverables
──────  ──────────────────  ────────────────────────────  ───────────────────────────────
S       < 1B VND/month      In-app + owned out-app        Content copy + Design
M       > 1B VND media      Above + 1–2 paid channels     + Comm planning + Media plan
L       > 3B VND media      Full channels                 + Concept creative + PM
XL      Company campaign    Full channels                 + All of the above
```

## S

S là BAU. Chỉ có in-app + owned, không paid. Đầu ra = copy + design, không cần concept creative hay media planning.

S is business-as-usual. In-app and owned channels only. Deliverables = content copy + design — no concept creative, no media planning.

## M

M dành cho campaign cần nhiều hơn copy với banner — như launch tính năng mới, tiếp cận nhóm user mới, hoặc xây thói quen mới.

M is for campaigns that need more than copy and a banner — launching a new feature, entering a new user segment, or building a new habit.

**Đầu ra / Deliverables:**
- Communication framework (message hierarchy, audience x channel x phase)
- Media plan (kênh paid nào, ngân sách, phasing)
- Campaign creative idea (không chỉ sản xuất asset)
- Bộ asset: awareness (video + banner + social) + conversion (banner set)

**Timeline chuẩn bị / Prep timeline:** 4–6 tuần nếu không shoot, 4–8 tuần nếu có shoot. Tổng thời gian campaign tối đa 12 tuần.

## L & XL

Ở L, vai trò của bạn thay đổi. Bạn không còn là người làm — bạn là người cung cấp input. Campaign có PM riêng, agency partners, cross-functional team.

At L, your role shifts. You're not executing — you're an input provider.
The campaign has a dedicated PM, agency partners, and cross-functional team.

**Khi nào lên L / When to escalate to L:**
- Strategic agenda của công ty, không chỉ là promotion
- Budget > 3B VND/tháng chỉ riêng media
- Nhiều team tham gia (product, brand, comms, legal)
- Ảnh hưởng brand dài hạn, không chỉ conversion ngắn hạn

---

## Prompt 00 · Phân loại campaign / Classify campaign level

**Khi nào dùng / When to use:** Ngay từ đầu, trước khi brief bất kỳ ai / At the very beginning, before briefing anyone.

```
Phân loại campaign để xác định cấp độ phù hợp.
Classify a campaign to determine the right level of execution.

Tổng quan / Overview:
- Campaign là gì: [ví dụ: push voucher cho user inactive /
  launch game mechanic mới / promotion mùa vụ]
  What is it: [monthly voucher push / new game launch / seasonal promo]
- Ngân sách ước tính mỗi tháng: [số tiền]
  Estimated budget per month: [amount]
- Thời gian dự kiến: [vd: 2 tuần / 1 tháng]
  Expected duration: [e.g. 2 weeks / 1 month]
- Mục tiêu kinh doanh: [vd: reactivate user lapsed /
  drive first-time redemption / support product milestone]
  Business goal: [recover lapsed users / drive first-time redemption / etc.]
- Đây là campaign độc lập hay thuộc initiative lớn hơn?
  Is this standalone or part of a larger initiative?

Bối cảnh hiện tại / Current context:
- Có campaign lớn nào đang chạy song song? [có / không]
  Any large campaigns running in parallel? [yes / no]
- Team đang tải nặng không? [nhẹ / bình thường / nặng]
  Team's current workload? [light / normal / heavy]

Dựa trên thông tin trên / Based on this:
1. Đề xuất level (S / M / L / XL) kèm lý do
   Recommend the level (S / M / L / XL) with reasoning
2. Cảnh báo nếu budget và mục tiêu không khớp
   Flag if budget and goal seem misaligned
3. Xác định ngày launch sớm nhất có thể
   Identify earliest realistic launch date
4. Một việc cần quyết định trước khi brief
   One thing to decide before briefing anyone
```

---

## Thảo luận / Discussion

Framework này được xây từ kinh nghiệm chạy hàng trăm campaign tại một
công ty fintech ở Việt Nam. Nhưng mỗi công ty phân loại khác nhau.

This framework came from running hundreds of campaigns at a fintech company
in Vietnam. But every company draws the lines differently.

**Câu hỏi cho bạn / Questions for you:**
- Ở công ty bạn, phân loại campaign thế nào? Giống hay khác?
  How do you classify campaigns where you work? Same or different?
- Điều khó nhất khi xác định level là gì — ngân sách mơ hồ, áp lực
  stakeholder, hay thứ khác?
  What's the hardest part — budget ambiguity, stakeholder pressure, or
  something else?
- Chia sẻ cách phân loại của bạn — mình rất muốn học hỏi.
  Drop your classification — I'd love to learn from other teams.
