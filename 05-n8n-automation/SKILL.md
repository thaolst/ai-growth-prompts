# 05 - Automation Prompts

## Tiếng Việt

## Prompt 01 - Xây competitor promotion monitor

**Khi nào dùng:** Muốn tự động theo dõi khuyến mãi đối thủ, biết ngay khi đối thủ ra deal mới, thay đổi chiến lược.

```
Tôi cần thiết kế một automation monitor để theo dõi khuyến mãi đối thủ.

Use case:
- Theo dõi [tên đối thủ 1], [tên đối thủ 2]
- Tần suất: [mỗi ngày / mỗi tuần]
- Kênh monitor: [web scraping / Google Search / app store description / social]

Tôi muốn automation:
1. Tự động crawl hoặc search thông tin khuyến mãi mới nhất
2. So sánh với campaign hiện tại của tôi
3. Gửi alert vào [Telegram / Slack / email] nếu:
   - Đối thủ giảm > [X]% so với tháng trước
   - Đối thủ ra hình thức promotion mới
   - Mức ưu đãi cao hơn campaign của tôi > [Y]%
4. Lưu lịch sử để detect trend theo tháng

Output mong đợi mỗi lần chạy:
(COMPETITOR ALERT box)
```

**Prompt phụ: ước lượng chi phí**

```
Với thiết kế trên, ước lượng:
1. Số API call mỗi tháng
2. Chi phí ước tính (nếu dùng free tier được bao nhiêu %)
3. Thời gian build (với người biết automation cơ bản)
4. Cách scale từ 2 đối thủ lên 10 đối thủ
```

---

## Prompt 02 - Xây campaign performance auto-alert

**Khi nào dùng:** Campaign đang chạy, cần tự động phát hiện khi metric xuống dưới threshold mà không cần ngồi dashboard.

```
Tôi cần automation monitor cho campaign đang chạy.

Campaign:
- Tên: [mô tả]
- KPI chính: [redemption rate / CTR / conversion rate]
- Target: [VD: redemption rate > 8%]
- Threshold alert: [VD: nếu xuống dưới 5% -> cảnh báo]
- Tần suất check: [mỗi giờ / mỗi ngày]

Nguồn dữ liệu:
- [Google Sheets / dashboard API / CSV upload định kỳ]

Yêu cầu automation:
1. Lấy dữ liệu từ nguồn mỗi [giờ/ngày]
2. So sánh actual vs target
3. Phân loại mức độ:
   - Xanh: trên target -> no action
   - Vàng: dưới target nhưng > threshold -> ghi log, không alert
   - Đỏ: dưới threshold -> alert ngay với context
4. Alert gồm: metric hiện tại, target, gap, đề xuất hành động đầu tiên
5. Cuối campaign: tự động generate summary report
```

---

## Prompt 03 - Xây customer feedback sentiment tracker

**Khi nào dùng:** Có nhiều review / feedback từ user (app store, Zalo, social), cần AI đọc và cảnh báo khi sentiment xấu bất thường.

```
Tôi cần automation phân tích sentiment từ feedback user.

Nguồn feedback:
- [App store reviews / Zalo OA comments / social mentions / survey response]
- Số lượng: [khoảng X feedback/tuần]

Yêu cầu:
1. AI đọc từng feedback và phân loại:
   - Sentiment: [positive / neutral / negative]
   - Chủ đề: [VD: voucher / game / app crash / giao hàng / CSKH]
   - Mức độ nghiêm trọng: [thấp / trung / cao]
2. Alert nếu:
   - Negative sentiment spike > [X]% trong 1 ngày
   - Cùng một chủ đề negative xuất hiện > [Y] lần/tuần
   - Bất kỳ feedback nào tagged "cao" (app crash, mất tiền, security)
3. Weekly summary:
   - Top 3 vấn đề được mention nhiều nhất
   - Sentiment trend (so với tuần trước)
   - Gợi ý hành động cho từng vấn đề
```

---

## Notes

- Các prompt trên không yêu cầu tool cụ thể (có thể dùng n8n, Make, Python script, hoặc Zapier)
- Tập trung vào *logic và output*, không phải implementation chi tiết
- Scale từ nhỏ -> lớn: bắt đầu với 1 use case, kiểm tra ROI trước khi mở rộng

---

## English

## Prompt 01 - Build a competitor promotion monitor

**When to use:** You want to automatically track competitor promotions. Know instantly when a competitor launches a new deal or changes strategy.

```
I need to design an automation monitor to track competitor promotions.

Use case:
- Track [competitor 1], [competitor 2]
- Frequency: [daily / weekly]
- Monitor channels: [web scraping / Google Search / app store / social]

I want the automation to:
1. Auto-crawl or search for latest promotion info
2. Compare with my current campaigns
3. Send alert to [Telegram / Slack / email] if:
   - Competitor drops > [X]% from last month
   - Competitor launches a new promotion type
   - Offer value exceeds my campaign > [Y]%
4. Store history for monthly trend detection
```

---

## Prompt 02 - Build a campaign performance auto-alert

**When to use:** A campaign is running and you need automatic detection when metrics drop below threshold.

```
I need automation to monitor an active campaign.

Campaign:
- Name: [description]
- Key KPI: [redemption rate / CTR / conversion rate]
- Target: [e.g., redemption rate > 8%]
- Alert threshold: [e.g., if below 5% -> alert]
- Check frequency: [hourly / daily]

Data source:
- [Google Sheets / dashboard API / periodic CSV upload]

Automation requirements:
1. Fetch data from source every [hour/day]
2. Compare actual vs target
3. Severity levels:
   - Green: above target -> no action
   - Yellow: below target but above threshold -> log only
   - Red: below threshold -> immediate alert with context
4. Alert includes: current metric, target, gap, suggested action
5. End of campaign: auto-generate summary report
```

---

## Prompt 03 - Build a customer feedback sentiment tracker

**When to use:** You have many user reviews/feedback (app store, Zalo, social) and need AI to alert when sentiment turns negative.

```
I need automation to analyze sentiment from user feedback.

Feedback sources:
- [App store reviews / Zalo OA comments / social mentions / survey responses]
- Volume: [~X feedback/week]

Requirements:
1. AI reads each feedback and classifies:
   - Sentiment: [positive / neutral / negative]
   - Topic: [e.g., voucher / game / app crash / delivery / CS]
   - Severity: [low / medium / high]
2. Alert if:
   - Negative sentiment spike > [X]% in one day
   - Same negative topic appears > [Y] times/week
   - Any feedback tagged "high" (app crash, lost money, security)
3. Weekly summary:
   - Top 3 most mentioned issues
   - Sentiment trend (vs last week)
   - Suggested actions per issue
```

---

## Notes

- These prompts work with any automation tool (n8n, Make, Python, Zapier)
- Focus on *logic and output*, not specific implementation
- Start small: begin with 1 use case, validate ROI before scaling
