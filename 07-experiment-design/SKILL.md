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

<details>
<summary>English version</summary>

## English

Prompts for A/B testing, experiment design, hypothesis building, and statistical analysis.

### Prompt 15 · Design A/B test for campaign
*When to use:* You're about to launch a campaign and want to test one variable first to optimize results.
*(Prompt content mirrors the Vietnamese version above.)*

### Prompt 16 · Analyze experiment results
*When to use:* You've run the test and need to analyze results and decide next steps.
*(Prompt content mirrors the Vietnamese version above.)*

### Prompt 17 · Experiment framework for growth teams
*When to use:* You need to build an experiment pipeline from scratch -- from hypothesis to decision.
*(Prompt content mirrors the Vietnamese version above.)*

</details>
