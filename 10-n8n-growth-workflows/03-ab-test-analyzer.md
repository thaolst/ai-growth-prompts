# 03 â€” A/B Test Analyzer

> Input A/B test results â†’ AI performs statistical analysis â†’ determines winner â†’ generates report.

---

## When to Use

- You ran an A/B test and need to declare a winner
- You want confidence intervals and statistical significance, not gut feeling
- You want AI to explain WHY one variant won

---

## How It Works

```
1. Input results  â†’  2. AI calculates stats  â†’  3. Determine outcome  â†’  4. Report
   (paste data)       (GPT analyzes)           (AI + logic)          (Sheets/Slack)
```

---

## Data Input Format

Create a Google Sheet with columns:

| test_name | variant | impressions | conversions | conversion_rate | spend | revenue |
|---|---|---|---|---|---|---|
| Voucher Test May | A (control) | 50,000 | 1,200 | 2.4% | 0 | 0 |
| Voucher Test May | B (free ship) | 50,000 | 1,850 | 3.7% | 75,000 | 0 |
| Voucher Test May | C (discount 5k) | 50,000 | 1,600 | 3.2% | 50,000 | 0 |

---

## AI Prompt

```
You are an A/B test analyst with a statistics background. Analyze this test data:

{{ $json.data }}

Calculate:
1. Conversion rate for each variant
2. Lift vs control (%)
3. Statistical significance (p-value approximation using z-test)
4. Confidence interval (95%) for each variant
5. Winner declaration with confidence level

Also consider:
- Revenue per user if revenue data exists
- Cost per conversion if spend data exists
- Minimum detectable effect: 10%
- Significance threshold: p < 0.05

Output JSON format:
{
  "variants": [
    {
      "name": "A",
      "conversion_rate": 2.4,
      "lift_vs_control": 0,
      "p_value": null,
      "is_winner": false,
      "confidence_interval": [2.2, 2.6]
    }
  ],
  "winner": "B",
  "confidence_level": 0.95,
  "recommendation": "Variant B shows 54.2% lift with 99.3% confidence. Scale to 100%."
}
```

---

## Setup

1. Create a Google Sheet with your test data
2. Paste the prompt above into an OpenAI node
3. Connect output to a Slack/Telegram notification and Sheet logger
4. Schedule: manual (run when you have test results)

---

## Decision Matrix

| p-value | Confidence | Verdict | Action |
|---|---|---|---|
| < 0.01 | > 99% | ðŸ† Strong winner | Scale to 100% |
| < 0.05 | > 95% | âœ… Clear winner | Scale with monitoring |
| 0.05â€“0.10 | 90â€“95% | âš ï¸ Marginal | Continue test or make judgment call |
| > 0.10 | < 90% | âŒ Inconclusive | Need more data or declare no winner |

---

*Previous: [Campaign Monitor + Alert](./02-campaign-monitor.md)*
*Next: [Campaign Brief Generator](./04-campaign-brief-generator.md)*
