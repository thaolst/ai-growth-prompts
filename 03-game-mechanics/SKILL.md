# 03 · Game mechanics & tương tác

Game và engagement mechanic - thường dùng nhất ở cấp M, nơi ngân sách hỗ trợ độ phức tạp. Ở cấp S, mechanic cần đơn giản và tự hoạt động được trong in-app.

## Prompt 07 · Thiết kế game mechanic theo cấp độ

**Khi nào dùng:** Cần xây hoặc đề xuất game mechanic. Ở cấp M (ngân sách lớn hơn, kênh paid), mechanic phức tạp hơn khả thi. Ở cấp S, phải đủ đơn giản để chạy chỉ với in-app.

```
Cần thiết kế game mechanic cho loyalty program.

Cấp độ: [S / M / L / XL]
Ngân sách: [ước lượng]

Ràng buộc cấp độ:
- S: mechanic phải chạy hoàn toàn trong app, không có paid reach,
      asset = content + design (không concept creative)
- M: có thể thêm 1–2 kênh paid để kéo user vào,
      có comm planning và media layer

Bối cảnh:
- Hiện có gì: [mô tả game hoặc tính năng hiện tại]
- Tỉ lệ tương tác hiện tại: [% MAU tương tác mỗi tháng]
- Vấn đề chính: [vd: user vào một lần rồi không quay lại /
                 chỉ redeem, không chơi game]
- Ràng buộc: [vd: không có dev sprint lớn /
              phải launch trong prep timeline của cấp độ này]

Audience mục tiêu:
- [Họ là ai và hành vi hiện tại]

Đề xuất:
1. 3 mechanic - phù hợp độ phức tạp của [S/M]
   S: đơn giản, in-house creative làm trong 3–6 tuần
   M: có thể layered hơn, supported by comm planning
2. Mỗi mechanic: user flow, return loop, chi phí điểm ước tính
3. Mechanic nào phù hợp nhất với cấp độ và audience - tại sao
4. Rủi ro và cách giảm thiểu trong ràng buộc của cấp độ
5. Metrics theo dõi ở ngày 14 và ngày 30
```

## Prompt 08 · Tìm friction trong game đang chạy

**Khi nào dùng:** Game đã live, engagement thấp hơn kỳ vọng, cần chẩn đoán nhanh.

```
Cấp độ game: [S / M / L / XL]

Funnel:
Bước 1 – [tên]: [users / %]
Bước 2 – [tên]: [users / %]
Bước 3 – [tên]: [users / %]
Hoàn thành: [users / %]

Bối cảnh:
- Thời gian trung bình từ vào đến hoàn thành: [nếu biết]
- Session length: [ngắn / vừa / dài]

Phân tích:
1. Bước nào mất nhiều user nhất?
2. 3 giả thuyết - cụ thể cho mechanic, không chung chung
3. Test nhanh nhất cho mỗi giả thuyết trong ràng buộc [S/M]:
   - S: đổi copy / điều chỉnh reward / đơn giản hóa flow (không paid boost)
   - M: có thể test với paid traffic push để cô lập biến
4. Quick win trong tuần này không cần dev change lớn?
```

## Thảo luận

Bạn đã dùng game mechanic nào cho loyalty? Cái nào hiệu quả nhất? Bạn có từng gặp trường hợp mechanic quá phức tạp cho cấp độ campaign không?

---

## 03 · Game mechanics & engagement

Game and engagement mechanics - most relevant at M level where budget supports the complexity. At S, mechanics need to be lightweight and self-contained.

## Prompt 07 · Design a game mechanic for a given campaign level

**When to use:** Need to build or propose a game mechanic. At M level (larger budget, paid channels), more complex mechanics are viable. At S, must be simple enough to work on in-app alone.

```
I need to design a game mechanic for a loyalty program.

Campaign level: [S / M / L / XL]
Budget range: [approximate]

Level-specific constraints:
- S: mechanic must work entirely in-app, no paid media amplification,
      asset = content + design (not concept creative)
- M: can include 1–2 paid channels to drive discovery,
      allows comm planning and media layer

Current context:
- What exists now: [brief description of current game or feature]
- Current engagement rate: [% of MAU who engage monthly]
- Core problem: [users enter once and don't return /
                 only redeem, no game interaction]
- Constraint: [no major dev sprint available /
               must launch within prep timeline for this level]

Target audience:
- [Who they are and their current behavior pattern]

Please suggest:
1. 3 mechanics - calibrated to [S/M] complexity and asset scope
   S: simple enough for in-house creative in 3–6 weeks
   M: can be more layered, supported by comm planning
2. For each: user flow, return loop, estimated point cost
3. Which fits this level and audience best - and why
4. Risks and how to reduce them within this level's constraints
5. Metrics to track at day 14 and day 30
```

