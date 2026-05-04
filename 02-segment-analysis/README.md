# 02 · Segment Analysis / Phân tích segment

**EN:** Targeting everyone means reaching no one. These prompts help you read cohort data, allocate limited budget to the right groups, and find early signals before users churn.

**VI:** Target tất cả mọi người nghĩa là không reach được ai. Các prompt này giúp bạn đọc cohort data, phân bổ ngân sách đúng nhóm, và tìm signal sớm trước khi user rời đi.

---

## Prompts inside / Prompt trong folder này

| # | File | Nội dung |
|---|------|----------|
| 04–06 | SKILL.md | Cohort analysis, budget allocation, early churn signals |
| 07–09 | SKILL-retention.md | Retention sau lần đổi đầu tiên — chẩn đoán, journey design, meaningful threshold |

→ [`prompts.md`](prompts.md)

---

## Example output / Ví dụ output

**Prompt 06 — early churn signals for a loyalty program**

```
Signal ranking (strongest → weakest):
1. Days since last voucher redemption (> 21 days = high risk)
2. Notification ignored 3x in a row (disengagement signal)
3. Points balance unchanged for 14 days (no earn, no burn)
4. Days since last app open (> 10 days combined with above)

Best combination: no redemption 21d + 3 ignored notifications
→ probability of churn within 14 days: high

Thresholds:
- Low risk:   no redemption 10–14 days → lightweight push
- Medium risk: no redemption 15–20 days → voucher offer
- High risk:  no redemption 21d + ignored notifs → best voucher + different channel

Intervention per tier:
- Low:    reminder push "Your vouchers are waiting"
- Medium: targeted voucher matching their last redeemed category  
- High:   surprise high-value voucher, send at different time of day
```
