# 07 · Experiment design & A/B testing

Experiment là cách duy nhất để biết cái gì thực sự hiệu quả. Ở cấp S, experiment đơn giản: A/B 1 biến, đo 1 metric. Ở cấp M, có thể chạy multivariate, đo nhiều metric, có statistical significance. Ở cấp L, experiment là hệ thống: always-on testing, automated decision.

| Cấp độ | Experiment khả thi | Ràng buộc |
| --- | --- | --- |
| **S** | A/B 1 biến, 1 metric, manual analyze | Traffic thấp, chạy 1-2 tuần, significance khó đạt |
| **M** | A/B đa biến, funnel analysis, cohort compare | Traffic vừa, có track tool, chạy 2-4 tuần |
| **L** | Always-on testing, automated decision, personalization | Full data pipeline, ML model, cross-team |

## Prompt 15 · Thiết kế A/B test cho campaign

**Khi nào dùng:** Sắp launch campaign và muốn test trước 1 biến để tối ưu.

```
Cần thiết kế A/B test cho campaign sắp chạy.

Campaign: [mô tả]
Kênh: [in-app push / email / SMS / paid social]
Cấp độ: [S / M / L]
Traffic dự kiến: [số user / ngày]
Thời gian chạy: [số ngày]

Biến muốn test:
- [ ] Offer / voucher value
- [ ] Message / creative
- [ ] Timing / frequency
- [ ] Segment / targeting
- [ ] CTA / button

Yêu cầu output:
1. Hypothesis: If [biến] then [kết quả] because [lý do]
2. Control vs Treatment mô tả cụ thể
3. Primary metric (1 cái duy nhất)
4. Sample size cần: tính dựa trên baseline + MDE
5. Duration: bao nhiêu ngày để đủ significance
6. Risk: nếu test sai hoặc không đủ traffic thì sao
7. Decision rule: khi nào dừng test, khi nào chọn winner

Với [S]: chấp nhận directional signal (không cần p-value)
Với [M]: yêu cầu p < 0.05, ít nhất 80% power
```

**Ví dụ output:**
```
Hypothesis: If we change notification copy from "Ưu đãi hôm nay"
to "Chỉ còn 4 tiếng" then CTR increases by 15% because urgency
framing activates loss aversion.

Control: "Ưu đãi hôm nay — mở xem ngay"
Treatment: "Chỉ còn 4 tiếng — voucher của bạn sắp hết"

Primary metric: notification CTR
Sample size: 12,000 per group (based on 8% baseline CTR, MDE 15%, 95% confidence)
Duration: 10 days
Decision rule: stop if treatment CTR > control by ≥15% for 3 consecutive days
```

## Prompt 16 · Phân tích kết quả experiment

**Khi nào dùng:** Đã chạy xong test, cần phân tích kết quả và quyết định next step.

```
Phân tích kết quả A/B test sau:

Hypothesis: [mô tả]
Control: [mô tả control]
Treatment: [mô tả treatment]
Thời gian chạy: [số ngày]

Kết quả:
- Control: [metric] = [giá trị], sample = [số]
- Treatment: [metric] = [giá trị], sample = [số]
- p-value: [nếu có]
- Statistical power: [nếu có]

Phân tích:
1. Lift: treatment hơn control bao nhiêu %? (absolute vs relative)
2. Có statistical significance không? (dựa trên p-value + sample size)
3. Có Simpson's paradox không? (kiểm tra segment breakdown)
4. Novelty effect: user mới vs user cũ có phản ứng khác không?
5. Decision:
   - Launch treatment?
   - Chạy lại với sample lớn hơn?
   - Test biến khác?
   - Bỏ ý tưởng này?
6. Nếu có thể launch: estimated impact nếu scale lên 100% user
```

**Ví dụ output:**
```
Lift: +18% relative (8.2% → 9.7% CTR) — vượt MDE 15%
Significance: p = 0.031, đủ significant tại 95% confidence
Simpson's paradox check: new user segment cho thấy +22%, active user +14%
  → treatment hoạt động tốt hơn với new user, cân nhắc personalize
Novelty effect: không phát hiện — CTR ổn định từ ngày 3
Decision: LAUNCH treatment cho toàn bộ user
Estimated impact at 100% rollout: +3,400 clicks/ngày dựa trên 34,000 daily push volume
```

## Prompt 17 · Experiment framework cho growth team

**Khi nào dùng:** Cần xây quy trình experiment từ đầu — từ hypothesis đến decision.

```
Xây experiment framework cho growth team.

Cấp độ: [S / M]
Team size: [số người]
Tool hiện có: [tracking tool / BI / growth platform]
Campaign chạy mỗi tháng: [số campaign]
Tỉ lệ campaign có experiment: [% hiện tại]

Yêu cầu output:
1. Experiment pipeline:
   - Hypothesis backlog: ai propose, review thế nào
   - Prioritization: ICE / RICE / PXL
   - Design: template cho experiment brief
   - Execute: run trong campaign hiện tại
   - Analyze: template cho result report
   - Decide: launch / iterate / kill
2. 3 experiment templates (copy-paste):
   - Offer test (tăng voucher value có tăng conversion không)
   - Message test (urgency vs benefit message)
   - Segment test (target A vs target B)
3. Thresholds:
   - Với [S]: "win" nếu treatment > control 5% sau 2 tuần
   - Với [M]: "win" nếu p < 0.05 + lift > MDE
4. Experiment culture:
   - Failure = learning, không phải waste
   - Document results regardless of outcome
   - Cadence: bao nhiêu experiment / tháng là đủ
```

