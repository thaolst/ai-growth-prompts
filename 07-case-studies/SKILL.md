# 07 · Case Studies — Learning from Real Growth Stories

## Tiếng Việt

Dùng AI để phân tích case study và rút ra bài học áp dụng được cho campaign thực tế. Không đọc thụ động — học cách apply.

---

## Prompt 01 — Phân tích case study và rút bài học

**Khi nào dùng:** Vừa đọc một case study growth, muốn AI phân tích và gợi ý cách apply.

```
Tôi muốn phân tích case study sau và rút ra bài học áp dụng cho campaign của tôi.

Case study: [tên công ty / mô tả ngắn]

Họ đã làm: [tóm tắt tactic chính]
Kết quả: [số liệu nếu có]
Bối cảnh: [thị trường, thời điểm, nguồn lực]

Phân tích giúp tôi:
1. Tại sao tactic đó hiệu quả (root cause, không chỉ surface observation)
2. Yếu tố nào phụ thuộc vào bối cảnh cụ thể của họ (không copy được)
3. Yếu tố nào độc lập với bối cảnh (có thể áp dụng)
4. Cách adapt tactic đó vào campaign của tôi: [mô tả campaign]
5. Rủi ro khi áp dụng và cách mitigate
```

---

## Prompt 02 — So sánh case study với campaign hiện tại

**Khi nào dùng:** Muốn biết một case study nổi tiếng có liên quan gì đến campaign mình đang làm không.

```
So sánh case study sau với campaign của tôi:

Case study: [tên]
Họ làm: [mô tả]
User segment: [mô tả]
KPI họ đo: [mô tả]

Campaign của tôi: [mô tả]
User segment: [mô tả]
KPI: [mô tả]
Mục tiêu: [mô tả]

Hãy:
1. Đánh giá mức độ tương đồng (1-10) trên các khía cạnh: user behavior, business model, market maturity, competition
2. Từ case study đó, rút ra 3 điều tôi có thể apply NGAY vào campaign hiện tại
3. 1 điều tôi KHÔNG nên copy vì khác bối cảnh
```

---

## Prompt 03 — Growth playbook từ nhiều case study

**Khi nào dùng:** Muốn tổng hợp bài học từ nhiều case study thành một playbook.

```
Tổng hợp bài học growth từ các case study sau thành một playbook ngắn:

Danh sách case study:
- [case 1]: [bài học chính]
- [case 2]: [bài học chính]
- [case 3]: [bài học chính]
- [case 4]: [bài học chính]

Lĩnh vực của tôi: [VD: loyalty / fintech / ecommerce]

Playbook cần:
1. 5 nguyên tắc growth xuất hiện nhiều lần (pattern)
2. 3 tactic cụ thể tôi có thể test trong 2 tuần tới
3. Những sai lầm phổ biến từ các case study — tránh
```

---

## English

Use AI to analyze case studies and extract actionable lessons. Not passive reading — learn how to apply.

---

## Prompt 01 — Analyze a case study

**When to use:** Just read a growth case study, want AI to analyze and suggest application.

```
Analyze this case study and extract lessons for my campaign.

Company: [name / brief]
What they did: [key tactics]
Results: [metrics if available]
Context: [market, timing, resources]

Please:
1. Why was the tactic effective? (root cause, not surface)
2. What depended on their specific context? (not copyable)
3. What is context-independent? (applicable)
4. How to adapt to my campaign: [describe]
5. Risks and mitigation
```

---

## Prompt 02 — Compare case study to current campaign

**When to use:** Want to know if a famous case study applies to your current campaign.

```
Compare this case study to my campaign:

Case study: [name]
Their approach: [description]
User segment: [description]

My campaign: [description]
User segment: [description]
Goal: [description]

Please:
1. Similarity score (1-10) on: user behavior, business model, market, competition
2. 3 things I can apply NOW
3. 1 thing I should NOT copy due to different context
```

---

## Prompt 03 — Growth playbook from multiple case studies

**When to use:** Want to synthesize lessons from multiple case studies into a playbook.

```
Synthesize growth lessons from these case studies into a playbook:

Case studies:
- [case 1]: [key lesson]
- [case 2]: [key lesson]
- [case 3]: [key lesson]
- [case 4]: [key lesson]

My field: [e.g., loyalty / fintech / ecommerce]

Playbook needs:
1. 5 recurring growth principles (patterns)
2. 3 specific tactics I can test in 2 weeks
3. Common mistakes from case studies — avoid
```

---

## Ví dụ output — Phân tích case study (Prompt 01)

**Input:**
```
Case study: Duolingo — streak system
Họ làm: Thêm streak counter, push notification "sắp mất streak",
         shield để bảo vệ streak khi bỏ lỡ 1 ngày
Kết quả: DAU tăng 4.5x trong 2 năm
Bối cảnh: app học ngôn ngữ, freemium, mobile-first
Campaign của tôi: loyalty program, user lapsed 30–45 ngày
```

**Output AI:**
```
Tại sao streak hiệu quả (root cause):
Không phải vì reward — mà vì loss aversion.
Người ta ghét mất thứ đang có hơn là muốn có thứ mới.
Streak tạo ra "sunk cost" tâm lý: "Mình đã giữ 15 ngày rồi, không thể mất."

Yếu tố phụ thuộc context Duolingo (không copy được):
- Học ngôn ngữ có natural daily habit loop (học 5 phút/ngày)
- User đã có intrinsic motivation (muốn học)
- Streak shield là premium feature → monetization tied vào habit

Yếu tố độc lập với context (áp dụng được):
- Loss aversion message mạnh hơn reward message
- "Sắp mất" frame mạnh hơn "sắp được"
- Recovery mechanic (shield/grace period) giảm churn khi user lỡ 1 ngày

Adapt vào campaign lapsed user:
Thay vì "Voucher 15k đang chờ bạn" → "Điểm của bạn hết hạn sau 48h"
Thêm: nếu user redeem trong 7 ngày → unlock "streak bonus" lần sau
Rủi ro: loyalty program không có daily trigger tự nhiên như app học —
         cần tạo trigger nhân tạo (push + in-app banner phối hợp)
Mitigate: test push frequency trước (không over-notify segment lapsed)
```

---

## Example output — Case study analysis (Prompt 01)

**Input:** Duolingo streak system. Result: DAU 4.5x in 2 years. My campaign: lapsed user re-engagement.

**AI output:**
```
Why streak worked (root cause):
Not the reward — the loss aversion.
People hate losing what they have more than they want to gain something new.
Streak creates psychological sunk cost: "I've kept this for 15 days, I can't lose it."

Context-dependent factors (not copyable):
- Language learning has natural daily habit loop (5 min/day)
- Users already have intrinsic motivation (want to learn)
- Streak shield is a premium feature → monetization tied to habit

Context-independent factors (applicable):
- Loss aversion message stronger than reward message
- "About to lose" frame stronger than "about to gain"
- Recovery mechanic (grace period) reduces churn when users miss one day

Adapt to lapsed user campaign:
Instead of "15k voucher waiting for you" → "Your points expire in 48h"
Add: redeem within 7 days → unlock "comeback bonus" next time
Risk: loyalty program lacks natural daily trigger unlike learning app
Mitigate: test push frequency first (avoid over-notifying lapsed segment)
```
