# 05 â€” Churn Signal + Re-engagement

> PhÃ¡t hiá»‡n user cÃ³ nguy cÆ¡ rá»i bá», trigger campaign kÃ©o vá» tá»± Ä‘á»™ng.

---

## Khi nÃ o dÃ¹ng

- Báº¡n cÃ³ data user activity (login, transaction, engagement)
- Muá»‘n detect sá»›m user sáº¯p churn trÆ°á»›c khi há» rá»i háº³n
- Muá»‘n tá»± Ä‘á»™ng trigger re-engagement campaign khÃ´ng cáº§n can thiá»‡p thá»§ cÃ´ng

---

## CÃ¡ch hoáº¡t Ä‘á»™ng

```
1. Äá»c user activity  â†’  2. AI phÃ¡t hiá»‡n churn signal  â†’  3. PhÃ¢n loáº¡i risk  â†’  4. Trigger campaign
   (DB/Sheets)            (GPT/Claude)                    (IF logic)          (Webhook/API)
```

---

## CÃ¡c node

### BÆ°á»›c 1: Äá»c user activity
- **Node:** Google Sheets / MySQL / PostgreSQL
- **Dá»¯ liá»‡u:** `user_id`, `last_active_date`, `total_sessions_30d`, `last_transaction`, `segment`, `push_optin`

### BÆ°á»›c 2: AI detect churn signal
- **Node:** OpenAI / Claude
- **Prompt:**
```
You are a retention analyst. Analyze each user and classify churn risk:

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

### BÆ°á»›c 3: PhÃ¢n loáº¡i theo risk
- **Node:** IF / Switch
- **HIGH:** Gá»­i alert + trigger campaign ngay
- **MEDIUM:** ThÃªm vÃ o queue re-engagement tuáº§n nÃ y
- **LOW/NONE:** Bá» qua, tiáº¿p tá»¥c monitor

### BÆ°á»›c 4: Trigger re-engagement
- **Node:** Telegram / Slack / HTTP Request (gá»i API campaign tool)
- **Ná»™i dung:** "User [id] - HIGH churn risk. Recommend: [offer] via [channel] within [urgency]"

---

## VÃ­ dá»¥ output

```
ðŸš¨ CHURN ALERT â€” May 16, 2026

HIGH RISK (triggered immediately):
â€¢ user_48392 - KhÃ´ng active 18 ngÃ y
  â†’ Hypothesis: Háº¿t voucher, khÃ´ng tháº¥y giÃ¡ trá»‹ quay láº¡i
  â†’ Action: Push "Voucher 5k chá» báº¡n" + SMS reminder
  â†’ Urgency: Ngay trong hÃ´m nay

â€¢ user_10234 - Tá»«ng active 5x/tuáº§n, giáº£m cÃ²n 0
  â†’ Hypothesis: Chuyá»ƒn sang Ä‘á»‘i thá»§ / app khÃ¡c
  â†’ Action: Offer Ä‘áº·c biá»‡t "Giáº£m 15k cho láº§n booking Ä‘áº§u"
  â†’ Urgency: Trong 24h

MEDIUM RISK (queue this week):
â€¢ user_77102 - 9 ngÃ y khÃ´ng active, frequency giáº£m 40%
  â†’ Hypothesis: Báº­n, khÃ´ng cÃ³ nhu cáº§u gáº§n Ä‘Ã¢y
  â†’ Action: Push reminder nháº¹ + ná»™i dung personalized
  â†’ Urgency: Trong tuáº§n nÃ y

Total scanned: 50,000 users
HIGH: 142 users | MEDIUM: 893 users | LOW: 2,104 users
```

---

*TrÆ°á»›c: [Campaign Brief Generator](./04-campaign-brief-generator.md)*
*Sau: Quay láº¡i [README](./README.md)*
