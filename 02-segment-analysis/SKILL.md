# 02 · Phân tích segment

Hiểu ai cần target và target thế nào - trong phạm vi kênh cho phép ở mỗi cấp độ campaign.

| Cấp độ | Dữ liệu có sẵn | Phân tích được |
|--------|---------------|----------------|
| **S** | Cohort, RFM cơ bản | Phân khúc hành vi, chọn 1 nhóm |
| **M** | Thêm dữ liệu kênh paid | Multi-segment, phân bổ budget |
| **L** | Full data + research | Nghiên cứu định tính + định lượng |

## Prompt 04 · Phân tích cohort drop để tìm điểm can thiệp

**Khi nào dùng:** Dữ liệu retention cho thấy drop-off nhưng chưa rõ nguyên nhân và cách xử lý.

```
Dữ liệu retention của một cohort loyalty:

[Paste dữ liệu - CSV, bảng, hoặc số liệu]

Ví dụ:
Tuần 0:   100%
Tuần 1:   68%
Tuần 2:   45%
Tuần 4:   38%
Tuần 8:   29%
Tuần 12:  22%

Cấp độ campaign có thể chạy: [S / M / L / XL]

Phân tích:
1. Điểm rớt mạnh nhất - user đang làm gì ở giai đoạn đó?
2. W0→W1 vs W1→W2 - cái nào đáng lo hơn và tại sao?
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

Cấp độ: [S / M / L / XL]
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
1. 3–4 segment tối đa - đủ để thực thi với kênh hiện có
2. Mỗi segment: đặc điểm, % ngân sách, loại voucher phù hợp, lý do
3. Segment nào nên bỏ qua ở mức ngân sách này - và tại sao
4. Nếu chỉ target 1 segment: chọn ai và tại sao?
```

## Prompt 06 · Tìm tín hiệu churn sớm để can thiệp

**Khi nào dùng:** Muốn can thiệp trước khi user ngừng hoạt động - ở cấp S, chỉ dùng owned channels và in-app mechanic.

```
Muốn xác định user có nguy cơ rời bỏ sớm để can thiệp.

Cấp độ: [S / M / L / XL]
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
3. Ngưỡng cảnh báo cụ thể - không quá sớm (tốn công), không quá muộn (vô ích)
4. Can thiệp theo mức rủi ro, chỉ dùng kênh của [S/M]:
   - Thấp → [hành động nhẹ]
   - Trung bình → [hành động mạnh hơn]
   - Cao → [hành động trực tiếp nhất]
```

## Thảo luận

Bạn phân tích segment như thế nào? Tín hiệu churn nào bạn thấy chính xác nhất?

---

## 02 · Segment analysis

Understand who to target and how - within the reach available at each campaign level.

## Prompt 04 · Analyze cohort drop to find intervention points

**When to use:** Retention data shows drop-off but cause and intervention aren't clear.

```
Here is retention data for a loyalty program cohort:

[Paste data - CSV, table, or written numbers]

Example:
Week 0:   100%
Week 1:   68%
Week 2:   45%
Week 4:   38%
Week 8:   29%
Week 12:  22%

Campaign level I can run in response: [S / M / L / XL]

Please analyze:
1. Steepest drop point - what are users likely doing at that stage?
2. W0→W1 vs W1→W2 - which is more concerning and why?
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

Campaign level: [S / M / L / XL]
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
1. 3–4 segments max - needs to be executable with available channels
2. For each: characteristics, budget share, best voucher type, reasoning
3. Which segment(s) to skip at this budget level - and why
4. If budget only allows targeting 1 segment, which one and why?
```

## Prompt 06 · Find early churn signals for proactive intervention

**When to use:** Want to intervene before users go inactive - at S level, this relies entirely on owned channels and in-app mechanics.

```
I want to identify at-risk users early enough to intervene.

Campaign level for intervention: [S / M / L / XL]
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
3. Specific threshold values - not too early (wasted effort), not too late (useless)
4. Intervention per risk tier, using only channels available at [S/M]:
   - Low risk → [lightweight action]
   - Medium risk → [stronger action]
   - High risk → [most direct action]
```

## Discussion

How do you analyze segments at your company? Which churn signal has been most accurate in your experience?

---

## Không có data? Dùng benchmark này

Nếu chưa có số liệu thực, dùng benchmark ngành dưới đây để điền placeholder:

| Metric | Benchmark thấp | Benchmark trung bình | Benchmark cao |
|---|---|---|---|
| Push CTR | 2% | 5% | 10% |
| Redemption rate | 3% | 8% | 15% |
| D7 retention | 15% | 30% | 50% |
| D30 retention | 5% | 15% | 30% |
| Churn rate / tháng | 5% | 15% | 30% |
| A/B test MDE | 5% | 10% | 20% |
| Sample size (MDE 10%, 95% CI) | ~1,500/group | ~3,800/group | ~9,500/group |

