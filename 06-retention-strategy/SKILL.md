# 06 · Retention & loyalty strategy

Retention không phải là nhắc user quay lại. Là xây hệ thống để user tự muốn quay lại. Ở cấp S, retention dựa vào timing và ưu đãi đơn giản. Ở cấp M, có thể thêm layer gamification và segment-specific mechanic. Ở cấp L, xây loyalty program riêng.

| Cấp độ | Chiến thuật khả thi | Ràng buộc |
|--------|--------------------|-----------|
| **S** | Trigger theo hành vi, voucher tái kích hoạt | In-app + owned out-app, không paid |
| **M** | Loyalty tier, streak mechanic, segment-specific comm | Có paid hỗ trợ kéo về, dev sprint giới hạn |
| **L** | Full loyalty program, Xu economy, VIP layer | Nhiều tháng dev, research, cross-functional team |

## Prompt 11 · Thiết kế retention loop cho campaign

**Khi nào dùng:** Đang thiết kế campaign và muốn có cơ chế giữ chân user ngay từ đầu, không phải chờ đến lúc họ rời đi mới can thiệp.

```
Retention loop cần được thiết kế ngay trong campaign,
không phải sau khi user drop off.

Cấp độ: [S / M / L / XL]
Loại campaign: [voucher drop / game / event / loyalty program / khác]
Ngân sách ước lượng: [số tiền hoặc phạm vi]

Bối cảnh:
- Mục tiêu của campaign: [tăng frequency / kích hoạt user mới / cross-sell]
- Kênh chính: [in-app push / SMS / email / paid social / in-app banner]
- User target: [new / active 30 ngày gần / lapsed >60 ngày / vip]
- Độ dài campaign dự kiến: [số ngày hoặc tuần]

Thiết kế retention loop với 3 phase:

**Phase 1 - Kick-off (Ngày 1-3)**
- User thấy gì và làm gì trong 3 ngày đầu?
- Điều gì đưa họ quay lại lần 2?
- KPI phase này: [tỉ lệ quay lại ngày 3]

**Phase 2 - Engagement (Ngày 4-14)**
- Cơ chế nào khiến user tương tác nhiều hơn 1 lần/tuần?
- Cần trigger gì (và trigger tự động được không)?
- Với [S]: chỉ in-app push + timing thông minh
- Với [M]: thêm trigger qua paid kênh nếu chi phí cho phép
- KPI phase này: [số phiên / user / tuần]

**Phase 3 - Sustain (Ngày 15+)**
- Khi nào user tự nhiên quay lại mà không cần nhắc?
- Điểm nào có thể chuyển họ từ "campaign participant" thành "habitual user"?
- Tỉ lệ giữ chân kỳ vọng ở ngày 30: [số % MAU của cohort]

Yêu cầu output:
1. Retention loop diagram (mô tả bằng text, dùng ASCII nếu cần)
2. 3 điểm quyết định quan trọng nhất trong loop
3. Cách đo mỗi phase — metric nào, dashboard nào
4. Risk: nếu loop không hoạt động, điểm fail đầu tiên là gì
```

**Ví dụ output (cấp S, voucher campaign):**

```
Phase 1 - Kick-off:
- User nhận voucher → redeem trong 48h
- Sau redeem: trigger push "còn 1 voucher đặc biệt nếu quay lại cuối tuần"
- KPI: >40% user dùng voucher lần 2 trong 3 ngày

Phase 2 - Engagement:
- Push reminder ngày 5-7: voucher sắp hết hạn
- Ngày 10: push "bạn đã tiết kiệm được X - tuần sau còn deal tốt hơn"
- Chỉ in-app push, không paid

Phase 3 - Sustain:
- Ngày 21: campaign kết thúc → redirect về loyalty hub
- User đã redeem >=2 lần → tag "active" vào cohort
- Mục tiêu: 15-20% cohort chuyển thành active user hàng tháng
```

## Prompt 12 · Thiết kế loyalty point / Xu economy

**Khi nào dùng:** Cần thiết kế hoặc tối ưu hệ thống điểm thưởng (Xu, loyalty points, coins) — cách kiếm, cách tiêu, và vòng đời giá trị.

```
Cần thiết kế hoặc tối ưu token economy cho loyalty program.

Cấp độ: [S / M / L / XL]
Loại token: [Xu / điểm / coins / stamp / khác]
Hệ thống hiện tại: [mô tả ngắn hoặc "chưa có"]

Mục tiêu:
- [ ] Tăng frequency: user quay lại thường xuyên hơn
- [ ] Tăng basket size: chi tiêu nhiều hơn mỗi lần
- [ ] Tăng cross-sell: dùng thử category mới
- [ ] Tăng retention: giữ user >90 ngày

Ràng buộc:
- Tỉ lệ chi phí điểm / giá trị thực: [vd: 10% - mỗi 10k Xu = 1k giá trị]
- Số dư trung bình user đang có: [số]
- Tỉ lệ user dùng hết điểm trong tháng: [%]
- [Các ràng buộc kỹ thuật / ngân sách khác]

Yêu cầu output:
1. Token earning model: hành vi nào được thưởng? Bao nhiêu?
   - Entry actions: dễ kiếm, lượng nhỏ
   - Engagement actions: cần effort hơn, thưởng lớn hơn
   - Milestone actions: hiếm, thưởng đột biến
2. Token spending model: user tiêu vào đâu?
   - voucher đổi được / cashback / non-monetary rewards
   - Tỉ lệ phần trăm điểm lưu thông mỗi tháng
3. Economy balance:
   - Số điểm vào hệ thống mỗi tháng vs số điểm ra
   - Tỉ lệ lạm phát / giảm phát của token
   - Cơ chế burn: điểm hết hạn? Reset?
4. Gap analysis: giữa earning và spending có gap gì?
   - User tích nhiều nhưng không có gì để tiêu → mất giá trị token
   - User tiêu hết ngay không muốn tích → không tạo retention
5. Với [S]: chỉ cần earning 1-2 action + spending 1-2 item
   Với [M]: thêm tier mechanic + bonus cho hành vi lặp lại
```

