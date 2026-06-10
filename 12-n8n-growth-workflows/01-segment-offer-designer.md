# 01 - Segment + Offer Designer

> Tu dong phan nhom user va thiet ke offer theo tung segment bang AI.

---

## Khi nao dung

- Ban co data user trong spreadsheet hoac database
- Can design offer khac nhau cho tung nhom user
- Muon AI goi y offer dua tren hanh vi thuc te, khong phai phong doan

---

## Cach hoat dong

1. Doc data user (Sheets/DB)
2. AI phan nhom (GPT/Claude)
3. AI design offer (GPT/Claude)
4. Xuat ra sheet (Google Sheet)

---

## Cac node

### Buoc 1: Doc du lieu user
- Node: Google Sheets / MySQL / PostgreSQL
- Input: User data gom cac cot: user_id, last_activity, total_spend, frequency, segment_history
- Mau: Toi thieu 100-1000 user de phan nhom co y nghia

### Buoc 2: AI phan nhom (segmentation)
- Node: OpenAI / Claude
- Prompt:
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

### Buoc 3: AI thiet ke offer
- Node: OpenAI / Claude
- Prompt:
```
You are a voucher/campaign designer. For this segment, design 3 offer variants.

Segment: {{ $json.segment_name }}
Traits: {{ $json.traits }}

Each variant must include:
1. Offer name (catchy, 6 words max)
2. Offer mechanics (exactly how it works)
3. Value proposition (why user should care)
4. CAC estimate (low/medium)
5. Urgency mechanic (time limit, limited quantity)

Budget constraint: Low cost per user (~2k VND)
```

### Buoc 4: Xuat ket qua
- Node: Google Sheets
- Output columns: segment_name, traits, offer_variant_1, offer_variant_2, offer_variant_3, recommended_action

---

## Huong dan setup

1. Tao Google Sheet chua data user
2. Add OpenAI API key vao n8n credentials
3. Import workflow JSON
4. Config Sheet ID + range o Buoc 1
5. Chay thu manual truoc, sau do schedule hang tuan

---

## Vi du output

| Segment | Dac diem | Offer 1 | Offer 2 |
|---|---|---|---|
| High-value Lapsed | Active 6mo truoc, spent >500k, ngung | Giam 15k cho booking dau | Tang 5k Xu + free ship |
| New Low-frequency | Active <3mo, spent <100k | Free ship 0d cho don 20k+ | Giam 5k hoa don 50k+ |
| Frequent DXTT User | Active thang nay, DXTT 3x+ | Tang 3k Xu booking tiep | Giam 10k DXTT tiep |

---

## Meo custom

- Lich chay: Hang tuan hoac 2 tuan/lan
- Segment: Dieu chinh AI prompt theo san pham cua ban
- Offer variants: Chay A/B test de validate goi y cua AI
- Data source: Thay Google Sheets bang SQL/API cho real-time

---

*Ke tiep: Campaign Monitor + Alert*
