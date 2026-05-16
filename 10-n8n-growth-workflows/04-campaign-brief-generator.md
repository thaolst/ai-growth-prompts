# 04 - Campaign Brief Generator

> Input thong tin campaign don gian, AI tao full campaign brief, xuat ra Google Doc + notify team.

---

## Khi nao dung

- Can campaign brief co cau truc nhanh
- Muon consistency giua cac brief
- Muon AI goi y channels, budget allocation, offer types dua tren campaign goals

---

## Cach hoat dong

1. Input campaign info (form/webhook)
2. AI generate brief (GPT/Claude)
3. Output to Google Doc (Google Docs API)
4. Notify team (Slack/Telegram)

---

## Input Form

Tao n8n webhook form hoac Google Form voi cac field:

| Field | Example | Type |
|---|---|---|
| Campaign name | Flash Sale T6 | text |
| Campaign level | S / M / L | dropdown |
| Target segment | MAU T4 chua T5 | text |
| Objective | MAU push / Revenue / Retention | dropdown |
| Budget | 200,000,000 | number |
| CAC target | 2,000 | number |
| Timeline | 14 days | text |
| Channels | In-app push, SMS, ZNS | text |
| Notes | Uu tien keo MAU | text |

---

## AI Prompt

```
You are a senior campaign manager. Generate a complete campaign brief.

Campaign Info:
- Name: {{ $json.campaign_name }}
- Level: {{ $json.campaign_level }}
- Target: {{ $json.target_segment }}
- Objective: {{ $json.objective }}
- Budget: {{ $json.budget }}
- CAC Target: {{ $json.cac_target }}
- Timeline: {{ $json.timeline }}
- Channels: {{ $json.channels }}
- Notes: {{ $json.notes }}

Generate in Vietnamese with English terms where appropriate:

## 1. Campaign Overview
- Name, objective, KPI targets (DRR, MAU lift, CPA)

## 2. Target Segment
- Description, size estimate, behavioral traits
- Key insight about this segment

## 3. Offer Strategy
- Type of offer (discount, cashback, reward)
- Value mechanics
- Urgency mechanism
- CAC estimate per user

## 4. Channel Allocation
- Primary, secondary channels
- Estimated volume per channel
- Budget split recommendation

## 5. Timeline
- Pre-launch, launch, optimization, wrap-up phases
- Key milestones

## 6. Risk Factors
- Top 3 risks + mitigation
- Go/no-go criteria

## 7. Measurement
- Success metrics
- Tracking setup needed
- Reporting frequency

Output as clean Markdown.
```

---

## Vi du output

CAMPAIGN BRIEF: Flash Sale T6

1. Overview
- Ten: Flash Sale T6 - Kich hoat MAU
- Objective: Push MAU thang 6
- Target: MAU T4 chua T5 (pool chinh)
- Level: M (medium)
- Budget: 200M
- Target KPI: DRR 3.5%, CAC <= 2k

2. Offer Strategy
- Offer chinh: Free ship 0d (CAC ~1.5k)
- Upsell: Giam 5k cho booking DXTT dau tien (CAC ~2k)
- Urgency: Chi trong 48h flash CTA

3. Channel Allocation
- In-app push: 40% budget, 500k volume
- SMS: 35% budget, 300k volume
- ZNS: 25% budget, 200k volume

---

## Setup

1. Tao n8n webhook de nhan input
2. Build form don gian (Typeform, Google Form, hoac custom HTML)
3. Ket noi toi OpenAI node voi prompt tren
4. Dung Google Docs node de tao document
5. Notify Slack/Telegram channel khi hoan thanh

---

*Truoc: A/B Test Analyzer*
*Ke tiep: Churn Signal + Re-engagement*