## Prompt 13 · Churn prediction & pre-emptive retention

**Khi nào dùng:** Có dữ liệu hành vi user và muốn xây hệ thống tự động phát hiện user sắp rời đi — trước khi họ rời.

```
Xây churn prediction framework cho phép can thiệp sớm.

Cấp độ: [S / M]
Với S: dùng rule-based (không cần ML model)
Với M: có thể dùng simple model hoặc heuristic nâng cao

Dữ liệu sẵn có (khoanh tròn cái nào có):
- Lần active cuối (last_active_date)
- Số phiên 7 ngày / 30 ngày
- Số dư điểm / Xu
- Lần redeem cuối
- Lần mua / giao dịch cuối
- Số voucher đã dùng 30 ngày
- Loại voucher ưa thích

Mục tiêu: phát hiện user "at-risk" trước 7-14 ngày
và can thiệp bằng chi phí tối thiểu.

Yêu cầu output:
1. Risk criteria (cấp S - rule based):
   - High risk: [điều kiện, vd: không active 14 ngày + có điểm chưa dùng]
   - Medium risk: [điều kiện, vd: active giảm 50% so với tháng trước]
   - Low risk: [điều kiện, vd: active đều nhưng chưa redeem]
2. Intervention phù hợp từng risk level:
   - High: voucher cá nhân hóa, giá trị cao hơn, urgency
   - Medium: reminder + ưu đãi nhẹ, personalized comm
   - Low: content-driven retention (tip, thông báo tính năng mới)
3. Với [S]: chỉ làm high risk, 1 loại intervention, tự động qua push
   Với [M]: làm cả 3 level, A/B test intervention message
4. Cost per saved user estimate
5. Metrics: saved rate (user quay lại trong 14 ngày sau intervention)
```

## Prompt 14 · Thiết kế re-engagement campaign cho user lapsed

**Khi nào dùng:** User đã không active >60 ngày. Cần campaign riêng để kéo họ về — không dùng chung message với user đang active.

```
Thiết kế re-engagement campaign cho user lapsed.

Cấp độ: [S / M]
Segment: user lapsed >[số] ngày, chưa uninstall

Dữ liệu:
- Số lượng user trong segment: [số]
- Lý do rời đi (nếu có survey hoặc data): [lý do phổ biến]
- Hành vi trước khi lapsed: [họ từng làm gì? Mua gì? Chơi game gì?]
- Lần tương tác cuối: [ngày / tháng]
- Số dư điểm còn lại: [có / không / bao nhiêu trung bình]

Mục tiêu: [số]% user quay lại và active trong 14 ngày sau campaign

Ngân sách: [ước lượng]
Kênh: [in-app push / SMS / email / paid retargeting]

Yêu cầu output:
1. 3 re-engagement message concepts — khác nhau về góc tiếp cận:
   - "Nhớ bạn" (emotional, community)
   - "Có deal mới" (transactional, FOMO)
   - "Tài khoản bạn vẫn còn X" (utility, sunken cost)
2. Timing strategy: gửi lúc nào,间隔 bao nhiêu ngày, tối đa mấy lần
3. Offer structure:
   - S: 1 offer duy nhất (take it or leave it)
   - M: 2-3 offer variants, A/B test, động học theo response
4. Cost analysis: bao nhiêu user cần quay lại để breakeven
5. Fallback: nếu user không phản hồi sau 2 lần, next step là gì?
```

---

<details>
<summary>English version</summary>

# 06 · Retention & loyalty strategy

Retention is not about reminding users to come back. It's about building a system where users want to come back on their own. At level S, retention relies on timing and simple incentives. At level M, you can add gamification layers and segment-specific mechanics. At level L, you build a full loyalty program.

| Level | Available tactics | Constraints |
|-------|------------------|-------------|
| **S** | Behavior triggers, re-activation vouchers | In-app + owned out-app, no paid |
| **M** | Loyalty tiers, streak mechanics, segment-specific comm | Paid can support re-targeting, limited dev sprint |
| **L** | Full loyalty program, point economy, VIP tiers | Months of dev, research, cross-functional team |

### Prompt 11 · Design retention loop for campaign
*When to use:* You're designing a campaign and want to build retention mechanics from the start — not wait until users leave to intervene.
*(Prompt content mirrors the Vietnamese version above.)*

### Prompt 12 · Design loyalty point / token economy
*When to use:* You need to design or optimize a reward points system — how to earn, how to spend, and the value lifecycle.

### Prompt 13 · Churn prediction & pre-emptive retention
*When to use:* You have user behavior data and want to build an automated system that detects users about to churn — before they leave.

### Prompt 14 · Re-engagement campaign for lapsed users
*When to use:* Users haven't been active for >60 days. You need a separate campaign to win them back — don't use the same message as for active users.

</details>
