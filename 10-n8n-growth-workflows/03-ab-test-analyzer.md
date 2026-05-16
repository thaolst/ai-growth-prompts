# 03 - A/B Test Analyzer

> Input ket qua A/B test, AI phan tich thong ke, xac dinh winner, tao report.

---

## Khi nao dung

- Ban chay A/B test va can tuyen bo winner
- Can confidence interval va statistical significance, khong chi cam tinh
- Muon AI giai thich TAI SAO variant nay thang

---

## Cach hoat dong

1. Input results (paste data)
2. AI tinh toan stats (GPT phan tich)
3. Xac dinh outcome (AI + logic)
4. Report (Sheets/Slack)

---

## Dinh dang data input

Tao Google Sheet voi cac cot:

| test_name | variant | impressions | conversions | conversion_rate | spend | revenue |
|---|---|---|---|---|---|---|
| Voucher May | A (control) | 50,000 | 1,200 | 2.4% | 0 | 0 |
| Voucher May | B (free ship) | 50,000 | 1,850 | 3.7% | 75,000 | 0 |
| Voucher May | C (discount 5k) | 50,000 | 1,600 | 3.2% | 50,000 | 0 |

---

## AI Prompt

```
You are an A/B test analyst with a statistics background. Analyze this test data:

{{ $json.data }}

Calculate:
1. Conversion rate for each variant
2. Lift vs control (%)
3. Statistical significance (p-value using z-test)
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
  "recommendation": "Variant B shows 54.2% lift with 99.3% confidence."
}
```

---

## Bang decision

| p-value | Confidence | Verdict | Action |
|---|---|---|---|
| < 0.01 | > 99% | Strong winner | Scale to 100% |
| < 0.05 | > 95% | Clear winner | Scale with monitoring |
| 0.05-0.10 | 90-95% | Marginal | Tiep tuc test hoac decide |
| > 0.10 | < 90% | Inconclusive | Can them data hoac declare no winner |

---

## Setup

1. Tao Google Sheet voi test data
2. Paste prompt vao OpenAI node
3. Ket noi output toi Slack/Telegram va Sheet logger
4. Schedule: manual (chay khi co ket qua test)

---

*Truoc: Campaign Monitor + Alert*
*Ke tiep: Campaign Brief Generator*
