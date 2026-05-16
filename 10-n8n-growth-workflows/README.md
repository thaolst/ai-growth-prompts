# n8n Growth Workflows

> Workflow n8n sáºµn dÃ¹ng cho growth marketing automation. Import, config, cháº¡y.
> DÃ nh cho growth team muá»‘n automation mÃ  khÃ´ng cáº§n code.

---

## Táº¡i sao n8n?

- **MÃ£ nguá»“n má»Ÿ** -- tá»± host hoáº·c dÃ¹ng cloud, khÃ´ng lock-in
- **AI native** -- tÃ­ch há»£p OpenAI/Claude sáºµn, phÃ¹ há»£p AI x Growth
- **200+ integrations** -- Google Sheets, Telegram, Slack, SQL, APIs
- **Visual builder** -- non-technical cÅ©ng hiá»ƒu vÃ  chá»‰nh sá»­a Ä‘Æ°á»£c

---

## Danh sÃ¡ch workflow

| # | Workflow | MÃ´ táº£ | Äá»™ khÃ³ |
|---|---|---|---|
| 01 | [Segment + Offer Designer](./01-segment-offer-designer.md) | Tá»± Ä‘á»™ng phÃ¢n nhÃ³m user, thiáº¿t káº¿ offer theo segment | Trung bÃ¬nh |
| 02 | [Campaign Monitor + Alert](./02-campaign-monitor.md) | Check metric hÃ ng ngÃ y, cáº£nh bÃ¡o khi drop | KhÃ³ |
| 03 | [A/B Test Analyzer](./03-ab-test-analyzer.md) | Input káº¿t quáº£ test, AI phÃ¢n tÃ­ch, chá»n winner | Dá»… |
| 04 | [Campaign Brief Generator](./04-campaign-brief-generator.md) | Input thÃ´ng tin Ä‘Æ¡n giáº£n, AI ra full brief | Trung bÃ¬nh |
| 05 | [Churn Signal + Re-engagement](./05-churn-reengagement.md) | Detect user sáº¯p rá»i bá», trigger campaign kÃ©o vá» | KhÃ³ |

---

## CÃ¡ch xÃ i

1. **CÃ i n8n** -- `npx n8n` hoáº·c deploy trÃªn Railway/Render/Fly.io
2. **Import workflow** -- download file `.json`, kÃ©o tháº£ vÃ o n8n editor
3. **Config credentials** -- thÃªm API keys (OpenAI, Google, Telegram, DB)
4. **Activate** -- schedule tá»± Ä‘á»™ng cháº¡y sau khi báº­t

---

## YÃªu cáº§u

| Tool | Free? | Ghi chÃº |
|---|---|---|
| n8n | Free self-host | Cloud ~$20/thÃ¡ng, deploy Railway free |
| OpenAI API | Pay-per-use | ~$1-5/thÃ¡ng cho growth tasks |
| Google Sheets API | Free | Cho data input/output |
| Telegram Bot | Free | Cho alerts & notifications |

---

## Kiáº¿n trÃºc chung

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  Trigger    â”‚ -> â”‚  Process    â”‚ -> â”‚  Output     â”‚
â”‚ (schedule   â”‚    â”‚ (AI + logic)â”‚    â”‚ (notify +   â”‚
â”‚  / webhook) â”‚    â”‚             â”‚    â”‚  store)     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

Háº§u háº¿t workflow Ä‘á»u theo pattern 3 bÆ°á»›c nÃ y. BÆ°á»›c giá»¯a lÃ  nÆ¡i AI + growth logic hoáº¡t Ä‘á»™ng.

---

<details>
<summary>English version</summary>

Ready-to-use n8n workflows for growth marketing automation. Import, configure, run. Built for growth teams who want automation without writing code.

### Why n8n?
- Open source, no vendor lock-in
- Native AI nodes (OpenAI/Claude), perfect for AI x Growth
- 200+ integrations
- Visual builder, non-technical marketers can understand

### How to use
1. Install n8n
2. Import workflow JSON
3. Configure credentials
4. Activate

</details>
