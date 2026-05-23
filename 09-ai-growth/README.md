# AI × Growth Marketing

## Tiếng Việt

AI đang thay đổi growth marketing thế nào — từ personalization quy mô lớn đến automated experimentation. Framework thực tế, không hype.

---

## 🚀 Cách Dùng Repo Này

### Bước 1 — Chọn đúng prompt theo tình huống

| Bạn đang cần... | Dùng prompt |
|---|---|
| Cá nhân hóa campaign cho từng nhóm user | `SKILL.md` → Prompt 01 |
| Phân tích kết quả campaign vừa chạy xong | `SKILL.md` → Prompt 02 |
| Thiết kế A/B test, không biết test gì trước | `SKILL.md` → Prompt 03 |
| Dự đoán kết quả trước khi launch campaign | `SKILL.md` → Prompt 04 |
| Phân khúc user, dự đoán ai sắp churn | `SKILL.md` → Prompt 05 |
| Thiết kế hệ thống gamification | `SKILL.md` → Prompt 06 |

### Bước 2 — Điền vào placeholder

Mỗi prompt có các ô `[như thế này]`. Điền thông tin thực của bạn vào trước khi paste vào ChatGPT / Claude.

**Ví dụ cụ thể:**
```
# Thay vì để nguyên:
Segments: [VD: new user, active user, dormant user]

# Điền thực tế của bạn:
Segments: new user (đăng ký < 7 ngày), active user (order trong 30 ngày), dormant (không login > 60 ngày)
```

### Bước 3 — Đọc output và lặp lại

AI sẽ trả về phân tích hoặc đề xuất. Nếu chưa đủ chi tiết, hỏi tiếp ngay trong cùng cuộc trò chuyện — không cần paste lại prompt từ đầu.

**Tip:** Càng nhiều dữ liệu thực → output càng sát thực tế. Paste CSV, số liệu dashboard, hoặc mô tả cụ thể thay vì để trống placeholder.

---

## Tại Sao AI Quan Trọng Với Growth

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

→ **Dùng:** `SKILL.md` Prompt 01

---

## 2. AI cho Phân Khúc (Segmentation)

**Điều gì đã thay đổi:**
- Phân khúc RFM tĩnh → Cụm hành vi động
- Gắn thẻ thủ công → Trích xuất thuộc tính tự động
- Phân khúc lịch sử → Phân khúc dự đoán (ai sẽ rời bỏ, ai sẽ chuyển đổi)

**Use cases:**
- **Dự đoán churn:** Người dùng nào sẽ rời bỏ tháng tới
- **Hành động tốt nhất tiếp theo:** Nên offer gì cho mỗi người dùng ngay lúc này
- **Lookalike modeling:** Tìm thêm người dùng giống phân khúc tốt nhất
- **Dự đoán vòng đời:** Người dùng này đang ở đâu trong hành trình?

→ **Dùng:** `SKILL.md` Prompt 05

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

→ **Dùng:** `SKILL.md` Prompt 02, 03

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

→ **Dùng:** `SKILL.md` Prompt 04

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

→ **Dùng:** `SKILL.md` Prompt 06

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
- **Quyền riêng tư:** Cá nhân hóa cần dữ liệu. Cân bằng giữa cá nhân hóa và tuân thủ privacy.
- **Thiên kiến:** Mô hình ML có thể khuếch đại thiên kiến có sẵn trong dữ liệu.
- **Tự động hóa quá mức:** AI tối ưu tốt trong mẫu đã biết nhưng khó với chiến lược mới.
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

How AI is reshaping growth marketing — from personalization at scale to automated experimentation. Practical frameworks, not hype.

---

## 🚀 How to Use This Repo

### Step 1 — Pick the right prompt for your situation

| You need to... | Use prompt |
|---|---|
| Personalize a campaign per user segment | `SKILL.md` → Prompt 01 |
| Analyze results of a campaign that just ended | `SKILL.md` → Prompt 02 |
| Design A/B tests, unsure what to prioritize | `SKILL.md` → Prompt 03 |
| Predict campaign results before launch | `SKILL.md` → Prompt 04 |
| Segment users, predict who will churn | `SKILL.md` → Prompt 05 |
| Design a gamification system | `SKILL.md` → Prompt 06 |

### Step 2 — Fill in the placeholders

Each prompt has `[placeholders like this]`. Fill in your real data before pasting into ChatGPT / Claude.

**Example:**
```
# Instead of leaving it blank:
Segments: [e.g. new user, active user, dormant user]

# Fill in your actual data:
Segments: new user (registered < 7 days), active user (ordered in last 30 days), dormant (no login > 60 days)
```

### Step 3 — Read the output and iterate

AI will return analysis or recommendations. If you need more detail, ask follow-up questions in the same conversation — no need to paste the full prompt again.

**Tip:** More real data = more accurate output. Paste CSVs, dashboard numbers, or specific descriptions instead of leaving placeholders empty.

---

## Why This Matters

- 70% of growth teams already use AI for campaign optimization
- Personalization at scale was impossible before AI
- Teams that adopt AI-first growth will have a structural advantage

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

→ **Use:** `SKILL.md` Prompt 01

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

→ **Use:** `SKILL.md` Prompt 05

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

→ **Use:** `SKILL.md` Prompt 02, 03

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

→ **Use:** `SKILL.md` Prompt 04

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

→ **Use:** `SKILL.md` Prompt 06

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
- **Over-automation:** AI optimizes well within known patterns but struggles with novel strategies.
- **Cost:** AI infrastructure costs are real. Start small, prove value, scale.

---

## What's Next

- Agentic AI for growth (AI that can execute multi-step campaigns autonomously)
- Real-time hyper-personalization at the individual user level
- AI-native growth teams where AI handles 80% of tactical execution

---

*For practical AI × Growth prompts, see the other folders — especially [01-voucher-design](../01-voucher-design) and [03-game-mechanics](../03-game-mechanics).*
