# 09 · AI × Growth Marketing — Prompt Ứng Dụng AI

## Tiếng Việt

Prompt để tận dụng AI trong growth marketing. Từ personalization, segmentation, campaign optimization đến predictive analytics và gamification.

**11 prompt theo tình huống thực tế. Điền placeholder → paste → lấy kết quả ngay.**

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

**11 prompts for real-world situations. Fill in the placeholders → paste → get results immediately.**

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

---

## Prompt 09 — AI thiết kế growth agent tự động *(mới)*

**Khi nào dùng:** Muốn build một AI agent tự động chạy growth task (monitor, phân tích, gợi ý) mà không cần đội ML riêng.

```
Tôi muốn thiết kế AI agent cho growth marketing.

Mục tiêu: [VD: agent tự động theo dõi campaign performance hằng ngày]
Input có sẵn: [VD: Google Sheet campaign data, dashboard export CSV]
Output mong đợi: [VD: báo cáo tóm tắt + cảnh báo nếu KPI dưới target]
Kênh output: [Telegram / Slack / email / Google Doc]

Agent workflow:
1. Trigger: [VD: chạy mỗi sáng 8:00 / chạy khi có data mới / chạy manual]
2. Data fetch: agent đọc từ đâu? Format gì?
3. Analysis: AI phân tích gì? So sánh với gì?
4. Decision: khi nào agent tự quyết định mà không cần hỏi?
5. Output: format output ra sao? Kênh nào?

Hãy thiết kế:
1. Agent architecture: các component cần có (trigger → fetch → analyze → decide → output)
2. AI prompt cho analysis step — viết sẵn, chỉ cần paste
3. Edge cases: khi data thiếu, khi output lỗi, khi cần human confirmation
4. Cách implement: chạy trong n8n / Make / Python script?
5. Scale: từ 1 campaign lên 10 campaigns thì cần thay đổi gì?

Nếu implement bằng n8n: xem thêm workflow [02 Campaign Monitor](./10-n8n-growth-workflows/).
```

**Ví dụ output mong đợi:**
> Agent: "Campaign Monitor Bot" — Trigger: 8:00 daily → Fetch Google Sheet → AI compare actual vs target → If 2+ metrics below target: gửi Telegram alert kèm 3 đề xuất fix → If all on track: gửi 1 dòng "Hôm nay OK" vào Slack.

---

## Prompt 10 — AI viết content & script cho campaign *(mới)*

**Khi nào dùng:** Cần content cho campaign — từ caption, script video ngắn, push notification, đến email sequence — muốn AI hỗ trợ viết nhanh theo đúng tone của brand.

```
Tôi cần AI viết content cho campaign sau:

Campaign: [VD: Flash sale 48h — giảm 30% cho đơn hàng đầu]
Target segment: [VD: New user — chưa từng order / gen Z 22-30 tuổi]
Kênh: [push notification / SMS / email / in-app banner / TikTok script]
Tone: [VD: trẻ trung hài hước / chuyên nghiệp đáng tin / urgent FOMO / thân thiện dễ thương]
Sản phẩm/dịch vụ: [VD: app thanh toán di động, voucher shopping]
Giới hạn: [VD: tối đa 150 ký tự cho push, tối đa 60s cho script]

Yêu cầu:
1. Viết 3 biến thể cho mỗi kênh — khác góc tiếp cận (FOMO, lợi ích, hài hước)
2. Có thể A/B test biến thể nào với biến thể nào
3. CTA phù hợp cho mỗi biến thể
4. Nếu là script video: kèm timing (0-3s hook, 3-15s nội dung, 15-20s CTA)

Nếu campaign có emoji/brand guideline, ghi rõ:
- Emoji được dùng: [VD: 🔥 🎉 ⚡]
- Không dùng: [VD: 💰 💵 — quá salesy]
- Hashtag bắt buộc: [VD: #MoMo #FlashSale]
```

**Ví dụ output mong đợi:**
> **Push (150 ký tự):** Variant A (FOMO): "🔥 Còn 12 tiếng — giảm 30% đơn đầu. Chưa có deal này lần 2 đâu. Mở app ngay →"  
> Variant B (Benefit): "🎉 Chào mừng bạn — tặng ngay 30% cho đơn hàng đầu tiên. Không điều kiện, không tối thiểu. Nhận ngay →"  
> **TikTok script (30s):** Hook 0-3s: "Bạn mới à? Có cái này chỉ dành cho bạn thôi..." → Content 3-20s: quay màn hình app, chạm vào voucher → CTA 20-30s: "Quét mã này, giảm 30% — xong. Đơn giản vậy thôi."

---

## Prompt 11 — AI dự đoán churn & đề xuất win-back tự động *(mới)*

**Khi nào dùng:** Có dữ liệu user behavior, muốn AI phân tích churn risk và tự động đề xuất win-back strategy cho từng nhóm, kết hợp output với n8n workflow.

