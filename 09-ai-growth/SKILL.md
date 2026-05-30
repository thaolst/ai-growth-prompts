# 09 · AI × Growth Marketing — Prompt Ứng Dụng AI

## Tiếng Việt

Prompt để tận dụng AI trong growth marketing. Từ personalization, segmentation, campaign optimization đến predictive analytics và gamification.

**6 prompt theo tình huống thực tế. Điền placeholder → paste → lấy kết quả ngay.**

---

## Prompt 01 — AI personalization cho campaign

**Khi nào dùng:** Muốn AI gợi ý cách cá nhân hóa campaign cho từng segment user.

```
Tôi muốn dùng AI để cá nhân hóa campaign sau:

Campaign: [mô tả — VD: voucher giảm 20% cho đơn hàng tiếp theo]
Segments: [VD: new user (đăng ký < 7 ngày), active user (order trong 30 ngày), dormant (không login > 60 ngày)]
Kênh: [push notification / email / in-app banner]
Dữ liệu có sẵn: [behavior history / purchase history / demographics]

Hãy thiết kế personalization strategy:
1. Với mỗi segment: message chính, offer, timing khác nhau thế nào
2. Cách AI có thể tự động điều chỉnh offer dựa trên real-time behavior
3. Metric để đo mức độ personalization hiệu quả
4. Rủi ro: khi nào personalization phản tác dụng
```

**Ví dụ output mong đợi:**
> Segment dormant: Message "Bạn vẫn còn 50 điểm sắp hết hạn" (loss aversion) + voucher 25% (cao hơn active user) + gửi lúc 8pm thứ 6. Metric: reactivation rate trong 7 ngày.

---

## Prompt 02 — AI phân tích campaign performance

**Khi nào dùng:** Campaign vừa kết thúc, muốn AI phân tích nhanh thay vì tự đọc dashboard.

```
Phân tích performance campaign sau giúp tôi:

Campaign: [mô tả — VD: flash sale 48h giảm 30%]
KPI chính: [VD: redemption rate]
Actual: [VD: 8.2%]
Target: [VD: 10%]
Thời gian chạy: [VD: 15-16/05/2025]

Dữ liệu kèm theo:
- Redemption theo ngày: [VD: ngày 1: 5.1%, ngày 2: 3.1%]
- Redemption theo segment: [VD: new user 12%, active 9%, dormant 2%]
- Chi phí: [VD: 45 triệu VND, CAC = 85k/user]

Phân tích:
1. Campaign performance overall — đạt hay không đạt target? Vì sao?
2. Segment nào hoạt động tốt nhất / tệ nhất? Tại sao?
3. Điểm gì bất thường trong dữ liệu (anomaly)?
4. 3 đề xuất cụ thể cho campaign lần sau
Trả về dạng bảng tóm tắt + bullet điểm chính.
```

**Ví dụ output mong đợi:**
> | Segment | Redemption | vs Target | Nhận xét |
> |---|---|---|---|
> | New user | 12% | +2% | Tốt — offer mới hấp dẫn |
> | Dormant | 2% | -8% | Cần re-engagement riêng trước campaign |

---

## Prompt 03 — AI gợi ý A/B test

**Khi nào dùng:** Có nhiều ý tưởng A/B test, cần AI ưu tiên và thiết kế test.

```
Tôi muốn chạy A/B test cho campaign sau:

Campaign: [mô tả]
Hiện tại đang dùng (control): [mô tả — VD: push notification lúc 9am, offer 20%]
Ý tưởng cần test: [liệt kê 3-5 ý tưởng — VD:
  1. Đổi giờ gửi sang 7pm
  2. Tăng offer lên 30% cho dormant
  3. Thay text "Ưu đãi hôm nay" → "Chỉ còn 4 tiếng"
  4. Thêm ảnh sản phẩm vào push]
Traffic có thể dùng: [VD: 50,000 user]
Thời gian test: [VD: 2 tuần]

Hãy giúp tôi:
1. Ưu tiên ý tưởng nào nên test trước (potential impact cao + dễ implement)
2. Thiết kế test: control vs variant, cách chia traffic, duration
3. Dự đoán kết quả: optimistic / realistic / pessimistic scenario
4. Cách xác định statistical significance (dùng công thức đơn giản)
5. Nếu chỉ test được 1 biến: nên test gì nhất?
```

