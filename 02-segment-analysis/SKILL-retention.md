# Retention After First Redemption / Giữ user sau lần đổi đầu tiên

## What this skill does / Skill này làm gì

**EN:** Diagnose why users don't return after their first voucher redemption, identify the highest-leverage intervention points, and design mechanics that convert one-time redeemers into habitual users.

**VI:** Chẩn đoán tại sao user không quay lại sau lần đổi voucher đầu tiên, tìm điểm can thiệp hiệu quả nhất, và thiết kế cơ chế biến người đổi một lần thành user có thói quen.

---

## When to use / Khi nào dùng

**EN:** Use when your redemption rate looks healthy but monthly returning redeemers are flat or declining. The problem isn't acquisition - it's habit formation after the first transaction.

**VI:** Dùng khi redemption rate nhìn ổn nhưng returning redeemer hàng tháng không tăng hoặc giảm. Vấn đề không phải là kéo user vào - mà là tạo thói quen sau lần giao dịch đầu tiên.

---

## Core insight / Insight cốt lõi

**EN:** First redemption ≠ loyalty. Loyalty starts at the second redemption. Most programs over-invest in acquisition and under-invest in the D1–D30 window after first redemption - the window where habit forms or dies.

**VI:** Đổi voucher lần đầu không phải loyalty. Loyalty bắt đầu từ lần thứ hai. Hầu hết chương trình đầu tư quá nhiều vào acquisition và quá ít vào khoảng D1–D30 sau lần đổi đầu - khoảng thời gian thói quen hình thành hoặc biến mất.

---

## Prompt 01 - Diagnose the drop after first redemption

**EN:** Use when you see high first-time redemption but low return rate in the following month.
**VI:** Dùng khi lần đổi đầu cao nhưng tỷ lệ quay lại tháng sau thấp.

```
I'm analyzing retention after first voucher redemption in a loyalty program.

Current situation:
- Users who redeemed at least once: [number]
- Users who redeemed again the following month: [number or %]
- Average days between 1st and 2nd redemption (if known): [number]
- What users receive immediately after first redemption: [description or "nothing"]
- Current re-engagement touchpoints after redemption: [push / email / in-app / none]

Please diagnose:
1. Is the drop-off happening immediately after redemption (D1–D7)
   or later (D8–D30)? What does that tell us?
2. What is likely missing in the D1–D7 experience?
   (reward acknowledgment / next step clarity / points visibility / progress toward goal)
3. 3 specific hypotheses for why users don't return
4. For each hypothesis: one experiment to test it within 2 weeks
5. Which single intervention would have the highest impact on 2nd redemption rate?
```

**What good output looks like / Output tốt trông như thế nào:**
- Diagnosis tied to a specific time window, not generic
- Hypotheses about the post-redemption experience, not pre-redemption
- Experiments small enough to run without a major dev sprint

---

## Prompt 02 - Design the post-redemption journey

**EN:** Use when diagnosis is done and you need to design what happens after a user redeems for the first time.
**VI:** Dùng khi đã chẩn đoán xong và cần thiết kế trải nghiệm sau lần đổi đầu tiên.

```
I need to design the post-redemption journey for a loyalty program.

Context:
- What the user just did: redeemed their first voucher ([category])
- Current points balance after redemption: [approximate range]
- Distance to next meaningful reward: [e.g. "500 points away from next voucher tier"]
- Campaign level: [S / M]
- Available touchpoints: [push / in-app / owned social / paid - per level]

Goals:
- Primary: get user to redeem again within [30 / 60] days
- Secondary: increase points balance visibility and perceived progress

Please design:
1. D1 touchpoint - what happens the day after first redemption?
   (acknowledgment, progress nudge, or next challenge?)
2. D7 touchpoint - if user hasn't returned, what's the re-engagement trigger?
3. D30 touchpoint - last chance before user is considered lapsed
4. What "progress signal" should the user see every time they open the app?
   (points balance / streak / distance to reward / tier status)
5. One mechanic that makes the second redemption feel easier than the first
```

**What good output looks like / Output tốt trông như thế nào:**
- Journey has clear timing (D1, D7, D30) not vague "follow up"
- Each touchpoint has a specific message angle, not just "remind them"
- Progress signal is concrete - not "show something motivating"

---

## Prompt 03 - Identify the meaningful threshold for your program

**EN:** Use when you suspect there's a points balance or engagement level that separates users who stay from users who leave - but you haven't confirmed it yet.
**VI:** Dùng khi bạn nghi ngờ có một ngưỡng số dư điểm hoặc mức engagement mà ở đó user có xu hướng ở lại hoặc rời đi - nhưng chưa xác nhận được.

```
I want to find the "meaningful threshold" in my loyalty program -
the point balance or behavior milestone where user retention improves significantly.

Data I have:
- Retention rate by points balance tier: [e.g. <500 pts: X%, 500-999: Y%, 1000+: Z%]
- Or: retention rate by number of redemptions: [1 redemption: X%, 2: Y%, 3+: Z%]
- Average time to reach each tier: [if known]
- Drop in adoption between tiers: [e.g. "60% drop from 1000 to 500 tier"]

Please analyze:
1. Where is the clearest step-change in retention? That's the threshold.
2. Is the threshold driven by points balance, redemption count, or time in program?
3. What's the fastest path to get a new user to that threshold?
   (earn mechanics / onboarding flow / first voucher design)
4. What % of current users are "near threshold" (within reach but haven't crossed)?
   This is the highest-ROI segment to target.
5. One campaign mechanic specifically designed to push near-threshold users over the line
```

**What good output looks like / Output tốt trông như thế nào:**
- Clear threshold with data backing, not a range
- "Near threshold" segment is quantified and actionable
- Campaign mechanic is designed for that specific segment, not everyone
