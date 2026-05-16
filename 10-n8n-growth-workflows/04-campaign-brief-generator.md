# 04 â€” Campaign Brief Generator

> Input campaign requirements â†’ AI generates full campaign brief â†’ output to Google Doc + Slack notification.

---

## When to Use

- You need a structured campaign brief fast
- You want consistency across all campaign briefs
- You want AI to suggest channels, budget allocation, and offer types based on campaign goals

---

## How It Works

```
1. Input campaign info  â†’  2. AI generates brief  â†’  3. Output to Google Doc  â†’  4. Notify team
   (form/webhook)           (GPT/Claude)              (Google Docs API)        (Slack/Telegram)
```

---

## Input Form

Create a simple n8n webhook form or Google Form with these fields:

| Field | Example | Type |
|---|---|---|
| Campaign name | "Flash Sale T6" | text |
| Campaign level | S / M / L | dropdown |
| Target segment | "MAU T4 chÆ°a T5" | text |
| Objective | MAU push / Revenue / Retention | dropdown |
| Budget | 200,000,000 | number |
| CAC target | 2,000 | number |
| Timeline | 14 days | text |
| Channels | "In-app push, SMS, ZNS" | text |
| Notes | "Æ¯u tiÃªn kÃ©o MAU" | text |

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

## Example Output

```
# Campaign Brief: Flash Sale T6

## 1. Overview
- TÃªn: Flash Sale T6 - KÃ­ch hoáº¡t MAU
- Objective: Push MAU thÃ¡ng 6
- Target: MAU T4 chÆ°a T5 (pool chÃ­nh)
- Level: M (medium)
- Budget: 200M
- Target KPI: DRR 3.5%, CAC â‰¤ 2k

## 2. Offer Strategy
- Offer chÃ­nh: Free ship 0Ä‘ (CAC ~1.5k)
- Upsell: Giáº£m 5k cho booking DXTT Ä‘áº§u tiÃªn (CAC ~2k)
- Urgency: "Chá»‰ trong 48h" flash CTA

## 3. Channel Allocation
| Channel | % Budget | Volume | CVR expectation |
|---|---|---|---|
| In-app push | 40% | 500k | 3.5% |
| SMS | 35% | 300k | 2.5% |
| ZNS | 25% | 200k | 4.0% |
```

---

## Setup

1. Create an n8n webhook for receiving input
2. Build a simple input form (Typeform, Google Form, or custom HTML)
3. Connect to OpenAI node with the prompt above
4. Use Google Docs node to create the document
5. Notify your Slack/Telegram channel when complete

---

*Previous: [A/B Test Analyzer](./03-ab-test-analyzer.md)*
*Next: [Churn Signal + Re-engagement](./05-churn-reengagement.md)*
