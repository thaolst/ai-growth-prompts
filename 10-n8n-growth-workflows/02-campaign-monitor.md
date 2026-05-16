# 02 â€” Campaign Monitor + Alert

> Daily campaign health check: monitor metrics, detect anomalies, send alerts, auto-generate reports.

---

## When to Use

- You're running a campaign and need to know ASAP if something goes wrong
- You want daily performance snapshots without manual checking
- You want AI to analyze trends and suggest actions

---

## How It Works

```
1. Fetch metrics  â†’  2. AI analyzes   â†’  3. Determine status  â†’  4. Alert & report
   (DB/API)           (GPT/Claude)       (logic node)         (Telegram/Slack + Sheets)
```

---

## Nodes (step by step)

### Step 1: Fetch Campaign Metrics
- **Node:** Google Sheets / MySQL / PostgreSQL / HTTP Request (API)
- **Input:** `date`, `impressions`, `clicks`, `conversions`, `spend`, `revenue`, `segment`, `channel`
- **Data range:** Last 7 days for trend analysis, today for current status

### Step 2: AI Analysis
- **Node:** OpenAI / Claude
- **Prompt:**
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

### Step 3: Branch by Status
- **Node:** IF/Logic
- **Logic:** Green â†’ daily report only. Red/Yellow â†’ urgent alert + recommended action

### Step 4a: Green â€” Daily Report
- **Node:** Telegram / Google Sheets
- **Content:** "Campaign OK. DRR: X%, Spend: X, Revenue: X"

### Step 4b: Red/Yellow â€” Urgent Alert
- **Node:** Telegram / Slack
- **Content:** "ðŸš¨ ALERT: Campaign [name]. DRR dropped X%. Suggestion: [AI action]"

### Step 4c: Log Report
- **Node:** Google Sheets
- **Append** to campaign log: `date`, `status`, `drr`, `cpa`, `ai_notes`

---

## Example Alert Output

```
ðŸ“Š Campaign Daily Report â€” May 16, 2026
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
âœ… STATUS: Green (on track)

ðŸ“ˆ Key metrics:
â€¢ DRR: 3.2% (target: 3.0%) âœ“
â€¢ CPA: 1,850 VND (limit: 2,000) âœ“
â€¢ Spend: 45.2M / 50M budget
â€¢ Revenue: 1.45B

ðŸ“‰ Anomalies detected:
â€¢ Segment "New Users" CPA increased to 2,300 VND (+15% D-7)
â€¢ Channel "SMS" volume dropped 30% vs yesterday

ðŸŽ¯ Recommended actions:
1. Pause SMS campaign for "New Users" segment
2. Increase push notification frequency to compensate
3. Review SMS delivery rate with provider

â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
Report generated: AI-powered
```

---

## JSON Workflow

Download: [`02-campaign-monitor.json`](./02-campaign-monitor.json)

```json
{
  "name": "02 - Campaign Monitor + Alert",
  "nodes": [
    {
      "name": "Daily Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [250, 300],
      "parameters": {
        "rule": {
          "interval": [{ "field": "days", "hoursInterval": 24 }]
        }
      }
    },
    {
      "name": "Fetch Campaign Metrics",
      "type": "n8n-nodes-base.googleSheets",
      "position": [450, 300],
      "parameters": {
        "operation": "read",
        "documentId": "YOUR_SHEET_ID",
        "sheetName": "Campaign Data"
      }
    },
    {
      "name": "AI Analyze",
      "type": "n8n-nodes-base.openAi",
      "position": [650, 300],
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "You are a campaign analyst. Analyze metrics, detect anomalies, recommend actions. Output JSON with: status (green/yellow/red), anomalies (array), recommendations (array), summary (string)."
            },
            {
              "role": "user",
              "content": "Campaign metrics: {{ $json }}"
            }
          ]
        }
      }
    },
    {
      "name": "IF Status = Red",
      "type": "n8n-nodes-base.if",
      "position": [850, 300],
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "status-check",
              "leftValue": "={{ $json.status }}",
              "rightValue": "red",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        }
      }
    },
    {
      "name": "Alert Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [1050, 200],
      "parameters": {
        "chatId": "YOUR_CHAT_ID",
        "text": "={{ 'ðŸš¨ ALERT: ' + $json.summary }}"
      }
    },
    {
      "name": "Log to Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [1050, 400],
      "parameters": {
        "operation": "append",
        "documentId": "YOUR_SHEET_ID",
        "sheetName": "Campaign Log"
      }
    }
  ],
  "connections": {
    "Daily Schedule": { "main": [[ { "node": "Fetch Campaign Metrics", "type": "main", "index": 0 } ]] },
    "Fetch Campaign Metrics": { "main": [[ { "node": "AI Analyze", "type": "main", "index": 0 } ]] },
    "AI Analyze": { "main": [[ { "node": "IF Status = Red", "type": "main", "index": 0 } ]] },
    "IF Status = Red": { 
      "main": [
        [ { "node": "Alert Telegram", "type": "main", "index": 0 } ],
        [ { "node": "Log to Sheets", "type": "main", "index": 0 } ]
      ]
    },
    "Alert Telegram": { "main": [[ { "node": "Log to Sheets", "type": "main", "index": 0 } ]] }
  }
}
```

---

## Customization Tips

- **Channels:** Add Slack, SMS, or email alerts in parallel
- **Thresholds:** Customize AI prompt with your campaign's specific KPIs
- **Segments:** Add a loop to analyze each segment independently
- **Dashboard:** Connect output to a Google Data Studio / Looker Studio dashboard

---

*Previous: [Segment + Offer Designer](./01-segment-offer-designer.md)*
*Next: [A/B Test Analyzer](./03-ab-test-analyzer.md)*
