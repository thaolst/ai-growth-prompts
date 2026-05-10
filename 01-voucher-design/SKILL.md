# 01 · Thiết kế voucher

Thiết kế voucher phù hợp với segment user và cấp độ campaign.
Ở cấp S, ít kênh hơn đồng nghĩa mechanic voucher phải tự thân vận động.

## Prompt 01 · Thiết kế bộ voucher cho một segment

**Khi nào dùng:** Đã xác định segment và cấp độ campaign. Cần thiết kế voucher phù hợp.

```
Cần thiết kế bộ voucher cho campaign loyalty.

Cấp độ campaign: [S / M]
Nếu S: chỉ in-app + owned out-app
Nếu M: thêm [kênh paid cụ thể]

Hồ sơ segment:
- Số dư điểm: [thấp / trung bình / cao]
- Tần suất giao dịch: [vd: 1–2 lần/tháng]
- Hành vi gần đây: [vd: đã dùng voucher food, chưa dùng game]
- Số ngày từ lần cuối hoạt động: [số]

Mục tiêu với segment này:
- [vd: kéo user lapsed quay lại / tăng tần suất redeem /
   kích hoạt lần đầu]

Ngân sách voucher mỗi user: [ước lượng / hoặc "hẹp / vừa / linh hoạt"]

Đề xuất:
1. 3 phương án voucher — phù hợp segment và phạm vi kênh của cấp độ đó
   (cấp S: voucher tự hoạt động được, không cần paid reach)
2. Tại sao từng phương án phù hợp với hành vi segment
3. Logic trigger — gửi khi nào, qua kênh nào
4. Cách đo hiệu quả ở ngày 7 và ngày 14
```

## Prompt 02 · Chọn giữa các hướng voucher

**Khi nào dùng:** Có 2–3 hướng, cần chọn nhanh.

```
Đang chọn giữa các hướng voucher cho campaign [S / M].

Phương án A: [mô tả ngắn]
Phương án B: [mô tả ngắn]
Phương án C: [nếu có]

Ràng buộc cấp độ:
- S: chỉ in-app + owned, copy + design, timeline gấp
- M: thêm 1–2 kênh paid và comm planning

KPI chính: [vd: redemption rate / tái tương tác / lần đầu giao dịch]
Rủi ro cần tránh: [vd: ăn thịt user đang active / dễ bị abuse]

Yêu cầu:
1. Phương án nào phù hợp nhất với ràng buộc cấp độ và KPI? Tại sao?
2. Điều gì không khả thi ở cấp S nhưng khả thi ở cấp M?
3. Chốt 1 phương án, kèm lý do rõ ràng.
```

## Prompt 03 · Chẩn đoán voucher đang chạy kém

**Khi nào dùng:** Giữa campaign, redemption rate không đạt mục tiêu. Cần chẩn đoán nhanh.

```
Cấp độ campaign: [S / M]

Voucher đang chạy:
- Loại và điều kiện: [mô tả]
- Audience: [segment]
- Kênh đang dùng: [in-app / push / owned social / paid]
- Số ngày chạy: [số]

Kết quả:
- Redemption rate: [thực tế vs. mục tiêu]
- Notification CTR: [nếu có]
- Điểm rớt: [user dừng ở bước nào?]

Chẩn đoán:
1. Điểm yếu nhất — giá trị voucher, điều kiện, kênh, hay segment?
2. Ở cấp [S/M], có thể thay đổi thực tế gì trong 3 ngày tới?
   (Không thêm kênh mới ở cấp S. Không thay đổi concept giữa campaign.)
3. Nếu chỉ được chọn một thứ: đó là gì?
```

## Thảo luận

Bạn thiết kế voucher thế nào ở công ty bạn? Kinh nghiệm nào bạn thấy hiệu quả nhất — voucher mạnh hay trigger đúng?

---

# 01 · Voucher design

Design vouchers that fit both the user segment and the campaign level.
At S level, fewer channels means the voucher mechanic itself carries more weight.

## Prompt 01 · Design a voucher set for a specific segment

**When to use:** Segment is defined, campaign level is set. Need to design the right voucher within what's available at that level.

```
I need to design a voucher set for a loyalty campaign.

Campaign level: [S / M]
If S: channels are in-app + owned out-app only
If M: channels include in-app, owned out-app, and [specify 1–2 paid channels]

Segment profile:
- Points balance: [low / mid / high — or approximate range]
- Transaction frequency: [e.g. 1–2x per month]
- Recent behavior: [e.g. redeemed food vouchers, hasn't used game features]
- Days since last activity: [number]

Goal with this segment:
- [e.g. re-engage lapsed users / increase redemption frequency /
   drive first transaction]

Voucher budget per user: [approximate — or "tight / moderate / flexible"]

Please suggest:
1. 3 voucher options suited to both the segment and the level's channel scope
   (at S level: vouchers that work without paid media amplification)
2. Why each fits their behavioral pattern
3. Trigger logic — when to send, through which available channel
4. How to measure effectiveness at day 7 and day 14
```

**What good output looks like:**
- Options designed for the available channels, not idealized ones
- At S level: mechanic is self-contained — doesn't depend on paid reach to work
- Trigger is specific (day + behavior condition + channel)
- Metrics match what's actually trackable at that level

## Prompt 02 · Choose between voucher directions

**When to use:** 2–3 directions are on the table, need to pick one fast.

```
I'm choosing between voucher directions for a [S / M] campaign.

Option A: [brief description]
Option B: [brief description]
Option C: [if applicable]

Campaign level constraints:
- S: in-app + owned channels only, content + design assets, tight timeline
- M: adds 1–2 paid channels and comm planning

Primary KPI: [redemption rate / re-engagement / first transaction]
Budget constraint: [tight / moderate]
Risk to avoid: [cannibalizing active users / high abuse potential]

Please:
1. Which option fits best given the level constraints and KPI? Why?
2. What breaks down at S level that might work at M?
3. Final recommendation — one option, clear reason
```

## Prompt 03 · Diagnose an underperforming voucher campaign

**When to use:** Mid-campaign, redemption rate isn't hitting target. Need fast diagnosis.

```
Campaign level: [S / M]

Voucher running:
- Type and conditions: [brief description]
- Audience: [segment description]
- Channels used: [in-app banner / push / owned social / paid — per level]
- Days running: [number]

Results so far:
- Redemption rate: [actual vs. target]
- Notification CTR: [if applicable]
- Drop-off point: [where in the funnel are users stopping?]

Please diagnose:
1. Most likely failure point — voucher value, conditions, channel, or segment fit?
2. At [S/M] level, what can realistically change in the next 3 days?
   (No new channels at S. No concept creative changes mid-campaign.)
3. If only one thing: what is it?
```

**What good output looks like:**
- Diagnosis respects what's changeable at the given level
- Won't suggest adding paid channels if campaign is S
- Prioritizes highest-impact, lowest-effort fix

## Discussion

How do you design vouchers at your company? What works better in your experience — a strong voucher value or smart trigger logic?
