# 05 · Automation Prompts — Growth Marketing Workflows

## Prompt 01 · Xây competitor promotion monitor

**Khi nào dùng:** Muốn tự động theo dõi khuyến mãi đối thủ — biết ngay khi đối thủ ra deal mới, thay đổi chiến lược.

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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 COMPETITOR ALERT
Đối thủ: Shopee
Deal mới: Free ship 0đ + giảm 50K
Kênh: In-app banner + push
So chúng ta: cao hơn 20%
Khuyến nghị: cần điều chỉnh voucher trong 3 ngày
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

## Prompt 02 · Xây campaign performance auto-alert

**Khi nào dùng:** Campaign đang chạy, cần tự động phát hiện khi metric xuống dưới threshold mà không cần ngồi dashboard.

```
Tôi cần automation monitor cho campaign đang chạy.

Campaign:
- Tên: [mô tả]
- KPI chính: [redemption rate / CTR / conversion rate]
- Target: [VD: redemption rate > 8%]
- Threshold alert: [VD: nếu xuống dưới 5% → cảnh báo]
- Tần suất check: [mỗi giờ / mỗi ngày]

Nguồn dữ liệu:
- [Google Sheets / dashboard API / CSV upload định kỳ]

Yêu cầu automation:
1. Lấy dữ liệu từ nguồn mỗi [giờ/ngày]
2. So sánh actual vs target
3. Phân loại mức độ:
   - 🟢 Xanh: trên target → no action
   - 🟡 Vàng: dưới target nhưng > threshold → ghi log, không alert
   - 🔴 Đỏ: dưới threshold → alert ngay với context
4. Alert gồm: metric hiện tại, target, gap, đề xuất hành động đầu tiên
5. Cuối campaign: tự động generate summary report

Ví dụ alert:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 CAMPAIGN ALERT
Metric: Redemption rate
Actual: 4.2% | Target: 8% | Threshold: 5%
⏱ Đã chạy: 5/14 ngày
💡 Đề xuất: kiểm tra push CTR → nếu push OK thì
   vấn đề ở voucher value hoặc segment fit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Prompt 03 · Xây customer feedback sentiment tracker

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

Output mong đợi:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 FEEDBACK SUMMARY — Tuần 20

Tổng feedback: 342 (+12% so với tuần trước)
Positive: 58% | Neutral: 27% | Negative: 15%

Top issues:
1. "Voucher hết nhanh" — 47 mentions ⚠️
2. "Game bị lag" — 23 mentions 🔴
3. "Push không đúng giờ" — 12 mentions 🟡

🚨 Alert: Game lag tăng 200% so với tuần trước
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notes

- Các prompt trên không yêu cầu tool cụ thể (có thể dùng n8n, Make, Python script, hoặc Zapier)
- Tập trung vào *logic và output*, không phải implementation chi tiết
- Scale từ nhỏ → lớn: bắt đầu với 1 use case, kiểm tra ROI trước khi mở rộng
