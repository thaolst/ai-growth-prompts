# 10 · n8n Growth Workflows — Prompt Thiết Kế & Customize

## Tiếng Việt

5 workflow n8n trong folder này là công cụ có sẵn. Prompt dưới đây giúp bạn:
- **Chọn** workflow phù hợp với campaign hiện tại
- **Customize** workflow cho context cụ thể
- **Kết hợp** nhiều workflow thành pipeline tự động
- **Troubleshoot** khi workflow chạy sai

Dùng sau khi đã đọc README.md để biết cách import.

---

## Prompt 01 — Chọn & customize workflow cho campaign của bạn

**Khi nào dùng:** Có 1 campaign cụ thể, không biết nên dùng workflow nào hoặc cần chỉnh workflow cho phù hợp.

```
Tôi đang chạy campaign sau và muốn dùng n8n workflow trong repo này.

Thông tin campaign:
- Tên: [VD: Flash sale 48h cuối tháng]
- Mục tiêu: [tăng redemption / kéo user quay lại / giới thiệu tính năng mới]
- Segment target: [new user / active / dormant / tất cả]
- Quy mô: [S / M / L]
- Kênh: [push / SMS / email / in-app / paid]
- Thời gian chạy: [số ngày]
- Data có sẵn: [VD: user segment CSV trên Google Sheet]

Từ thông tin trên, hãy:
1. Đề xuất workflow nào trong [01-05] phù hợp nhất — giải thích tại sao
2. Nếu cần kết hợp nhiều workflow: đề xuất thứ tự và cách ghép nối
3. Các node cần customize: cách điều chỉnh trigger, filter, AI prompt cho campaign này
4. Metric nào workflow có thể tự động ghi lại để báo cáo cuối campaign
5. Rủi ro khi chạy workflow với campaign này (data quality, schedule conflict,...)
```

**Ví dụ output mong đợi:**
> Dùng workflow 01 (Segment + Offer Designer) kết hợp 04 (Campaign Brief Generator). Chạy 01 trước để phân nhóm → output làm input cho 04. Customize node AI trong 01: thay segment mô tả bằng target của campaign flash sale. Schedule: chạy 01 mỗi sáng, 04 chạy 1 lần đầu campaign.

---

## Prompt 02 — Tự động hoá workflow pipeline cho campaign lifecycle

**Khi nào dùng:** Muốn tự động hoá toàn bộ lifecycle campaign (từ planning → launch → monitor → report) bằng cách kết hợp nhiều workflow.

```
Tôi muốn build một pipeline n8n tự động hoá toàn bộ campaign lifecycle:

Campaign: [VD: Chương trình tích điểm hàng tháng]
Các phase: [planning → segment → launch → monitor → report]
Duration: [VD: 30 ngày]

Yêu cầu automation:
1. Phase Planning: tạo campaign brief tự động từ input ngắn
2. Phase Segment: phân nhóm user và thiết kế offer riêng từng segment
3. Phase Launch: gửi notification qua push/SMS kèm offer cá nhân hoá
4. Phase Monitor: theo dõi metric hằng ngày, cảnh báo nếu KPI drop > 20%
5. Phase Report: cuối campaign tự động tổng hợp báo cáo

Hãy thiết kế pipeline dùng các workflow có sẵn + thêm node nếu cần:
1. Sơ đồ pipeline: workflow nào chạy trước/sau, trigger mỗi phase
2. Data flow: dữ liệu từ workflow trước truyền sang workflow sau như thế nào
3. Schedule: cron schedule cho từng phase (chạy 1 lần / daily / weekly)
4. Error handling: nếu 1 workflow fail thì các workflow sau xử lý ra sao
5. Logging: cách ghi log để biết pipeline đang ở phase nào
```

---

## Prompt 03 — Customize AI prompt bên trong workflow n8n

**Khi nào dùng:** Đã import workflow, muốn chỉnh prompt AI node cho phù hợp với ngành hàng / sản phẩm / chiến dịch của mình.

