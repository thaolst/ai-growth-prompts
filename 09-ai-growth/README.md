# AI × Growth Marketing

## Tiếng Việt

AI đang thay đổi growth marketing thế nào — từ personalization quy mô lớn đến automated experimentation. Framework thực tế, không hype.

Bảy phần: personalization, segmentation, campaign optimization, predictive analytics, game mechanics, growth stack, và limitation/rủi ro. Mỗi phần có prompt để thử ngay.

---

## Tại Sao Lại Quan Trọng

- 70% đội growth đã dùng AI để tối ưu campaign
- Cá nhân hóa quy mô lớn là bất khả thi trước khi có AI
- Team nào áp dụng AI-first growth sẽ có lợi thế cấu trúc

---

## 1. AI cho Cá Nhân Hóa (Personalization)

**Điều gì đã thay đổi:**
- Segmentation dựa trên rule → Segmentation dự đoán
- Campaign theo batch → Cá nhân hóa thời gian thực
- Đoán và kiểm tra → Gợi ý dựa trên ML

**Use cases:**
- **Cá nhân hóa nội dung:** Landing page động, gợi ý sản phẩm
- **Tối ưu ưu đãi:** Voucher/giá nào nên hiển thị cho từng người dùng
- **Tối ưu thời điểm:** Giờ gửi thông báo tốt nhất dựa trên hành vi
- **Chọn kênh:** Kênh nào (push, SMS, in-app) hiệu quả cho người dùng nào

**Prompt để thử:**
```
You're a growth marketer. Given user segment [describe], design 3 personalized offer variants. Each variant should target a different motivation: price sensitivity, novelty-seeking, or habit reinforcement.
```

---

## 2. AI cho Phân Khúc (Segmentation)

**Điều gì đã thay đổi:**
- Phân khúc RFM tĩnh → Cụm hành vi động
- Gắn thẻ thủ công → Trích xuất thuộc tính tự động
- Phân khúc lịch sử → Phân khúc dự đoán (ai sẽ rời bỏ, ai sẽ chuyển đổi)

**Use cases:**
- **Dự đoán churn:** Người dùng nào sẽ rời bỏ tháng tới
- **Hành động tốt nhất tiếp theo:** Nên offer gì cho mỗi người dùng ngay lúc này
- **Lookalike modeling:** Tìm thêm người dùng giống phân khúc tốt nhất của bạn
- **Dự đoán vòng đời người dùng:** Người dùng này đang ở đâu trong hành trình?

**Prompt để thử:**
```
Given these user behavior patterns [data], identify the top 3 segments that are most likely to churn next month. For each segment, suggest a one-action intervention (no more than CZK [budget] per user).
```

---

## 3. AI cho Tối Ưu Campaign

**Điều gì đã thay đổi:**
- A/B testing thủ công → Multivariate test tự động tối ưu
- Campaign tĩnh → Phân bổ ngân sách động
- Phân tích sau campaign → Tối ưu thời gian thực

**Use cases:**
- **Phân bổ ngân sách:** Tự động chuyển ngân sách từ kênh kém sang kênh hiệu quả
- **Tối ưu creative:** Tạo và test hàng chục ad creative tự động
- **Tối ưu bid:** Điều chỉnh giá thầu thời gian thực trên kênh trả phí
- **Tối ưu landing page:** Tự động tạo và test biến thể landing page

**Prompt để thử:**
```
Design a campaign optimization flow that: 1) launches 3 creative variants per segment, 2) auto-pauses underperformers after 24h, 3) reallocates budget to the winner, 4) generates a performance report daily. Budget: [amount], timeline: [days].
```

---

## 4. AI cho Phân Tích Dự Đoán (Predictive Analytics)

**Điều gì đã thay đổi:**
- Phân tích phản ứng → Dự báo chủ động
- Báo cáo lịch sử → Phát hiện bất thường thời gian thực
- Trích xuất insight thủ công → Phát hiện mẫu tự động

**Use cases:**
- **Dự đoán LTV:** Dự đoán giá trị vòng đời khách hàng ngay khi đăng ký
- **Dự báo ROI campaign:** Dự đoán hiệu suất campaign trước khi launch
- **Dự báo theo mùa:** Dự đoán nhu cầu dựa trên lịch sử + tín hiệu bên ngoài
- **Phát hiện bất thường:** Nhận cảnh báo khi metric vượt ngoài khoảng dự kiến

