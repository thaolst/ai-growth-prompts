# Contributing / Đóng góp

Cảm ơn bạn đã quan tâm đến việc đóng góp cho **ai-growth-prompts**! Repo này sống nhờ những prompt được kiểm chứng thực tế từ cộng đồng growth marketing.

## How to contribute / Cách đóng góp

### 1. Add a new prompt / Thêm prompt mới

Mỗi prompt cần có đủ 3 phần:

| Part / Phần | Description / Mô tả |
|---|---|
| **When to use / Khi nào dùng** | Tình huống cụ thể, không chung chung |
| **Prompt** | Có thể copy-paste, điền `[...]` với context thực tế |
| **Example output / Ví dụ output** | Output đúng trông như thế nào |

Prompt có thể bằng **tiếng Việt hoặc tiếng Anh**. Nếu được, thêm bản dịch ở dưới.

### 2. Folder structure

```
00-campaign-level/     — SKILL.md (Xác định level S/M/L)
01-voucher-design/     — SKILL.md (Thiết kế voucher theo segment)
02-segment-analysis/   — SKILL.md (Target & can thiệp)
03-game-mechanics/     — SKILL.md (Game mechanics)
04-comm-and-brief/     — SKILL.md (Comm plan & brief)
05-automation/         — SKILL.md (Automation prompts)
06-growth-frameworks/  — SKILL.md (Prompt mental model growth)
07-case-studies/       — SKILL.md (Prompt phân tích case study)
08-glossary/           — SKILL.md (Prompt tra cứu thuật ngữ)
09-ai-growth/          — SKILL.md (Prompt AI × growth marketing)
```

Muốn thêm folder mới? Tạo issue trước để thảo luận.

### 3. File naming

- `SKILL.md` - prompt chính của folder
- `SKILL-<topic>.md` - prompt mở rộng theo chủ đề cụ thể
- `README.md` - giới thiệu folder (optional, tự động lấy từ SKILL.md)

### 4. Style guidelines

- Viết cho người đọc có thể copy-paste và dùng ngay
- Không dùng jargon không cần thiết
- Nếu có số liệu hoặc ngưỡng (ví dụ: budget), ghi rõ đơn vị
- Giữ giọng văn thực tế, không phải tiếp thị

## Process / Quy trình

1. **Fork** repo này
2. **Tạo nhánh:** `feat/<tên-prompt>` hoặc `fix/<mô-tả>`
3. **Commit** thay đổi
4. **Mở Pull Request** mô tả rõ:
   - Prompt này dùng trong tình huống nào
   - Tại sao nó useful (bạn đã test chưa? kết quả?)
5. Maintainer review trong vòng 1 tuần

## Code of Conduct / Quy tắc ứng xử

- Tôn trọng lẫn nhau
- Không spam, không quảng cáo
- Feedback mang tính xây dựng

---

*Câu hỏi? Mở issue hoặc gửi DM.*
