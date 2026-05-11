# 05 · n8n Workflow Blueprint — AI-Powered Automated Alerting

## Nguồn

Workflow này từ [n8n community](https://n8n.io/workflows/12971-search-flights-with-gemini-via-telegram-and-send-serpapi-price-alerts/),
tác giả Nguyen Thieu Toan (Jay Nguyen). Đây là mẫu thiết kế automation
có thể adapt cho growth marketing.

---

## Phân tích kiến trúc workflow

### Tổng quan

Workflow có **2 luồng chính**:

```
┌─────────────────────────────────────┐
│         🔔 Automated Monitoring      │
│  Schedule → SerpAPI → Compare → Send │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│      💬 AI Flight Assistant         │
│  Telegram → Gemini Agent → Search   │
│  → Format → Reply                   │
└─────────────────────────────────────┘
```

### Workflow 1: Automated Monitoring

**Cách hoạt động:**

1. **Trigger**: Schedule (mỗi 7 ngày)
2. **Data**: SerpAPI — search engine results, real-time prices
3. **Logic**: So sánh giá hiện tại với threshold → gửi alert nếu thấp hơn
4. **Output**: Telegram message — thông tin vé rẻ nhất, hãng bay, giờ bay

**Điểm mạnh:**
- Cấu trúc đơn giản (trigger → fetch → compare → output)
- Chi phí thấp (SerpAPI free tier: 500 req/tháng)
- Dễ mở rộng (thêm route, thêm threshold, thêm output channel)

**Điểm yếu:**
- Fixed schedule — không real-time
- Chỉ check 1 route mỗi workflow
- So sánh đơn giản (giá < threshold, không ML-based prediction)

### Workflow 2: AI Flight Assistant

**Cách hoạt động:**

1. **Trigger**: Telegram message từ user
2. **AI Agent**: Gemini model với tool-calling capability
3. **Tools**: SerpAPI search flights (round-trip auto +5 ngày)
4. **Memory**: Session-based conversation context
5. **Output**: Telegram HTML format — thông tin chuyến bay theo ngữ cảnh

**Điểm mạnh:**
- Natural language input (cả VI và EN)
- Context-aware (nhớ lịch sử hỏi trước)
- Tool-calling pattern: AI agent quyết định khi nào gọi API
- Format đẹp (HTML formatting trong Telegram)

**Pattern quan trọng: Tool-calling Agent**

```
User query (NL) → Gemini → decide: cần search không?
  ├─ Không → trả lời trực tiếp
  └─ Có → gọi SerpAPI → parse kết quả → format response
```

Đây là pattern cốt lõi cho bất kỳ AI automation nào:
AI quyết định workflow execution, không phải code cứng.

---

## Tech Stack

| Component | Công cụ | Vai trò |
|-----------|---------|---------|
| Orchestration | n8n | Kết nối luồng, trigger, transform |
| AI/NLU | Google Gemini Flash | Xử lý ngôn ngữ tự nhiên, tool-calling |
| Data source | SerpAPI (Google Flights) | Real-time search results |
| Interface | Telegram Bot | Input/output của user |
| Schedule | n8n Cron | Trigger định kỳ |
| Memory | n8n Memory Node | Session-based context |

---

## Adapt cho Growth Marketing

Pattern này có thể adapt cho nhiều use case marketing:

### 1. Competitor Promotion Monitor

```
Thay vì track giá vé máy bay → track khuyến mãi đối thủ
```

- **Trigger**: Schedule daily
- **Data**: SerpAPI tìm "tên đối thủ + khuyến mãi + tháng này"
- **Compare**: So sánh với threshold (VD: "giảm > 30% → alert")
- **Output**: Telegram/Slack notify marketing team

**Prompt để build workflow này:**

```
Mô tả use case cho AI agent:

Tôi cần một workflow theo dõi khuyến mãi của đối thủ cạnh tranh.

Yêu cầu:
- Chạy mỗi ngày lúc 8:00
- Search "tên công ty + khuyến mãi + tháng [hiện tại]"
- Phân tích kết quả: đối thủ nào, giảm bao nhiêu %, kênh nào
- So sánh với campaign hiện tại của tôi
- Gửi alert nếu giảm > 30% hoặc có hình thức promotion mới

Output format:
━━━━━━━━━━━━━━━━━━━━━━
📊 COMPETITOR ALERT
Đối thủ: Shopee
Deal: Free ship 0đ + giảm 50K
Kênh: In-app banner + push
So với chúng ta: cao hơn 20%
━━━━━━━━━━━━━━━━━━━━━━
```

### 2. Campaign Performance Monitor

- **Trigger**: Schedule hourly trong thời gian campaign chạy
- **Data**: Internal dashboard API hoặc Google Sheets
- **Compare**: Actual vs target (CTR < X%, redemption rate < Y%)
- **Output**: Alert nếu metric xuống dưới threshold

### 3. Customer Feedback Intelligence

- **Trigger**: Webhook từ app review / social mention
- **AI Agent**: Gemini phân tích sentiment, extract issue
- **Output**: Alert nếu negative sentiment spike > threshold

---

## Marketing Alert Workflow — Full Prompt

**Khi nào dùng:** Bạn muốn xây automation monitor — giá đối thủ,
campaign performance, hoặc bất kỳ metric nào cần real-time alert.

```
Thiết kế workflow automation cho growth marketing monitoring.

Tech stack có sẵn:
- n8n (automation hub)
- Gemini API (AI + tool-calling)
- SerpAPI (search & public data)
- Telegram / Slack (output)
- Google Sheets (data storage)

Use case: [competitor monitoring / campaign tracking / feedback alert / other]

Yêu cầu monitoring:
- Frequency: [daily / hourly / real-time]
- Data source: [SerpAPI / internal API / Google Sheets]
- Threshold: [điều kiện trigger alert — VD: giá drop > 10%]
- Output channel: [Telegram / Slack / email]

Phân tích và đề xuất:
1. Kiến trúc workflow (trigger → fetch → compare → output)
2. Cần mấy workflow? (scheduled vs interactive)
3. Error handling (API fail, timeout, parse error)
4. Cost estimate mỗi tháng (API calls x price)
5. Cách scale khi cần thêm route / kênh
```

**Ví dụ output mong đợi:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WORKFLOW DESIGN: Competitor Promotion Monitor

KIẾN TRÚC
──────────
Workflow 1 · Scheduled Scanner (daily 8AM)
  Schedule → SerpAPI → Parse → Compare → Alert
                                      ↗
Workflow 2 · Trend History ← Google Sheets
  (lưu lịch sử để detect trend)

CHI PHÍ
───────
- n8n: self-hosted (free)
- SerpAPI: 500 calls/tháng (100 search = monitoring daily 3 routes)
- Gemini Flash: ~$0.15/tháng
- Total: ~$0.15/tháng (nếu chỉ tracking)

SCALE
─────
10 routes → $1-2/tháng
Thêm Slack → free
Thêm sentiment analysis → thêm Gemini token cost
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Tự build workflow này

Nếu Thảo muốn tự chạy:

1. **Cài n8n**: Docker hoặc n8n.cloud
2. **Tạo API keys**:
   - SerpAPI: serpapi.com (500 free/tháng)
   - Gemini: aistudio.google.com (free tier)
   - Telegram Bot: @BotFather
3. **Import template** từ [n8n.io template](https://n8n.io/workflows/12971-search-flights-with-gemini-via-telegram-and-send-serpapi-price-alerts/)
4. **Adapt**: sửa SerpAPI params từ flight search → marketing search
5. **Test** với 1 route, sau đó scale

---

*Reference: "Search flights with Gemini via Telegram and send SerpAPI price alerts" — by Nguyen Thieu Toan (n8n community template)*