**Prompt để thử:**
```
Based on this campaign data [describe], forecast the expected ROI for the next 30 days. Consider seasonality, previous campaign performance, and current market conditions. Highlight the top 3 risk factors.
```

---

## 5. AI × Cơ Chế Game (Game Mechanics)

**Điều gì đã thay đổi:**
- Chương trình loyalty cố định → Gamification động, cá nhân hóa
- Thử thách một-cỡ-cho-tất-cả → Mục tiêu cá nhân hóa

**Use cases:**
- **Mốc động:** Mỗi người dùng thấy mốc được hiệu chỉnh theo hành vi của họ
- **Phần thưởng cá nhân hóa:** Phần thưởng phù hợp với sở thích từng người
- **Độ khó thích ứng:** Thử thách khó dần khi người dùng lên cấp
- **Tái tương tác đúng lúc:** AI phát hiện khi engagement đang giảm và kích hoạt thử thách

**Prompt để thử:**
```
Design a gamification system for [product type] that: 1) personalizes goals per user, 2) uses loss aversion (don't lose your streak) over reward-seeking, 3) has 3 levels with increasing difficulty, 4) triggers re-engagement before user drops off.
```

---

## 6. AI trong Growth Stack

```
+---------------------------------+
|        AI Layer                 |
|  (personalization, prediction,   |
|   optimization, generation)     |
+---------------------------------+
|      Growth Stack               |
|  (analytics, campaigns,          |
|   CRM, testing tools)           |
+---------------------------------+
|      Data Infrastructure        |
|  (CDP, data warehouse, event     |
|   tracking)                     |
+---------------------------------+
```

**Nguyên tắc chính:** AI bổ trợ, không thay thế growth stack. Chất lượng dữ liệu quyết định chất lượng đầu ra của AI.

---

## 7. Giới Hạn & Rủi Ro

- **Phụ thuộc dữ liệu:** Rác vào = rác ra. AI cần dữ liệu sạch, có cấu trúc.
- **Quyền riêng tư:** Cá nhân hóa cần dữ liệu. Cân bằng giữa cá nhân hóa và tuân thủ quyền riêng tư.
- **Thiên kiến:** Mô hình ML có thể khuếch đại thiên kiến có sẵn trong dữ liệu.
- **Tự động hóa quá mức:** AI tối ưu tốt trong các mẫu đã biết nhưng khó với chiến lược mới.
- **Chi phí:** Chi phí hạ tầng AI là thực tế. Bắt đầu nhỏ, chứng minh giá trị, rồi mở rộng.

---

## Tiếp Theo Là Gì

- Agentic AI cho growth (AI có thể tự thực thi campaign đa bước)
- Hyper-personalization thời gian thực ở cấp độ từng người dùng
- Đội growth native AI nơi AI xử lý 80% thực thi chiến thuật

---

*Xem các prompt thực hành AI × Growth ở các folder khác — đặc biệt là [01-voucher-design](../01-voucher-design) và [03-game-mechanics](../03-game-mechanics).*

---

## English

How AI is reshaping growth marketing - from personalization at scale to automated experimentation. Practical frameworks, not hype.

Seven sections: personalization, segmentation, campaign optimization, predictive analytics, game mechanics, growth stack, and limitations/risks. Each section includes a prompt to try now.

---

## Why This Matters

- 70% of growth teams already use AI for campaign optimization
- Personalization at scale was impossible before AI
- The teams that adopt AI-first growth will have a structural advantage

---

## 1. AI for Personalization

**What's changed:**
- Rule-based segmentation → Predictive segmentation
- Batch campaigns → Real-time personalization
- Guess-and-check → ML-powered recommendation

**Use cases:**
- **Content personalization:** Dynamic landing pages, product recommendations
- **Offer optimization:** What voucher/price to show each user
- **Timing optimization:** Best send time for notifications based on behavior patterns
- **Channel selection:** Which channel (push, SMS, in-app) works for which user

**Prompt to try:**
```
You're a growth marketer. Given user segment [describe], design 3 personalized offer variants. Each variant should target a different motivation: price sensitivity, novelty-seeking, or habit reinforcement.
```

