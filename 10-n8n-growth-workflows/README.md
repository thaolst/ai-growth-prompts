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

| # | Workflow | Mô tả | Độ khó |
|---|---|---|---|
| 01 | Segment + Offer Designer | Tự động phân nhóm user, thiết kế offer theo segment | Trung bình |
| 02 | Campaign Monitor + Alert | Check metric hàng ngày, cảnh báo khi drop | Khó |
| 03 | A/B Test Analyzer | Input kết quả test, AI phân tích, chọn winner | Dễ |
| 04 | Campaign Brief Generator | Input thông tin đơn giản, AI ra full brief | Trung bình |
| 05 | Churn Signal + Re-engagement | Detect user sắp rời bỏ, trigger campaign kéo về | Khó |

---

## Cách xài

1. Cài n8n — `npx n8n` hoặc deploy trên Railway/Render/Fly.io
2. Import workflow — download file `.json`, kéo vào n8n editor
3. Config credentials — thêm API keys (OpenAI, Google, Telegram, DB)
4. Activate — schedule tự động chạy sau khi bật

---

## Yêu cầu

| Tool | Free? | Ghi chú |
|---|---|---|
| n8n | Free self-host | Cloud ~$20/tháng, deploy Railway free |
| OpenAI API | Pay-per-use | ~$1–5/tháng cho growth tasks |
| Google Sheets API | Free | Cho data input/output |
| Telegram Bot | Free | Cho alerts & notifications |

---

## Kiến trúc chung

Mỗi workflow đều có 3 bước:

```
[Trigger] → [Process (AI + logic)] → [Output (notify + store)]
```

- **Trigger:** schedule hàng ngày hoặc webhook từ hệ thống
- **Process:** AI phân tích dữ liệu, growth logic ra quyết định
- **Output:** gửi alert Telegram / cập nhật Google Sheets / trigger campaign

---

## Bắt đầu từ đâu?

| Bạn muốn... | Dùng workflow |
|---|---|
| Phân nhóm user và thiết kế offer tự động | 01 - Segment + Offer Designer |
| Nhận cảnh báo khi campaign performance drop | 02 - Campaign Monitor + Alert |
| Phân tích kết quả A/B test nhanh | 03 - A/B Test Analyzer |
| Tạo campaign brief từ vài dòng input | 04 - Campaign Brief Generator |
| Phát hiện và kéo lại user sắp churn | 05 - Churn Signal + Re-engagement |

---

<details>
<summary>English version</summary>

## n8n Growth Workflows

Ready-to-use n8n workflows for growth marketing automation. Import, configure, run.
Built for growth teams who want automation without writing code.

### Why n8n?

- Open source — self-host or use cloud, no vendor lock-in
- AI native — OpenAI/Claude nodes built in, perfect for AI × Growth
- 200+ integrations — Google Sheets, Telegram, Slack, SQL, APIs
- Visual builder — non-technical marketers can understand and edit

### Workflow list

| # | Workflow | Description | Difficulty |
|---|---|---|---|
| 01 | Segment + Offer Designer | Auto-segment users, design offers per segment | Medium |
| 02 | Campaign Monitor + Alert | Daily metric check, alert on drop | Hard |
| 03 | A/B Test Analyzer | Input test results, AI analyzes, picks winner | Easy |
| 04 | Campaign Brief Generator | Simple input, AI outputs full brief | Medium |
| 05 | Churn Signal + Re-engagement | Detect at-risk users, trigger win-back campaign | Hard |

### How to use

1. Install n8n — `npx n8n` or deploy on Railway/Render/Fly.io
2. Import workflow — download `.json` file, drag into n8n editor
3. Config credentials — add API keys (OpenAI, Google, Telegram, DB)
4. Activate — set schedule, workflow runs automatically

### Requirements

| Tool | Free? | Notes |
|---|---|---|
| n8n | Free self-host | Cloud ~$20/month, Railway deploy is free |
| OpenAI API | Pay-per-use | ~$1–5/month for growth tasks |
| Google Sheets API | Free | For data input/output |
| Telegram Bot | Free | For alerts & notifications |

### Common architecture

```
[Trigger] → [Process (AI + logic)] → [Output (notify + store)]
```

Every workflow follows this pattern. The middle step is where AI and growth logic happen.

### Where to start?

| You want to... | Use workflow |
|---|---|
| Auto-segment users and design offers | 01 - Segment + Offer Designer |
| Get alerted when campaign metrics drop | 02 - Campaign Monitor + Alert |
| Analyze A/B test results fast | 03 - A/B Test Analyzer |
| Generate a campaign brief from a few inputs | 04 - Campaign Brief Generator |
| Detect and re-engage users about to churn | 05 - Churn Signal + Re-engagement |

</details>