```
Tôi muốn build hệ thống churn detection + win-back tự động.

Dữ liệu user có sẵn:
- User ID, ngày đăng ký, ngày active cuối cùng
- Số lần order/transaction trong 30 / 60 / 90 ngày
- Tổng chi tiêu (VND)
- Push open rate (nếu có)
- Tính năng đã dùng (nếu có)
- Segment hiện tại: [new / active / dormant / vip]

Cấu hình campaign:
- Win-back budget: [VD: 50 triệu / tháng]
- Kênh có thể dùng: [push / SMS / email / in-app]
- Offer có thể dùng: [VD: voucher giảm giá, voucher freeship, tích điểm thêm, event exclusive]

Hãy thiết kế churn detection + win-back system:
1. Phân loại user thành 5 mức churn risk — từ "đang rất ổn" đến "sắp mất"
   - Mỗi mức: dấu hiệu nhận biết, % user dự kiến, thời gian còn lại để can thiệp
2. Với mỗi mức churn risk: đề xuất win-back strategy cụ thể:
   - Offer gì? Timing nào? Kênh nào? Message thế nào?
   - Chi phí ước tính mỗi user
   - Expected win-back rate (optimistic / realistic)
3. AI threshold: khi nào AI tự động trigger win-back, khi nào cần human approve
4. Feedback loop: sau khi gửi win-back, làm sao đo được hiệu quả
5. Tích hợp n8n: workflow nào trong folder 10 có thể dùng?

Nếu có thể: thiết kế luôn một bảng quyết định (decision matrix) đơn giản.
```

**Ví dụ output mong đợi:**
> | Risk Level | Dấu hiệu | Còn | Offer | Channel | Budget/user | Win-back rate |
> |---|---|---|---|---|---|---|
> | 🔴 Critical | Không login > 60 ngày | 7-14 ngày | 50% voucher | SMS + Push | 25k | 12-18% |
> | 🟡 Medium | Login nhưng không order > 30 ngày | 30 ngày | Freeship + 20% | Push + In-app | 10k | 20-30% |
> | 🟢 Low | Active đều, open push thấp | 60+ ngày | Loyalty điểm thưởng | In-app banner | 5k | 35-45% |

---

## English

---

## Prompt 07 — AI explains how RAG works in campaign targeting

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

## Prompt 08 — Build a mini campaign search engine in Python

**When to use:** Want to build a tool to match user segments with best-fit campaigns, no ML framework, pure Python only.

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

---

## Prompt 09 — Design an AI growth agent *(new)*

**When to use:** Want to build an AI agent that autonomously runs growth tasks (monitor, analyze, suggest) without needing a dedicated ML team.

```
I want to design an AI agent for growth marketing.

Goal: [e.g. agent that monitors campaign performance daily]
Available input: [e.g. Google Sheet with campaign data, dashboard CSV export]
Expected output: [e.g. summary report + alert if KPI below target]
Output channel: [Telegram / Slack / email / Google Doc]

Agent workflow:
1. Trigger: [e.g. runs daily at 8:00 / runs when new data arrives / manual]
2. Data fetch: where does the agent read from? What format?
3. Analysis: what does AI analyze? Compare against what baseline?
4. Decision: when does the agent decide autonomously vs. ask human?
5. Output: format? Channel?

Design:
1. Agent architecture: components needed (trigger → fetch → analyze → decide → output)
2. AI prompt for the analysis step — write it, ready to paste
3. Edge cases: missing data, output errors, human confirmation needed
4. Implementation: n8n / Make / Python script?
5. Scale: from 1 campaign to 10 campaigns — what changes?
```

---

## Prompt 10 — AI content & script writing for campaigns *(new)*

**When to use:** Need campaign content — from captions, short video scripts, push notifications to email sequences — want AI to write fast in your brand tone.

```
I need AI to write content for this campaign:

Campaign: [e.g. 48h flash sale — 30% off first order]
Target segment: [e.g. new users / Gen Z 22-30]
Channel: [push notification / SMS / email / in-app banner / TikTok script]
Tone: [e.g. casual funny / professional trustworthy / urgent FOMO / friendly]
Product/service: [e.g. mobile payment app, shopping voucher]
Limits: [e.g. max 150 chars for push, max 60s for video script]

Requirements:
1. Write 3 variants per channel — different angles (FOMO, benefit, humor)
2. Which variants to A/B test against each other
3. Appropriate CTA per variant
4. If video script: include timing (0-3s hook, 3-15s content, 15-20s CTA)
```

---

## Prompt 11 — AI churn prediction & win-back automation *(new)*

**When to use:** Have user behavioral data, want AI to analyze churn risk and auto-suggest win-back strategy per segment, connected to n8n workflows.

```
I want to build an automated churn detection + win-back system.

Available user data:
- User ID, registration date, last active date
- Transaction count in 30 / 60 / 90 days
- Total spend (VND)
- Push open rate (if available)
- Features used (if available)
- Current segment: [new / active / dormant / vip]

Campaign config:
- Win-back budget: [e.g. $2,000 / month]
- Channels available: [push / SMS / email / in-app]
- Offers available: [e.g. discount voucher, free shipping, bonus points, exclusive event]

Design churn detection + win-back system:
1. Classify users into 5 churn risk levels — from "healthy" to "about to leave"
   - Each level: signals, estimated % of users, remaining intervention window
2. Per risk level: specific win-back strategy:
   - Offer? Timing? Channel? Message?
   - Estimated cost per user
   - Expected win-back rate (optimistic / realistic)
3. AI threshold: when does AI auto-trigger win-back vs. need human approval?
4. Feedback loop: after sending win-back, how to measure effectiveness?
5. n8n integration: which workflows from folder 10 can be used?

If possible: design a simple decision matrix for quick reference.
```