```
Tôi đã import workflow [01 / 02 / 03 / 04 / 05] vào n8n.
Workflow này có node AI (OpenAI/Claude) cần customize prompt cho context của tôi.

Thông tin sản phẩm/ngành của tôi:
- Ngành: [VD: Fintech / E-commerce / Edtech / Food]
- Loại sản phẩm: [VD: App thanh toán, sàn thương mại, app học tập]
- User persona chính: [VD: Gen Z văn phòng 22-30 tuổi]
- Campaign thường chạy: [VD: voucher, cashback, game, event]
- KPI chính: [VD: MAU, redemption rate, retention D30]

Hãy viết lại prompt cho node AI trong workflow [số] để:
1. Phù hợp với ngành và sản phẩm của tôi (dùng đúng thuật ngữ)
2. Giữ nguyên cấu trúc output mà workflow downstream cần
3. Thêm các ràng buộc cụ thể (VD: không offer quá 30%, ưu tiên retention)
4. Viết bằng [Tiếng Việt / English] — tuỳ theo ngôn ngữ campaign

Output: Prompt mới, sẵn sàng copy-paste vào node AI trong n8n.
```

**Ví dụ output mong đợi:**
```
Node AI trong workflow 01 (Segment + Offer Designer) — customize cho Fintech:

Prompt mới:
"Bạn là growth marketer cho app thanh toán di động. Người dùng Gen Z (22-30), chi tiêu trung bình 2-5 triệu/tháng.
Phân tích segment sau và đề xuất offer tối ưu:
[segment data từ input]
Yêu cầu:
- Không offer cashback > 20% (margin constraint)
- Ưu tiên offer dạng tích điểm (Xu) hơn giảm giá trực tiếp
..."
```

---

## Prompt 04 — Debug workflow & xử lý lỗi thường gặp

**Khi nào dùng:** Workflow chạy sai / không ra output như mong đợi / báo lỗi.

```
Tôi gặp vấn đề với workflow [01 / 02 / 03 / 04 / 05].

Triệu chứng:
- Workflow chạy nhưng không có output / output sai
- Node AI báo lỗi / trả về empty
- Schedule không kích hoạt đúng giờ
- Dữ liệu từ Google Sheets không được đọc đúng

Mô tả cụ thể:
[Paste error message hoặc mô tả chi tiết hành vi workflow]
[Paste cấu hình node đang gặp vấn đề nếu có]

Hãy giúp tôi:
1. Nguyên nhân có thể nhất (top 3)
2. Cách kiểm tra từng nguyên nhân — thứ tự ưu tiên
3. Fix cụ thể: thay đổi config nào, ở node nào
4. Cách test fix mà không ảnh hưởng dữ liệu thật (dùng test event)
```

---

## Prompt 05 — Mở rộng workflow: thêm tính năng mới

**Khi nào dùng:** Workflow hiện tại gần đúng nhưng cần thêm tính năng (VD: thêm kênh output, thêm filter, thêm step phân tích).

```
Tôi muốn mở rộng workflow [01 / 02 / 03 / 04 / 05] thêm tính năng sau:

Tính năng mới:
[VD: 
- Gửi thêm bản copy report vào email
- Thêm filter để chỉ xử lý user active > 30 ngày
- Thêm step phân tích sentiment từ feedback user
- Tích hợp thêm kênh output: Zalo OA / Facebook page inbox]

Cấu hình hiện tại của workflow:
[mô tả workflow đang chạy — node trigger, AI, output]

Hãy hướng dẫn:
1. Các node cần thêm vào workflow (theo thứ tự)
2. Cách kết nối node mới với node hiện tại (input/output mapping)
3. API key / credential cần thêm (nếu có)
4. Cách test node mới trước khi active
5. Tác dụng phụ có thể xảy ra với workflow hiện tại
```

---

## English

5 n8n workflows in this folder are ready-to-import tools. The prompts below help you:
- **Choose** the right workflow for your campaign
- **Customize** it to your specific context
- **Combine** multiple workflows into automated pipelines
- **Debug** when things go wrong

Use after reading README.md for import instructions.

---