---

## 2. AI for Segmentation

**What's changed:**
- Static RFM segments → Dynamic behavioral clusters
- Manual tagging → Automated attribute extraction
- Historical segments → Predictive segments (who will churn, who will convert)

**Use cases:**
- **Churn prediction:** Which users will drop off next month
- **Next best action:** What to offer each user right now
- **Lookalike modeling:** Find more users like your best segment
- **User lifecycle prediction:** Where is this user in their journey?

**Prompt to try:**
```
Given these user behavior patterns [data], identify the top 3 segments that are most likely to churn next month. For each segment, suggest a one-action intervention (no more than CZK [budget] per user).
```

---

## 3. AI for Campaign Optimization

**What's changed:**
- Manual A/B testing → Auto-optimized multivariate tests
- Static campaigns → Dynamic budget allocation
- Post-campaign analysis → Real-time optimization

**Use cases:**
- **Budget allocation:** Auto-shift budget from underperforming to overperforming channels
- **Creative optimization:** Generate and test dozens of ad creatives automatically
- **Bid optimization:** Real-time bid adjustment in paid channels
- **Landing page optimization:** Auto-generate and test landing page variants

**Prompt to try:**
```
Design a campaign optimization flow that: 1) launches 3 creative variants per segment, 2) auto-pauses underperformers after 24h, 3) reallocates budget to the winner, 4) generates a performance report daily. Budget: [amount], timeline: [days].
```

---

## 4. AI for Predictive Analytics

**What's changed:**
- Reactive analysis → Predictive forecasting
- Historical reporting → Real-time anomaly detection
- Manual insight extraction → Automated pattern discovery

**Use cases:**
- **LTV prediction:** Predict customer lifetime value at sign-up
- **Campaign ROI forecast:** Predict campaign performance before launch
- **Seasonal prediction:** Forecast demand based on historical + external signals
- **Anomaly detection:** Get alerted when a metric moves outside expected range

**Prompt to try:**
```
Based on this campaign data [describe], forecast the expected ROI for the next 30 days. Consider seasonality, previous campaign performance, and current market conditions. Highlight the top 3 risk factors.
```

---

## 5. AI x Game Mechanics

**What's changed:**
- Fixed loyalty programs → Dynamic, personalized gamification
- One-size-fits-all challenges → Individualized goals

**Use cases:**
- **Dynamic milestones:** Each user sees milestones calibrated to their behavior
- **Personalized rewards:** Rewards that match each user's preferences
- **Adaptive difficulty:** Challenges that get harder as users level up
- **Re-engagement at the right time:** AI detects when engagement is dropping and triggers a challenge

**Prompt to try:**
```
Design a gamification system for [product type] that: 1) personalizes goals per user, 2) uses loss aversion (don't lose your streak) over reward-seeking, 3) has 3 levels with increasing difficulty, 4) triggers re-engagement before user drops off.
```

---

## 6. AI in the Growth Stack

```
+---------------------------------+
|        AI Layer                 |
|  (personalization, prediction,   |
|   optimization, generation)     |
+---------------------------------+
|      Growth Stack               |
|  (analytics, campaigns,          |
|   CRM, testing tools)           |
+---------------------------------+
|      Data Infrastructure        |
|  (CDP, data warehouse, event     |
|   tracking)                     |
+---------------------------------+
```

**Key principle:** AI augments, not replaces, the growth stack. Data quality determines AI output quality.

---

## 7. Limitations & Risks

- **Data dependency:** Garbage in = garbage out. AI needs clean, structured data.
- **Privacy:** Personalization requires data. Balance personalization with privacy compliance.
- **Bias:** ML models can amplify existing biases in your data.
- **Over-automation:** AI can optimize within known patterns but struggles with novel strategies.
- **Cost:** AI infrastructure costs are real. Start small, prove value, scale.

---

## What's Next

- Agentic AI for growth (AI that can execute multi-step campaigns autonomously)
- Real-time hyper-personalization at the individual user level
- AI-native growth teams where AI handles 80% of tactical execution

---

*For practical AI × Growth prompts, see the other folders in this repo - especially [01-voucher-design](../01-voucher-design) and [03-game-mechanics](../03-game-mechanics).*