**Ví dụ output mong đợi:**
> Ưu tiên #1: Test urgency copy ("Chỉ còn 4 tiếng") — low effort, high impact. Split 50/50, cần ~12,000 user mỗi nhóm để đạt 95% confidence với uplift 15%.

---

## Prompt 04 — AI dự đoán campaign outcome

**Khi nào dùng:** Trước khi launch campaign, muốn AI dự đoán kết quả dựa trên dữ liệu lịch sử.

```
Tôi sắp launch campaign mới. Dựa trên dữ liệu lịch sử, hãy dự đoán kết quả.

Campaign mới: [mô tả]
Ngân sách: [số]
Target segment: [mô tả]
Kênh: [liệt kê]

Dữ liệu lịch sử (3 campaign gần nhất):
- Campaign A: [mô tả ngắn + metric — VD: flash sale tháng 3, redemption 9.5%, CAC 72k]
- Campaign B: [mô tả ngắn + metric]
- Campaign C: [mô tả ngắn + metric]

Dự đoán:
1. Expected redemption rate (range: pessimistic / realistic / optimistic)
2. Segment nào performance nhất / kém nhất
3. Rủi ro chính dựa trên pattern từ campaign trước
4. Điều chỉnh gì để tăng xác suất thành công
```

**Ví dụ output mong đợi:**
> Dự đoán redemption: pessimistic 6%, realistic 9%, optimistic 12%. Rủi ro chính: dormant segment historically underperforms 60% vs active — cân nhắc loại khỏi target hoặc dùng offer riêng.

---

## Prompt 05 — AI phân tích churn & segmentation *(mới)*

**Khi nào dùng:** Muốn AI phân tích dữ liệu hành vi để xác định nhóm có nguy cơ churn cao và đề xuất can thiệp.

```
Tôi cần phân tích churn risk và segmentation cho user base của mình.

Thông tin sản phẩm: [VD: app đặt đồ ăn, subscription hàng tháng]
Tổng user active: [số]

Dữ liệu hành vi có sẵn (mô tả hoặc paste CSV):
- Frequency: [VD: số lần login / order trong 30 ngày qua]
- Recency: [VD: ngày cuối cùng login / order]
- Monetary: [VD: tổng chi tiêu 90 ngày]
- Engagement signals: [VD: push open rate, feature usage]

Hãy giúp tôi:
1. Phân nhóm user thành 4-5 segment dựa trên dữ liệu trên (đặt tên dễ nhớ)
2. Với mỗi segment: đặc điểm chính, % user ước tính, mức độ churn risk
3. Segment nào cần can thiệp ngay trong 30 ngày tới?
4. Với mỗi segment có churn risk cao: đề xuất 1 action cụ thể (message, offer, hoặc flow)
5. Leading indicator nào nên theo dõi hàng tuần để phát hiện churn sớm?
Trả về dạng bảng segment + action plan.
```

**Ví dụ output mong đợi:**
> | Segment | Đặc điểm | Churn risk | Action |
> |---|---|---|---|
> | Champions | Order 4+/tháng, recency < 7 ngày | Thấp | Loyalty reward |
> | At-risk | Từng active, recency 30-60 ngày | Cao | Win-back campaign ngay |
> | Hibernating | Recency > 90 ngày | Rất cao | Unsubscribe hoặc deep discount |

---

## Prompt 06 — AI thiết kế gamification system *(mới)*

**Khi nào dùng:** Muốn thiết kế hoặc cải thiện hệ thống gamification / loyalty để tăng engagement và retention.

