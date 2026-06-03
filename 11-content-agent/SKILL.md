# 11 · Content Agent — Nâng cấp

## Cách custom cho repo của bạn

1. Sửa `config.json`: trỏ `repo_path` đến repo của bạn
2. Agent tự động đọc README.md các folder để sinh chủ đề
3. Thêm angle riêng trong dict `angles` ở hàm `suggest_ideas()`

## Ý tưởng mở rộng

- Gửi gợi ý qua email / Slack / Telegram
- Lên lịch đăng tự động dựa trên content queue
- Track performance và tự động gợi ý topic tương tự nếu bài trước chạy tốt
