# n8n Growth Workflows

> Workflow n8n sẵn dùng cho growth marketing automation. Import, config, chạy.
> Dành cho growth team muốn automation mà không cần code.

---

## Tại sao n8n?

- Mã nguồn mở — tự host hoặc dùng cloud, không lock-in
- AI native — tích hợp OpenAI/Claude sẵn, phù hợp AI × Growth
- 200+ integrations — Google Sheets, Telegram, Slack, SQL, APIs
- Visual builder — non-technical cũng hiểu và chỉnh sửa được

---

## Danh sách workflow

| # | Workflow | Mô tả | Độ khó | JSON |
|---|---|---|---|---|
| 01 | Segment + Offer Designer | Phân nhóm user, thiết kế offer theo segment | Trung bình | [import](./workflows/01-segment-offer-designer.json) |
| 02 | Campaign Monitor + Alert | Check metric hàng ngày, cảnh báo khi drop | Khó | [import](./workflows/02-campaign-monitor.json) |
| 03 | A/B Test Analyzer | Input kết quả test, AI phân tích, chọn winner | Dễ | [import](./workflows/03-ab-test-analyzer.json) |
| 04 | Campaign Brief Generator | Input đơn giản, AI ra full brief vào Google Doc | Trung bình | [import](./workflows/04-campaign-brief-generator.json) |
| 05 | Churn Signal + Re-engagement | Detect user sắp rời bỏ, trigger campaign kéo về | Khó | [import](./workflows/05-churn-reengagement.json) |

---

## Cách import workflow vào n8n

1. **Cài n8n** — `npx n8n` hoặc deploy trên [Railway](https://railway.app) (free tier)
2. **Download file JSON** — click link `import` trong bảng trên
3. **Import vào n8n** — vào n8n editor → Menu → Import from file → chọn file JSON
4. **Config credentials** — thêm API keys: OpenAI, Google Sheets, Telegram/Slack
5. **Thay YOUR_SHEET_ID** — mở workflow, tìm node Google Sheets, điền ID sheet của bạn
6. **Chạy thử manual** — nhấn "Execute Workflow" một lần trước khi bật schedule
7. **Activate** — bật toggle để workflow tự chạy theo lịch

---

## Yêu cầu

| Tool | Free? | Ghi chú |
|---|---|---|
| n8n | Free self-host | Cloud ~$20/tháng, Railway deploy free |
| OpenAI API | Pay-per-use | ~$1–5/tháng cho growth tasks |
| Google Sheets API | Free | Cho data input/output |
| Telegram Bot | Free | Cho alerts & notifications |
| Google Docs API | Free | Chỉ cần cho workflow 04 |
| Slack | Free tier | Tùy chọn thay Telegram |

---

## Kiến trúc chung

```
[Trigger] → [Fetch Data] → [AI Analysis] → [Decision] → [Output + Log]
```

Mỗi workflow đều theo pattern này. Node AI ở giữa là nơi growth logic xảy ra.

---

## Bắt đầu từ đâu?

| Bạn muốn... | Dùng workflow |
|---|---|
| Phân nhóm user và thiết kế offer tự động | 01 - Segment + Offer Designer |
| Nhận cảnh báo khi campaign metric drop | 02 - Campaign Monitor + Alert |
| Phân tích kết quả A/B test nhanh | 03 - A/B Test Analyzer |
| Tạo campaign brief từ vài dòng input | 04 - Campaign Brief Generator |
| Phát hiện và kéo lại user sắp churn | 05 - Churn Signal + Re-engagement |

---

<details>
<summary>English version</summary>

## n8n Growth Workflows

Ready-to-import n8n workflows for growth marketing automation. Download JSON → import → configure → activate.

### How to import

1. Install n8n — `npx n8n` or deploy on Railway (free tier)
2. Download JSON file from the table above
3. In n8n: Menu → Import from file → select JSON
4. Add credentials: OpenAI, Google Sheets, Telegram/Slack
5. Replace `YOUR_SHEET_ID` placeholders with your actual sheet IDs
6. Run manually once to verify, then activate schedule

### Workflow list

| # | Workflow | Description |
|---|---|---|
| 01 | Segment + Offer Designer | Auto-segment users, design offers per segment |
| 02 | Campaign Monitor + Alert | Daily metric check, alert on anomalies |
| 03 | A/B Test Analyzer | Statistical analysis, pick winner |
| 04 | Campaign Brief Generator | Full brief into Google Doc from simple input |
| 05 | Churn Signal + Re-engagement | Detect at-risk users, trigger win-back |

</details>

---

## 10 vs 05 — Dùng cái nào?

| | Folder này (10) | [05-n8n-automation](../05-n8n-automation) |
|---|---|---|
| **Là gì** | Workflow n8n *sẵn sàng import* | Prompt để *thiết kế* logic automation |
| **Dùng khi** | Đã có n8n, muốn chạy ngay | Muốn hiểu logic, tự build bằng bất kỳ tool nào |
| **Tool** | n8n cụ thể | n8n, Make, Zapier, Python — đều được |
| **Output** | File JSON import thẳng vào n8n | AI giúp bạn thiết kế logic |

**Gợi ý:** Đọc [`05-n8n-automation`](../05-n8n-automation) trước để hiểu logic → dùng folder này để thực thi nhanh.
