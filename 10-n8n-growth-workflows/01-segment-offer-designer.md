# 01 - Segment + Offer Designer

> Tá»± Ä‘á»™ng phÃ¢n nhÃ³m user vÃ  thiáº¿t káº¿ offer theo tá»«ng segment báº±ng AI.

---

## Khi nÃ o dÃ¹ng

- Báº¡n cÃ³ data user trong spreadsheet hoáº·c database
- Cáº§n design offer khÃ¡c nhau cho tá»«ng nhÃ³m user
- Muá»‘n AI gá»£i Ã½ offer dá»±a trÃªn hÃ nh vi thá»±c táº¿, khÃ´ng pháº£i phá»ng Ä‘oÃ¡n

---

## CÃ¡ch hoáº¡t Ä‘á»™ng

```
1. Äá»c data user   2. AI phÃ¢n nhÃ³m     3. AI design offer   4. Xuáº¥t ra sheet
   (Sheets/DB)        (GPT/Claude)         (GPT/Claude)         (Google Sheet)
```

---

## CÃ¡c node (tá»«ng bÆ°á»›c)

### BÆ°á»›c 1: Äá»c dá»¯ liá»‡u user
- **Node:** Google Sheets / MySQL / PostgreSQL
- **Input:** User data gá»“m cÃ¡c cá»™t: `user_id`, `last_activity`, `total_spend`, `frequency`, `segment_history`
- **Máº«u:** Tá»‘i thiá»ƒu 100-1000 user Ä‘á»ƒ phÃ¢n nhÃ³m cÃ³ Ã½ nghÄ©a

### BÆ°á»›c 2: AI phÃ¢n nhÃ³m (segmentation)
- **Node:** OpenAI / Claude
- **Prompt (English for AI):**
```
You are a growth marketing analyst. Segment these users into 3-5 groups based on:
- Recency (last activity)
- Frequency of engagement
- Monetary value (total spend)

For each segment, provide:
1. Segment name (4 words max)
2. Key behavioral traits (3 bullet points)
3. Recommended offer type (discount, cashback, reward, freebie)
4. Recommended offer value (low/medium/high)
5. Expected conversion rate (%)

User data: {{ $json.data }}
```

### BÆ°á»›c 3: AI thiáº¿t káº¿ offer
- **Node:** OpenAI / Claude
- **Prompt:**
```
You are a voucher/campaign designer. For this segment, design 3 offer variants:

Segment: {{ $json.segment_name }}
Traits: {{ $json.traits }}

Each variant must include:
1. Offer name (catchy, 6 words max)
2. Offer mechanics (exactly how it works)
3. Value proposition (why user should care)
4. CAC estimate (low/medium)
5. Urgency mechanic (time limit, limited quantity)

Budget constraint: Low cost per user (~2k VND or equivalent)
```

### BÆ°á»›c 4: Xuáº¥t káº¿t quáº£
- **Node:** Google Sheets
- **Output columns:** `segment_name`, `traits`, `offer_variant_1`, `offer_variant_2`, `offer_variant_3`, `recommended_action`

---

## HÆ°á»›ng dáº«n setup

1. Táº¡o Google Sheet chá»©a data user
2. Add OpenAI API key vÃ o n8n credentials
3. Import workflow JSON
4. Config Sheet ID + range á»Ÿ BÆ°á»›c 1
5. Cháº¡y thá»­ manual trÆ°á»›c, sau Ä‘Ã³ schedule hÃ ng tuáº§n

---

## VÃ­ dá»¥ output

| Segment | Äáº·c Ä‘iá»ƒm | Offer 1 | Offer 2 | Chá»n |
|---|---|---|---|---|
| High-value Lapsed | Active 6mo trÆ°á»›c, spent >500k, ngÆ°ng | Giáº£m 15k cho booking Ä‘áº§u | Táº·ng 5k Xu + free ship | Offer 1 |
| New Low-frequency | Active <3mo, spent <100k, 1-2 láº§n mua | Free ship 0Ä‘ cho Ä‘Æ¡n 20k+ | Giáº£m 5k hoÃ¡ Ä‘Æ¡n 50k+ | Offer 1 |
| Frequent DXTT User | Active thÃ¡ng nÃ y, DXTT 3x+ | Táº·ng 3k Xu booking tiáº¿p | Giáº£m 10k DXTT tiáº¿p | Offer 2 |

---

## Máº¹o custom

- **Lá»‹ch cháº¡y:** HÃ ng tuáº§n hoáº·c 2 tuáº§n/láº§n
- **Segment:** Äiá»u chá»‰nh AI prompt theo sáº£n pháº©m cá»§a báº¡n (DXTT, e-commerce, travel...)
- **Offer variants:** Cháº¡y A/B test Ä‘á»ƒ validate gá»£i Ã½ cá»§a AI
- **Data source:** Thay Google Sheets báº±ng SQL/API cho real-time

---

*Káº¿ tiáº¿p: [Campaign Monitor + Alert](./02-campaign-monitor.md)*
