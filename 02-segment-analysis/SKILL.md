# 02 · Phân tích segment

Hiểu ai cần target và target thế nào — trong phạm vi kênh cho phép ở mỗi cấp độ campaign.

## Prompt 04 · Phân tích cohort drop để tìm điểm can thiệp

**Khi nào dùng:** Dữ liệu retention cho thấy drop-off nhưng chưa rõ nguyên nhân và cách xử lý.

```
Dữ liệu retention của một cohort loyalty:

[Paste dữ liệu — CSV, bảng, hoặc số liệu]

Ví dụ:
Tuần 0:   100%
Tuần 1:   68%
Tuần 2:   45%
Tuần 4:   38%
Tuần 8:   29%
Tuần 12:  22%

Cấp độ campaign có thể chạy: [S / M]

Phân tích:
1. Điểm rớt mạnh nhất — user đang làm gì ở giai đoạn đó?
2. W0→W1 vs W1→W2 — cái nào đáng lo hơn và tại sao?
3. 3 giả thuyết hành vi cụ thể cho drop
4. Cho mỗi giả thuyết, một thử nghiệm phù hợp [S/M]:
   - S: in-app mechanic hoặc owned channel test, 1–2 tuần
   - M: có thể thêm kênh paid hoặc comm planning
5. Nếu chỉ can thiệp một việc trong tuần này: làm gì?
```

## Prompt 05 · Phân khúc user để phân bổ ngân sách

**Khi nào dùng:** Đã có ngân sách (S hoặc M), cần phân bổ vào nhóm nào.

```
Cần ưu tiên segment nào để target.

Cấp độ: [S / M]
Ngân sách: [ước lượng]
Kênh:
- S: in-app + owned out-app
- M: thêm [kênh paid cụ thể]

Dữ liệu mỗi user:
- Số dư điểm
- Ngày từ lần giao dịch cuối
- Số lần redeem voucher 30 ngày qua
- Danh mục voucher ưa thích
- [Khác nếu có]

Mục tiêu: [tăng MAU / kéo user lapsed / tăng tần suất]

Đề xuất:
1. 3–4 segment tối đa — đủ để thực thi với kênh hiện có
2. Mỗi segment: đặc điểm, % ngân sách, loại voucher phù hợp, lý do
3. Segment nào nên bỏ qua ở mức ngân sách này — và tại sao
4. Nếu chỉ target 1 segment: chọn ai và tại sao?
```

## Prompt 06 · Tìm tín hiệu churn sớm để can thiệp

**Khi nào dùng:** Muốn can thiệp trước khi user ngừng hoạt động — ở cấp S, chỉ dùng owned channels và in-app mechanic.

```
Muốn xác định user có nguy cơ rời bỏ sớm để can thiệp.

Cấp độ: [S / M]
Công cụ can thiệp:
- S: push notification, in-app banner, in-app mechanic
- M: thêm [paid retargeting / owned social / email]

Tín hiệu có thể theo dõi:
- Số ngày từ lần mở app cuối
- Số ngày từ lần redeem voucher cuối
- Xu hướng số dư điểm (tăng / đều / giảm)
- Tỉ lệ tương tác notification (30 ngày qua)

Đề xuất:
1. Tín hiệu nào dự đoán churn mạnh nhất?
2. Combination tín hiệu tốt nhất cho cảnh báo sớm
3. Ngưỡng cảnh báo cụ thể — không quá sớm (tốn công), không quá muộn (vô ích)
4. Can thiệp theo mức rủi ro, chỉ dùng kênh của [S/M]:
   - Thấp → [hành động nhẹ]
   - Trung bình → [hành động mạnh hơn]
   - Cao → [hành động trực tiếp nhất]
```

## Thảo luận

Bạn phân tích segment như thế nào? Tín hiệu churn nào bạn thấy chính xác nhất?

---

# 02 · Segment analysis

Understand who to target and how — within the reach available at each campaign level.

## Prompt 04 · Analyze cohort drop to find intervention points

**When to use:** Retention data shows drop-off but cause and intervention aren't clear.

```
Here is retention data for a loyalty program cohort:

[Paste data — CSV, table, or written numbers]

Example:
Week 0:   100%
Week 1:   68%
Week 2:   45%
Week 4:   38%
Week 8:   29%
Week 12:  22%

Campaign level I can run in response: [S / M]

Please analyze:
1. Steepest drop point — what are users likely doing at that stage?
2. W0→W1 vs W1→W2 — which is more concerning and why?
3. 3 specific behavioral hypotheses for the drop
4. For each hypothesis, one experiment sized for [S/M]:
   - S: in-app mechanic or owned channel test, 1–2 weeks
   - M: can include a paid channel or comm planning layer
5. If only one intervention is possible this week, what is it?
```

## Prompt 05 · Segment users to allocate budget within level constraints

**When to use:** Budget is set (S or M threshold), need to allocate to the right groups.

```
I need to prioritize which user segments to target.

Campaign level: [S / M]
Available budget: [approximate]
Channels available at this level:
- S: in-app + owned out-app
- M: above + [specify paid channels]

Data I have per user:
- Points balance
- Days since last transaction
- Voucher redemptions in past 30 days
- Preferred voucher category
- [Other if available]

Goal: [grow MAU / recover lapsed users / increase frequency]

Please suggest:
1. 3–4 segments max — needs to be executable with available channels
2. For each: characteristics, budget share, best voucher type, reasoning
3. Which segment(s) to skip at this budget level — and why
4. If budget only allows targeting 1 segment, which one and why?
```

## Prompt 06 · Find early churn signals for proactive intervention

**When to use:** Want to intervene before users go inactive — at S level, this relies entirely on owned channels and in-app mechanics.

```
I want to identify at-risk users early enough to intervene.

Campaign level for intervention: [S / M]
Intervention options available:
- S: push notification, in-app banner, in-app mechanic
- M: above + [paid retargeting / owned social / email]

Signals I can track:
- Days since last app open
- Days since last voucher redemption
- Points balance trend (growing / flat / declining)
- Notification engagement rate (past 30 days)
- [Other]

Please suggest:
1. Which signals are strongest predictors of churn?
2. Best signal combination for an early warning threshold
3. Specific threshold values — not too early (wasted effort), not too late (useless)
4. Intervention per risk tier, using only channels available at [S/M]:
   - Low risk → [lightweight action]
   - Medium risk → [stronger action]
   - High risk → [most direct action]
```

## Discussion

How do you analyze segments at your company? Which churn signal has been most accurate in your experience?
