# n8n Growth Workflows

> Workflow n8n san dung cho growth marketing automation. Import, config, chay.
> Danh cho growth team muon automation ma khong can code.

---

## Tai sao n8n?

- Ma nguon mo -- tu host hoac dung cloud, khong lock-in
- AI native -- tich hop OpenAI/Claude san, phu hop AI x Growth
- 200+ integrations -- Google Sheets, Telegram, Slack, SQL, APIs
- Visual builder -- non-technical cung hieu va chinh sua duoc

---

## Danh sach workflow

| # | Workflow | Mo ta | Do kho |
|---|---|---|---|
| 01 | Segment + Offer Designer | Tu dong phan nhom user, thiet ke offer theo segment | Trung binh |
| 02 | Campaign Monitor + Alert | Check metric hang ngay, canh bao khi drop | Kho |
| 03 | A/B Test Analyzer | Input ket qua test, AI phan tich, chon winner | De |
| 04 | Campaign Brief Generator | Input thong tin don gian, AI ra full brief | Trung binh |
| 05 | Churn Signal + Re-engagement | Detect user sap roi bo, trigger campaign keo ve | Kho |

---

## Cach xai

1. Cai n8n -- `npx n8n` hoac deploy tren Railway/Render/Fly.io
2. Import workflow -- download file .json, keo vao n8n editor
3. Config credentials -- them API keys (OpenAI, Google, Telegram, DB)
4. Activate -- schedule tu dong chay sau khi bat

---

## Yeu cau

| Tool | Free? | Ghi chu |
|---|---|---|
| n8n | Free self-host | Cloud ~$20/thang, deploy Railway free |
| OpenAI API | Pay-per-use | ~$1-5/thang cho growth tasks |
| Google Sheets API | Free | Cho data input/output |
| Telegram Bot | Free | Cho alerts & notifications |

---

## Kien truc chung

Moi workflow deu co 3 buoc:
1. Trigger (schedule hoac webhook)
2. Process (AI + logic)
3. Output (notify + store)

Buoc giua la noi AI va growth logic hoat dong.

---

<details>
<summary>English version</summary>

Ready-to-use n8n workflows for growth marketing automation. Import, configure, run.

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
