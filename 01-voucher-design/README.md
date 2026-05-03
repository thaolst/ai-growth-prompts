# 01 · Voucher Design / Thiết kế voucher

**EN:** Vouchers work when they match user behavior — not just offer a discount. These prompts help you design vouchers for specific segments, choose between directions fast, and diagnose why a campaign is underperforming.

**VI:** Voucher hiệu quả khi phù hợp với hành vi người dùng — không phải chỉ vì giảm giá. Các prompt này giúp bạn thiết kế voucher theo từng segment, chọn hướng nhanh, và chẩn đoán tại sao campaign đang không đạt kỳ vọng.

---

## Prompts inside / Prompt trong folder này

| # | Prompt | When to use / Khi dùng |
|---|--------|------------------------|
| 01 | Design a voucher set for a specific segment | Segment đã rõ, cần chọn đúng loại voucher |
| 02 | Choose between voucher directions | Có 2–3 hướng, cần quyết định nhanh |
| 03 | Diagnose an underperforming campaign | Giữa campaign, kết quả thấp hơn target |

→ [`prompts.md`](prompts.md)

---

## Example output / Ví dụ output

**Prompt 01 — segment: users with low balance, inactive 15 days, food category**

```
Recommended vouchers:
1. Food cashback 15% (max 20k) — conditions: transaction > 30k
   Trigger: D+3 after inactivity, push notification 11:30 AM
   Reason: low-commitment entry point, matches existing food behavior

2. Bundle deal: 3 food vouchers for 500 points
   Trigger: after first redemption in the month
   Reason: drives repeat behavior once re-engaged

3. Surprise voucher (reveal after app open)
   Trigger: D+7 if still inactive after first push
   Reason: curiosity mechanic works for disengaged users

Metrics to track: redemption rate D7, D14 / repeat redemption rate
```
