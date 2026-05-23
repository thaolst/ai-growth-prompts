# 06 · Growth Frameworks — Mental Model Prompts

## Tiếng Việt

Prompt để hiểu và áp dụng các mental model growth cốt lõi vào campaign thực tế. Dùng khi cần chọn framework phù hợp hoặc debug chiến lược.

---

## Prompt 01 — Chọn framework phù hợp cho campaign

**Khi nào dùng:** Đang design campaign mới, không biết nên dùng mental model nào.

```
Tôi đang thiết kế campaign [mô tả ngắn]. Mục tiêu là [target].

Hãy giúp tôi chọn 1-2 mental model growth phù hợp nhất từ danh sách sau:

1. AARRR (Pirate Metrics) — phân tích từng giai đoạn funnel
2. North Star Metric — tìm metric duy nhất phản ánh giá trị cốt lõi
3. Growth Loops — thiết kế vòng lặp tự duy trì
4. Hook Model (Trigger → Action → Variable Reward → Investment)
5. ICE/RICE — ưu tiên ý tưởng growth
6. Flywheel — xây đà tăng trưởng
7. JTBD (Jobs To Be Done) — hiểu motivation thực sự của user

Yêu cầu:
- Giải thích lý do chọn framework đó
- Áp dụng framework đó vào campaign cụ thể của tôi
- Output dạng: chọn framework → giải thích → apply → expected outcome
```

---

## Prompt 02 — Debug campaign bằng AARRR

**Khi nào dùng:** Campaign đang chạy nhưng metric không đạt target, cần tìm điểm nghẽn.

```
Tôi đang chạy campaign [mô tả]. Các metric hiện tại:

- Acquisition: [số liệu]
- Activation: [số liệu]
- Retention: [số liệu]
- Revenue: [số liệu]
- Referral: [số liệu]

Target không đạt ở giai đoạn: [tên giai đoạn]

Dùng AARRR framework, hãy:
1. Xác định lý do có thể nhất gây ra điểm nghẽn
2. Đề xuất 3 hypothesis cần test
3. Với mỗi hypothesis: cách test, success metric, thời gian test
```

---

## Prompt 03 — Ưu tiên ý tưởng growth bằng ICE

**Khi nào dùng:** Có nhiều ý tưởng growth nhưng không biết làm cái nào trước.

```
Tôi có các ý tưởng growth sau cho [context]:

1. [ý tưởng 1]
2. [ý tưởng 2]
3. [ý tưởng 3]
... (thêm nếu có)

Dùng ICE framework (Impact × Confidence × Ease), hãy:
1. Chấm điểm từng ý tưởng theo 3 tiêu chí (1-10)
2. Tính tổng điểm và sắp xếp thứ tự ưu tiên
3. Giải thích tại sao ý tưởng nào nên làm trước

Điều kiện:
- Impact: mức độ ảnh hưởng đến target KPI
- Confidence: bao nhiêu % chắc chắn sẽ hiệu quả (dựa trên data/reference)
- Ease: dễ implement (thời gian, nguồn lực, phụ thuộc)
```

---

## English

Prompts to understand and apply core growth mental models to real campaigns. Use when you need to pick the right framework or debug a strategy.

---

## Prompt 01 — Pick the right framework

**When to use:** Designing a new campaign, unsure which mental model fits.

```
I'm designing a campaign for [describe]. The goal is [target].

Help me pick 1-2 growth mental models from:

1. AARRR (Pirate Metrics) — funnel stage analysis
2. North Star Metric — single metric reflecting core value
3. Growth Loops — self-sustaining loops
4. Hook Model (Trigger → Action → Variable Reward → Investment)
5. ICE/RICE — growth idea prioritization
6. Flywheel — momentum-driven growth
7. JTBD (Jobs To Be Done) — understand user motivation

Output format: pick framework → explain why → apply to my campaign → expected outcome
```

---

## Prompt 02 — Debug campaign with AARRR

**When to use:** Campaign running below target, need to find the bottleneck.

```
I'm running a campaign [describe]. Current metrics:

- Acquisition: [data]
- Activation: [data]
- Retention: [data]
- Revenue: [data]
- Referral: [data]

Struggling at: [stage name]

Using AARRR, please:
1. Identify the most likely bottleneck cause
2. Propose 3 hypotheses to test
3. For each: test method, success metric, timeline
```

---

## Prompt 03 — Prioritize growth ideas with ICE

**When to use:** Multiple growth ideas, unsure which to execute first.

```
I have these growth ideas for [context]:

1. [idea 1]
2. [idea 2]
3. [idea 3]

Using ICE (Impact × Confidence × Ease), please:
1. Score each idea 1-10 on all three criteria
2. Calculate total score, rank priority
3. Explain top priority choice
```

---

## Ví dụ output — Chọn framework (Prompt 01)

**Input:**
```
Campaign: re-engagement cho user lapsed 30–60 ngày
Mục tiêu: tăng redemption rate từ 5% lên 8% trong 30 ngày
```

**Output AI:**
```
Framework đề xuất: Hook Model + AARRR kết hợp

Tại sao Hook Model phù hợp:
User lapsed đã có habit cũ nhưng vòng lặp bị đứt.
Hook Model giúp xác định đúng chỗ vòng lặp đứt để rebuild:
→ Trigger: họ đang thiếu trigger bên ngoài (push tắt, không có lý do mở app)
→ Action: action cũ (redeem) vẫn còn nhớ — barrier thấp nếu trigger đúng
→ Variable Reward: thêm element bất ngờ thay vì fixed discount
→ Investment: nếu có streak hoặc progress bar, họ không muốn mất

Tại sao thêm AARRR:
Để đo đúng giai đoạn nào đang fail — Acquisition (reach) hay Activation (click→redeem)?
5% redemption rate có thể là: CTR thấp (reach problem) hoặc drop ở landing page (activation problem).
Đo cả 2 trước khi quyết định fix cái gì.

Apply vào campaign:
Bước 1: Check AARRR — CTR push vs redemption rate. Gap ở đâu?
Bước 2: Dùng Hook Model để redesign trigger (push copy) và reward (variable offer thay vì fixed)
Expected: CTR tăng 30% + conversion rate tăng 20% → redemption tổng đạt 8%
```

---

## Example output — Pick framework (Prompt 01)

**Input:** Re-engagement campaign for users lapsed 30–60 days. Goal: redemption rate 5% → 8% in 30 days.

**AI output:**
```
Recommended: Hook Model + AARRR combined

Why Hook Model fits:
Lapsed users had a habit loop that broke. Hook Model identifies exactly
where it broke so you can rebuild it:
→ Trigger: missing external trigger (push off, no reason to open)
→ Action: old action (redeem) still remembered — low barrier if triggered right
→ Variable Reward: add surprise element instead of fixed discount
→ Investment: streak or progress bar creates loss aversion

Why add AARRR:
To measure which stage is failing — reach (Acquisition) or action (Activation)?
5% redemption could mean: low CTR (reach problem) or drop at landing page (activation problem).
Measure both before deciding what to fix.

Application:
Step 1: Check AARRR — push CTR vs redemption rate. Where's the gap?
Step 2: Use Hook Model to redesign trigger (push copy) + reward (variable vs fixed)
Expected: CTR +30%, conversion rate +20% → combined redemption reaches 8%
```
