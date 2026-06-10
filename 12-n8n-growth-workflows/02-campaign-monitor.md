# 02 - Campaign Monitor + Alert

> Kiem tra metric campaign hang ngay, phat hien bat thuong, gui canh bao, tu dong tao report.

---

## Khi nao dung

- Ban dang chay campaign va can biet ngay neu co van de
- Muon co daily snapshot ma khong can kiem tra thu cong
- Muon AI phan tich xu huong va goi y hanh dong

---

## Cach hoat dong

1. Lay metrics (DB/API)
2. AI phan tich (GPT/Claude)
3. Xac dinh trang thai (logic node)
4. Canh bao + report (Telegram/Slack + Sheets)

---

## Cac node

### Buoc 1: Lay campaign metrics
- Node: Google Sheets / MySQL / PostgreSQL / HTTP Request
- Input: date, impressions, clicks, conversions, spend, revenue, segment, channel
- Data range: 7 ngay gan nhat de phan tich trend

### Buoc 2: AI phan tich
- Node: OpenAI / Claude
- Prompt:
```
You are a campaign analyst. Analyze these metrics and provide:
1. Overall status: Green (on track) / Yellow (caution) / Red (critical)
2. Key changes vs previous period (D-7, D-1)
3. Top 3 anomalies detected
4. Recommended actions (max 3, be specific)

Metrics: {{ $json.metrics }}

Campaign constraints:
- Expected DRR: [XX]%
- Max CPA: [XX] VND
- Daily budget: [XX] VND
```

### Buoc 3: Phan nhanh theo trang thai
- Node: IF/Logic
- Green: daily report. Red/Yellow: urgent alert + action

### Buoc 4: Gui ket qua
- Green: Telegram / Google Sheets -- "Campaign OK. DRR: X%, Spend: X"
- Red/Yellow: Telegram / Slack -- "ALERT: Campaign [name]. DRR dropped X%"

### Buoc 5: Ghi log
- Node: Google Sheets
- Append vao campaign log: date, status, drr, cpa, ai_notes

---

## Vi du output

CAMPAIGN DAILY REPORT -- May 16, 2026

STATUS: Green (on track)

Key metrics:
- DRR: 3.2% (target: 3.0%) OK
- CPA: 1,850 VND (limit: 2,000) OK
- Spend: 45.2M / 50M budget
- Revenue: 1.45B

Anomalies:
- Segment "New Users" CPA tang toi 2,300 VND (+15% vs D-7)
- Channel "SMS" volume giam 30% vs hom qua

Actions:
1. Tam dung SMS campaign cho "New Users"
2. Tang push notification frequency de bu
3. Kiem tra SMS delivery rate voi provider

---

## Setup

1. Tao Google Sheet chua campaign data
2. Add OpenAI + Telegram API keys vao n8n
3. Import workflow JSON
4. Chay thu manual, sau do schedule hang ngay

---

*Truoc: Segment + Offer Designer*
*Ke tiep: A/B Test Analyzer*