## Prompt 08 · Find friction in an existing game flow

**When to use:** Game is live, engagement is lower than expected, need fast diagnosis.

```
Campaign level: [S / M / L / XL]

Funnel data:
Step 1 – [step name]: [users / %]
Step 2 – [step name]: [users / %]
Step 3 – [step name]: [users / %]
Completion: [users / %]

Additional context:
- Average time from entry to completion: [if known]
- Session length: [short / medium / long]

Please analyze:
1. Which step loses the most users?
2. 3 hypotheses for why - specific to the mechanic, not generic
3. Fastest test for each hypothesis within [S/M] constraints:
   - S: copy change / reward adjustment / flow simplification (no paid boost)
   - M: can test with a paid traffic push to isolate the variable
4. Quick win possible this week without a major dev change?
```

## Discussion

What game mechanics have you used for loyalty programs? Which ones worked best? Have you ever run into a case where a mechanic was too complex for the campaign level?

---

## Ví dụ output — Thiết kế game mechanic (Prompt 07)

**Input:**
```
Cấp độ: S | Vấn đề: user vào game 1 lần rồi không quay lại
Hiện có: spin wheel đơn giản, không có streak
MAU engagement: 12%
Ràng buộc: không có dev sprint lớn trong 6 tuần tới
```

**Output AI:**
```
3 mechanic phù hợp cấp S (không cần dev lớn):

Mechanic 1 — Daily Streak (khuyến nghị)
Flow: Mở app → spin → nhận reward → "Quay lại ngày mai để giữ streak"
Return loop: Ngày 3 streak → bonus reward. Mất streak → mất bonus.
Chi phí điểm: +50 điểm/ngày, bonus ngày 3: +200 điểm
Implement: chỉ cần thêm counter + push logic, không đổi core mechanic

Mechanic 2 — Weekly Mission
Flow: Mỗi tuần có 3 nhiệm vụ nhỏ → hoàn thành → nhận reward lớn
Return loop: Deadline cuối tuần tạo urgency
Chi phí điểm: 500 điểm/tuần nếu hoàn thành đủ 3 nhiệm vụ
Implement: cần design mission logic — phức tạp hơn mechanic 1

Mechanic 3 — Lucky Hour
Flow: Mỗi ngày 1 khung giờ random → reward x2
Return loop: User check app để biết hôm nay Lucky Hour mấy giờ
Chi phí điểm: tương đương current, chỉ tăng x2 trong 1h
Implement: đơn giản nhất — chỉ cần time-based multiplier

Khuyến nghị: Mechanic 1 (Streak) — phù hợp nhất cấp S,
không cần dev lớn, loss aversion mạnh hơn reward-seeking.

Metrics ngày 14: D7 retention, average sessions/user/week
Metrics ngày 30: streak length distribution, D30 retention
```

---

## Example output — Design game mechanic (Prompt 07)

**Input:** Level S, problem: users play once and don't return, no dev sprint available

**AI output:**
```
3 mechanics suited for S level (no major dev needed):

Mechanic 1 — Daily Streak (recommended)
Flow: Open app → spin → earn reward → "Come back tomorrow to keep streak"
Return loop: Day 3 streak = bonus reward. Break streak = lose bonus.
Point cost: +50 pts/day, Day 3 bonus: +200 pts
Implement: add counter + push logic only, core mechanic unchanged

Mechanic 2 — Weekly Mission
Flow: 3 small tasks per week → complete all → big reward
Return loop: End-of-week deadline creates urgency
Point cost: 500 pts/week if all 3 completed
Implement: requires mission logic design — more complex than option 1

Mechanic 3 — Lucky Hour
Flow: One random hour daily → 2x rewards
Return loop: Users check app to find today's Lucky Hour
Point cost: same as current, 2x multiplier for 1 hour only
Implement: simplest — time-based multiplier only

Recommendation: Mechanic 1 (Streak) — best fit for S level,
no major dev, loss aversion stronger driver than reward-seeking.
```