**Cách dùng:** Điền benchmark "trung bình" vào placeholder, chạy prompt, sau đó thay bằng số thực khi có.

---

## Không có data? Use these benchmarks

If you don't have real numbers yet, use these industry benchmarks to fill placeholders:

| Metric | Low | Mid | High |
|---|---|---|---|
| Push CTR | 2% | 5% | 10% |
| Redemption rate | 3% | 8% | 15% |
| D7 retention | 15% | 30% | 50% |
| D30 retention | 5% | 15% | 30% |
| Monthly churn | 5% | 15% | 30% |
| A/B test MDE | 5% | 10% | 20% |
| Sample size (MDE 10%, 95% CI) | ~1,500/group | ~3,800/group | ~9,500/group |

**How to use:** Fill "mid" benchmarks into placeholders, run the prompt, replace with real numbers when available.

---

## Ví dụ output — Phân tích cohort drop (Prompt 04)

**Input:**
```
Tuần 0: 100% | Tuần 1: 62% | Tuần 2: 41% | Tuần 4: 29% | Tuần 8: 18%
Cấp độ có thể chạy: S
```

**Output AI:**
```
Điểm rớt mạnh nhất: W0→W1 (-38 điểm) — đây là early activation problem,
không phải retention problem. User chưa kịp thấy giá trị lần đầu đã rời.

W0→W1 đáng lo hơn W1→W2:
W1→W2 rớt 21 điểm — user đã activate nhưng không có lý do quay lại.
W0→W1 rớt 38 điểm — user thậm chí chưa bắt đầu. Fix W0→W1 trước.

3 giả thuyết:
1. Onboarding flow quá dài → user bỏ trước khi thấy reward đầu tiên
2. Reward đầu tiên quá nhỏ → không đủ để trigger quay lại
3. Không có nudge nào trong 48h đầu → user quên mất app

Test cho cấp S (không cần paid):
1. Đổi onboarding: bỏ bước 3/4, cho user thấy reward ngay trong 60 giây
2. Tăng reward lần đầu: 5k → 10k, đo redemption D3
3. Thêm push D2: "Bạn còn 48h để dùng ưu đãi chào mừng"

Nếu chỉ làm 1 việc tuần này: thêm push D2 — ít effort nhất,
test được trong 1 tuần, không cần dev change.
```

---

## Ví dụ output — Phân khúc user (Prompt 05)

**Input:**
```
Cấp độ: S | Ngân sách: 80M VND | Mục tiêu: tăng MAU
Kênh: in-app push + owned social
```

**Output AI:**
```
3 segment ưu tiên (bỏ qua inactive >90 ngày ở ngân sách này):

Segment A — "Sleepers" (lapsed 30–60 ngày, từng active)
→ 35% ngân sách | Voucher giảm 15k, expiry 48h
→ Lý do: highest reactivation potential, còn nhớ app

Segment B — "Low-frequency actives" (1 lần/tháng, có balance)
→ 40% ngân sách | Voucher tích lũy: redeem 2 lần → nhận bonus
→ Lý do: dễ push lên 2 lần/tháng hơn là kéo user lạnh về

Segment C — "New users tháng này" (đăng ký <30 ngày)
→ 25% ngân sách | Push milestone: "Hoàn thành profile để nhận 5k"
→ Lý do: habit formation window, ROI dài hạn cao nhất

Bỏ qua: inactive >90 ngày — cost/saved user quá cao với ngân sách S.
```

---

## Example output — Cohort drop analysis (Prompt 04)

**Input:** Week 0: 100% → W1: 62% → W2: 41% → W4: 29% → W8: 18%. Level: S

**AI output:**
```
Steepest drop: W0→W1 (-38 points) — early activation problem,
not a retention problem. Users leave before experiencing value.

W0→W1 is more concerning than W1→W2:
W1→W2 drops 21 points — users activated but found no reason to return.
W0→W1 drops 38 points — users never even started. Fix this first.

3 hypotheses:
1. Onboarding too long → users quit before seeing first reward
2. First reward too small → not enough to trigger return visit
3. No nudge in first 48h → users forget the app exists

S-level tests (no paid budget needed):
1. Shorten onboarding: remove step 3/4, show reward within 60 seconds
2. Increase first reward: 5k → 10k, measure D3 redemption
3. Add D2 push: "48 hours left to claim your welcome reward"

If only 1 action this week: add the D2 push — lowest effort,
testable in 1 week, no dev change required.
```