---

## English

Experiment is the only way to know what actually works. At S level, keep it simple: one variable, one metric, manual analysis. At M level, you can run multivariate tests, track multiple metrics, and achieve statistical significance. At L level, experimentation becomes a system: always-on testing with automated decisions.

| Level | Viable experiments | Constraints |
| --- | --- | --- |
| **S** | A/B 1 variable, 1 metric, manual analysis | Low traffic, 1–2 week runs, significance hard to achieve |
| **M** | Multi-variable A/B, funnel analysis, cohort compare | Medium traffic, tracking tools available, 2–4 week runs |
| **L** | Always-on testing, automated decisions, personalization | Full data pipeline, ML models, cross-team |

## Prompt 15 · Design an A/B test for a campaign

**When to use:** You're about to launch a campaign and want to test one variable first to optimize performance.

```
I need to design an A/B test for an upcoming campaign.

Campaign: [description]
Channel: [in-app push / email / SMS / paid social]
Campaign level: [S / M / L]
Expected traffic: [users per day]
Run duration: [number of days]

Variable to test:
- [ ] Offer / voucher value
- [ ] Message / creative
- [ ] Timing / frequency
- [ ] Segment / targeting
- [ ] CTA / button

Required output:
1. Hypothesis: If [variable] then [outcome] because [reason]
2. Control vs Treatment — specific descriptions
3. Primary metric (one only)
4. Required sample size: calculated from baseline + MDE
5. Duration: how many days to reach significance
6. Risk: what if the test design is wrong or traffic is insufficient?
7. Decision rule: when to stop the test, when to declare a winner

At [S]: directional signal is acceptable (p-value not required)
At [M]: require p < 0.05, at least 80% statistical power
```

**Example output:**
```
Hypothesis: If we change notification copy from "Today's deal"
to "Only 4 hours left" then CTR increases by 15% because urgency
framing activates loss aversion.

Control: "Today's deal — open now"
Treatment: "Only 4 hours left — your voucher expires soon"

Primary metric: notification CTR
Sample size: 12,000 per group (8% baseline CTR, 15% MDE, 95% confidence)
Duration: 10 days
Decision rule: stop if treatment CTR > control by ≥15% for 3 consecutive days
```

## Prompt 16 · Analyze experiment results

**When to use:** Test has finished running and you need to analyze results and decide next steps.

```
Analyze the following A/B test results:

Hypothesis: [description]
Control: [description]
Treatment: [description]
Run duration: [number of days]

Results:
- Control: [metric] = [value], sample = [number]
- Treatment: [metric] = [value], sample = [number]
- p-value: [if available]
- Statistical power: [if available]

Please analyze:
1. Lift: how much better is treatment vs control? (absolute and relative)
2. Is this statistically significant? (based on p-value + sample size)
3. Simpson's paradox check: does the result hold across segments?
4. Novelty effect: do new users and existing users respond differently?
5. Decision:
   - Launch treatment?
   - Re-run with larger sample?
   - Test a different variable?
   - Kill this idea?
6. If launchable: estimated impact at 100% rollout
```

**Example output:**
```
Lift: +18% relative (8.2% → 9.7% CTR) — exceeds 15% MDE
Significance: p = 0.031, significant at 95% confidence
Simpson's paradox check: new users show +22%, active users +14%
  → treatment works better for new users; consider personalizing
Novelty effect: not detected — CTR stable from Day 3 onward
Decision: LAUNCH treatment to all users
Estimated impact at 100% rollout: +3,400 additional clicks/day
  based on 34,000 daily push volume
```

## Prompt 17 · Build an experiment framework for a growth team

**When to use:** You need to build an experimentation process from scratch — from hypothesis to decision.

```
Build an experiment framework for a growth team.

Campaign level: [S / M]
Team size: [number of people]
Current tools: [tracking tool / BI platform / growth platform]
Campaigns per month: [number]
% of campaigns currently with experiments: [%]

Required output:
1. Experiment pipeline:
   - Hypothesis backlog: who proposes, how to review
   - Prioritization method: ICE / RICE / PXL
   - Design: template for experiment brief
   - Execute: how to run within existing campaigns
   - Analyze: template for results report
   - Decide: launch / iterate / kill criteria
2. 3 ready-to-use experiment templates:
   - Offer test (does increasing voucher value increase conversion?)
   - Message test (urgency framing vs benefit framing)
   - Segment test (target group A vs target group B)
3. Win thresholds:
   - At [S]: "win" if treatment > control by 5% after 2 weeks
   - At [M]: "win" if p < 0.05 + lift exceeds MDE
4. Experiment culture principles:
   - Failure = learning, not waste
   - Document all results regardless of outcome
   - Cadence: how many experiments per month is the right pace?
```

**Example output (S level team, 3 people, 4 campaigns/month):**
```
Pipeline (lightweight for S level):
- Backlog: shared Google Sheet, anyone can add
- Prioritization: ICE score — Impact (1-3) × Confidence (1-3) × Ease (1-3)
- Design: 1-page brief: hypothesis, control, treatment, metric, duration
- Execute: split traffic 50/50 in campaign tool
- Analyze: compare results in Sheet after run ends
- Decide: weekly 30-min review meeting

Win threshold at S: treatment > control by ≥5% for 2+ weeks

Cadence: 1 experiment per campaign = 4/month
  → enough to learn 2-3 significant things per quarter
```