```
Tôi muốn thiết kế hệ thống gamification cho:

Sản phẩm: [mô tả — VD: app học tiếng Anh, super app, platform thương mại]
Hành vi muốn thúc đẩy: [VD: daily login, hoàn thành bài học, giới thiệu bạn bè]
User profile: [mô tả — VD: 18-35 tuổi, dùng app 3-4 lần/tuần, drop-off nhiều sau tuần 2]
Hiện tại đang có (nếu có): [VD: hệ thống điểm đơn giản, chưa có streak]

Thiết kế hệ thống gamification:
1. Core loop: hành động → phần thưởng → động lực tiếp tục (cycle cụ thể)
2. Cấu trúc cấp độ: 3-4 level với tên gợi cảm, điều kiện lên cấp, đặc quyền mỗi level
3. Cơ chế giữ chân: streak / loss aversion hoạt động như thế nào
4. Personalization: hệ thống tự điều chỉnh target cho từng user ra sao
5. Re-engagement trigger: AI phát hiện dấu hiệu drop-off và kích hoạt gì
6. Metric để đo gamification hiệu quả (D7 retention, DAU/MAU, streak length)
Trả về dạng sơ đồ flow + bảng cấp độ.
```

**Ví dụ output mong đợi:**
> Level 1 "Người mới" → Level 2 "Thành viên" (7-day streak) → Level 3 "Chuyên gia" (30 ngày + 10 referral). Re-engagement trigger: nếu user không login sau 48h → push "Streak của bạn sắp mất!" (loss aversion > reward-seeking).

---

## English

Prompts to leverage AI in growth marketing. From personalization and segmentation to campaign optimization, predictive analytics, and gamification.

**6 prompts for real-world situations. Fill in the placeholders → paste → get results immediately.**

---

## Prompt 01 — AI personalization

**When to use:** Want AI to suggest how to personalize a campaign per user segment.

```
I want to use AI to personalize this campaign:

Campaign: [description — e.g. 20% voucher for next order]
Segments: [e.g. new user (registered < 7 days), active (ordered in 30 days), dormant (no login > 60 days)]
Channels: [push / email / in-app]
Data available: [behavior / purchase / demographics]

Design a personalization strategy:
1. Different message, offer, timing per segment
2. How AI can auto-adjust offers based on real-time behavior
3. Metrics to measure personalization effectiveness
4. When personalization backfires — what to watch for
```

---

## Prompt 02 — AI campaign analysis

**When to use:** Campaign just ended, want AI analysis instead of reading dashboards.

```
Analyze this campaign performance:

Campaign: [description — e.g. 48h flash sale 30% off]
KPI: [e.g. redemption rate]
Actual: [e.g. 8.2%]
Target: [e.g. 10%]
Duration: [e.g. May 15-16]

Data:
- Redemption by day: [e.g. day 1: 5.1%, day 2: 3.1%]
- Redemption by segment: [e.g. new: 12%, active: 9%, dormant: 2%]
- Cost: [e.g. $2,000, CAC = $4/user]

Please:
1. Overall performance — hit or miss? Why?
2. Best/worst performing segment? Why?
3. Anomalies in the data?
4. 3 specific recommendations for next campaign
Return as summary table + key bullets.
```

---

## Prompt 03 — AI A/B test design

**When to use:** Multiple A/B test ideas, need AI to prioritize and design tests.

```
I want to run A/B tests for:

Campaign: [description]
Current control: [e.g. push at 9am, 20% offer]
Ideas to test: [3-5 ideas — e.g.
  1. Change send time to 7pm
  2. Increase offer to 30% for dormant
  3. Copy change: "Today's deal" → "Only 4 hours left"
  4. Add product image to push]
Available traffic: [e.g. 50,000 users]
Test duration: [e.g. 2 weeks]

Help me:
1. Prioritize which to test first (high impact + easy to implement)
2. Design the test: control vs variant, traffic split, duration
3. Predict outcomes: optimistic / realistic / pessimistic
4. How to measure statistical significance (simple formula)
5. If only 1 variable: which to test first?
```

---

## Prompt 04 — AI outcome prediction

**When to use:** Before launching a campaign, want AI to predict results based on historical data.

```
Predict results for my upcoming campaign based on past data.

New campaign: [description]
Budget: [number]
Target segment: [description]
Channels: [list]

Historical data (last 3 campaigns):
- Campaign A: [brief + metrics — e.g. March flash sale, redemption 9.5%, CAC $3.5]
- Campaign B: [brief + metrics]
- Campaign C: [brief + metrics]

Predict:
1. Expected redemption rate (pessimistic / realistic / optimistic range)
2. Best/worst performing segments
3. Key risks based on past patterns
4. Adjustments to increase success probability
```

