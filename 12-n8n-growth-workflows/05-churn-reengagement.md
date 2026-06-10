# 05 - Churn Signal + Re-engagement

> Phat hien user co nguy co roi bo, trigger campaign keo ve tu dong.

---

## Khi nao dung

- Ban co data user activity (login, transaction, engagement)
- Muon detect som user sap churn truoc khi ho roi han
- Muon tu dong trigger re-engagement campaign khong can thao tac thu cong

---

## Cach hoat dong

1. Doc user activity (DB/Sheets)
2. AI phat hien churn signal (GPT/Claude)
3. Phan loai risk (IF logic)
4. Trigger campaign (Webhook/API)

---

## Cac node

### Buoc 1: Doc user activity
- Node: Google Sheets / MySQL / PostgreSQL
- Du lieu: user_id, last_active_date, total_sessions_30d, last_transaction, segment, push_optin

### Buoc 2: AI detect churn signal
- Node: OpenAI / Claude
- Prompt:
```
You are a retention analyst. Analyze each user and classify churn risk.

Risk levels:
- HIGH: Not active >14 days, previously active >3 sessions/week
- MEDIUM: Not active >7 days, declining frequency
- LOW: Active within 7 days, stable behavior
- NONE: Active today or yesterday

For HIGH and MEDIUM users, suggest:
1. Churn reason hypothesis (based on behavior pattern)
2. Best re-engagement channel (push, SMS, email)
3. Offer type to bring them back
4. Urgency level (immediate / within 48h / this week)

User data: {{ $json.data }}
Output format: JSON array with user_id, risk_level, hypothesis, channel, offer, urgency
```

### Buoc 3: Phan loai theo risk
- Node: IF / Switch
- HIGH: Gui alert + trigger campaign ngay
- MEDIUM: Them vao queue re-engagement tuan nay
- LOW/NONE: Bo qua, tiep tuc monitor

### Buoc 4: Trigger re-engagement
- Node: Telegram / Slack / HTTP Request (goi API campaign tool)
- Noi dung: "User [id] - HIGH churn risk. Recommend: [offer] via [channel] within [urgency]"

---

## Vi du output

CHURN ALERT -- May 16, 2026

HIGH RISK (triggered immediately):
- user_48392 - Khong active 18 ngay
  > Hypothesis: Het voucher, khong thay gia tri quay lai
  > Action: Push "Voucher 5k cho ban" + SMS reminder
  > Urgency: Ngay trong hom nay

- user_10234 - Tung active 5x/tuan, giam con 0
  > Hypothesis: Chuyen sang app khac
  > Action: Offer dac biet "Giam 15k cho lan booking dau"
  > Urgency: Trong 24h

MEDIUM RISK (queue this week):
- user_77102 - 9 ngay khong active, frequency giam 40%
  > Hypothesis: Ban, khong co nhu cau
  > Action: Push reminder nhe + personalized content
  > Urgency: Trong tuan nay

Total scanned: 50,000 users
HIGH: 142 users | MEDIUM: 893 users | LOW: 2,104 users

---

*Truoc: Campaign Brief Generator*
*Sau: Quay lai README*