## Prompt 01 — Choose & customize workflow for your campaign

**When to use:** Have a specific campaign, not sure which workflow to use or need to adapt it.

```
I'm running this campaign and want to use an n8n workflow:

Campaign info:
- Name: [e.g. 48h flash sale end-of-month]
- Goal: [boost redemption / re-engage users / launch new feature]
- Target segment: [new / active / dormant / all]
- Scale: [S / M / L]
- Channels: [push / SMS / email / in-app / paid]
- Duration: [days]
- Available data: [e.g. user segments in Google Sheets]

Based on this:
1. Recommend the best workflow from [01-05] — explain why
2. If combining multiple workflows: suggest order and connection
3. Nodes to customize: trigger, filter, AI prompt adjustments
4. Metrics the workflow should auto-log for post-campaign reporting
5. Risks: data quality, schedule conflicts, cost overruns
```

---

## Prompt 02 — Build automated pipeline for campaign lifecycle

**When to use:** Want to automate the full campaign lifecycle (planning → launch → monitor → report) by chaining workflows.

```
I want to build an n8n pipeline for full campaign lifecycle:

Campaign: [e.g. monthly loyalty points program]
Phases: [planning → segment → launch → monitor → report]
Duration: [e.g. 30 days]

Automation needs per phase:
1. Planning: auto-generate brief from short input
2. Segment: segment users, design per-segment offers
3. Launch: send personalized push/SMS with offers
4. Monitor: daily metric tracking, alert if KPI drops > 20%
5. Report: auto-compile end-of-campaign report

Design a pipeline using existing workflows + new nodes if needed:
1. Pipeline diagram: workflow order, phase triggers
2. Data flow: how data passes between workflows
3. Schedule: cron per phase (one-time / daily / weekly)
4. Error handling: if one workflow fails, what happens next
5. Logging: how to track which phase the pipeline is in
```

---

## Prompt 03 — Customize AI prompt inside n8n workflow

**When to use:** Already imported a workflow, need to adapt the AI node prompt to your industry/product/campaign.

```
I imported workflow [01/02/03/04/05] into n8n.
The AI node (OpenAI/Claude) needs prompt customization for my context.

My product/industry:
- Industry: [e.g. Fintech / E-commerce / Edtech / Food]
- Product type: [e.g. payment app, marketplace, learning app]
- Primary user persona: [e.g. Gen Z office workers 22-30]
- Typical campaigns: [e.g. vouchers, cashback, games, events]
- Key KPI: [e.g. MAU, redemption rate, D30 retention]

Rewrite the AI node prompt to:
1. Match my industry and product (use correct terminology)
2. Keep output structure that downstream nodes expect
3. Add specific constraints (e.g. max 30% offer, prioritize retention)
4. Write in [Vietnamese / English]

Output: Ready-to-paste prompt for the n8n AI node.
```

---

## Prompt 04 — Debug workflow errors

**When to use:** Workflow runs but gives wrong output / errors / schedule issues.

```
I'm having issues with workflow [01/02/03/04/05].

Symptoms:
- Workflow runs but output is wrong / empty
- AI node errors / returns empty
- Schedule doesn't trigger on time
- Google Sheets data read incorrectly

Specifics:
[Paste error message or describe workflow behavior]
[Paste problematic node config if available]

Help me:
1. Most likely cause (top 3)
2. How to verify each cause — priority order
3. Specific fix: which config change, which node
4. How to test the fix without affecting real data
```

---

## Prompt 05 — Extend workflow with new features

**When to use:** Existing workflow is close but needs additional features.

```
I want to extend workflow [01/02/03/04/05] with:

New feature:
[e.g.
- Send report copy via email
- Add filter for active > 30 days users
- Add sentiment analysis from user feedback
- Add output channel: Zalo OA / Facebook page]

Current workflow config:
[describe current setup — trigger, AI, output nodes]

Guide me:
1. New nodes to add (in order)
2. How to connect to existing nodes (input/output mapping)
3. New API key / credential needed (if any)
4. How to test new nodes before activating
5. Side effects on existing workflow
```