---

## Prompt 05 — AI churn analysis & segmentation *(new)*

**When to use:** Want AI to analyze behavioral data to identify high-churn segments and suggest interventions.

```
I need churn risk analysis and segmentation for my user base.

Product: [e.g. food delivery app, monthly subscription]
Total active users: [number]

Behavioral data (describe or paste CSV):
- Frequency: [e.g. logins / orders in last 30 days]
- Recency: [e.g. last login / order date]
- Monetary: [e.g. total spend in 90 days]
- Engagement signals: [e.g. push open rate, feature usage]

Please:
1. Group users into 4-5 segments based on the data above (give each a memorable name)
2. For each segment: key traits, estimated % of users, churn risk level
3. Which segments need intervention in the next 30 days?
4. For each high-churn segment: suggest 1 specific action (message, offer, or flow)
5. Which leading indicators should be tracked weekly for early churn detection?
Return as segment table + action plan.
```

---

## Prompt 06 — AI gamification design *(new)*

**When to use:** Designing or improving a gamification / loyalty system to increase engagement and retention.

```
I want to design a gamification system for:

Product: [e.g. language learning app, super app, e-commerce platform]
Behaviors to encourage: [e.g. daily login, lesson completion, referrals]
User profile: [e.g. 18-35, uses app 3-4x/week, high drop-off after week 2]
Current system (if any): [e.g. simple points, no streaks]

Design the gamification system:
1. Core loop: action → reward → motivation to continue (specific cycle)
2. Level structure: 3-4 levels with memorable names, upgrade conditions, perks per level
3. Retention mechanism: how streak / loss aversion works specifically
4. Personalization: how the system auto-adjusts targets per user
5. Re-engagement trigger: how AI detects drop-off signals and what it activates
6. Metrics to measure effectiveness (D7 retention, DAU/MAU, streak length)
Return as flow diagram + levels table.
```

---

## Prompt 07 — AI explains how RAG works in campaign targeting *(new)*

**When to use:** Want to understand AI retrieval mechanics to design better campaign targeting, or explain to your team why the personalization engine behaves the way it does.

```
Explain how RAG (Retrieval-Augmented Generation) relates to campaign targeting, using TF-IDF as a concrete example.

My context:
- Campaign pool: [describe size and types — e.g. 20 campaigns: cashback / gamification / referral / urgency]
- User segments: [e.g. new user, active, dormant, high-value]
- Current targeting approach: [e.g. rule-based, manual, ML model]

Explain:
1. What TF-IDF is and how it "matches" users to campaigns (with examples from my campaigns)
2. How RAG differs from TF-IDF — embeddings understand semantics, TF-IDF understands exact terms
3. Why "user who likes games" can match "gamification spin wheel" even without using that word
4. When TF-IDF is enough vs. when you need embeddings / RAG
5. Simplest possible Python code example illustrating the concept (< 30 lines)
```

**Note:** If AI returns 0% score across all campaigns, the query uses terms entirely outside the corpus — review how you describe campaigns or segments.

---

## Prompt 08 — Build a mini campaign search engine in Python *(new)*

**When to use:** Want to build a tool to match user segments with the best-fit campaigns, no ML framework, pure Python only.

```
Help me build a mini campaign search engine in pure Python (no sklearn or ML libraries).

My campaign pool:
[Paste campaign list in this format:
- Name: [campaign name]
  Description: [keywords describing mechanic, offer, target — e.g. cashback refund shopping voucher]
]

Segment queries to match:
[e.g.
- New user: "streak check-in points accumulation new users"
- Churned: "winback reactivation lapsed users offer"
- High-value: "vip loyalty premium exclusive tier"
]

Build an engine with:
1. TF-IDF from scratch — explain each step: TF, IDF, score
2. search(query, top_k=3) returning best-fit campaigns with relevance %
3. IDF analysis — which terms are most specific in my pool
4. Edge case: handle when query matches no campaign (score = 0)
5. Comments explaining each code block in marketer language

Expected output: runnable code with results like:
Segment: Churned 60 days
  -> Winback churned users   100%  ######################
  -> VIP loyalty tier         27%  ######
```

