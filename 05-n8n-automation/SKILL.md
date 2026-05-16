# 05 - Automation Prompts

# Tiếng Việt

## Prompt 01 - Xay competitor promotion monitor

**Khi nao dung:** Muon tu dong theo doi khuyen mai doi thu, biet ngay khi doi thu ra deal moi, thay doi chien luoc.

```
Toi can thiet ke mot automation monitor de theo doi khuyen mai doi thu.

Use case:
- Theo doi [ten doi thu 1], [ten doi thu 2]
- Tan suat: [moi ngay / moi tuan]
- Kenh monitor: [web scraping / Google Search / app store description / social]

Toi muon automation:
1. Tu dong crawl hoac search thong tin khuyen mai moi nhat
2. So sanh voi campaign hien tai cua toi
3. Gui alert vao [Telegram / Slack / email] neu:
   - Doi thu giam > [X]% so voi thang truoc
   - Doi thu ra hinh thuc promotion moi
   - Muc uu dai cao hon campaign cua toi > [Y]%
4. Luu lich su de detect trend theo thang

Output mong doi moi lan chay:
(COMPETITOR ALERT box)
```

**Prompt phu: uoc luong chi phi**

```
Voi thiet ke tren, uoc luong:
1. So API call moi thang
2. Chi phi uoc tinh (neu dung free tier duoc bao nhieu %)
3. Thoi gian build (voi nguoi biet automation co ban)
4. Cach scale tu 2 doi thu len 10 doi thu
```

---

## Prompt 02 - Xay campaign performance auto-alert

**Khi nao dung:** Campaign dang chay, can tu dong phat hien khi metric xuong duoi threshold ma khong can ngoi dashboard.

```
Toi can automation monitor cho campaign dang chay.

Campaign:
- Ten: [mo ta]
- KPI chinh: [redemption rate / CTR / conversion rate]
- Target: [VD: redemption rate > 8%]
- Threshold alert: [VD: neu xuong duoi 5% -> canh bao]
- Tan suat check: [moi gio / moi ngay]

Nguon du lieu:
- [Google Sheets / dashboard API / CSV upload dinh ky]

Yeu cau automation:
1. Lay du lieu tu nguon moi [gio/ngay]
2. So sanh actual vs target
3. Phan loai muc do:
   - Xanh: tren target -> no action
   - Vang: duoi target nhung > threshold -> ghi log, khong alert
   - Do: duoi threshold -> alert ngay voi context
4. Alert gom: metric hien tai, target, gap, de xuat hanh dong dau tien
5. Cuoi campaign: tu dong generate summary report
```

---

## Prompt 03 - Xay customer feedback sentiment tracker

**Khi nao dung:** Co nhieu review / feedback tu user (app store, Zalo, social), can AI doc va canh bao khi sentiment xau bat thuong.

```
Toi can automation phan tich sentiment tu feedback user.

Nguon feedback:
- [App store reviews / Zalo OA comments / social mentions / survey response]
- So luong: [khoang X feedback/tuan]

Yeu cau:
1. AI doc tung feedback va phan loai:
   - Sentiment: [positive / neutral / negative]
   - Chu de: [VD: voucher / game / app crash / giao hang / CSKH]
   - Muc do nghiem trong: [thap / trung / cao]
2. Alert neu:
   - Negative sentiment spike > [X]% trong 1 ngay
   - Cung mot chu de negative xuat hien > [Y] lan/tuan
   - Bat ky feedback nao tagged "cao" (app crash, mat tien, security)
3. Weekly summary:
   - Top 3 van de duoc mention nhieu nhat
   - Sentiment trend (so voi tuan truoc)
   - Goi y hanh dong cho tung van de
```

---

## Notes

- Cac prompt tren khong yeu cau tool cu the (co the dung n8n, Make, Python script, hoac Zapier)
- Tap trung vao *logic va output*, khong phai implementation chi tiet
- Scale tu nho -> lon: bat dau voi 1 use case, kiem tra ROI truoc khi mo rong

---

# English

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
