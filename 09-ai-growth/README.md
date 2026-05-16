# AI × Growth Marketing

> **VI:** AI đang thay đổi growth marketing thế nào — từ personalization quy mô lớn đến automated experimentation. Framework thực tế, không hype.
> **EN:** How AI is reshaping growth marketing — from personalization at scale to automated experimentation. Practical frameworks, not hype.

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

*For practical AI × Growth prompts, see the other folders in this repo — especially [01-voucher-design](../01-voucher-design) and [03-game-mechanics](../03-game-mechanics).*
