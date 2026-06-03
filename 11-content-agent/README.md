# Content Agent — Idea Suggester cho Personal Brand

![prompts](https://img.shields.io/badge/prompts-none-4ade80?style=flat-square) ![type](https://img.shields.io/badge/type-idea·agent-a78bfa?style=flat-square) [![← repo](https://img.shields.io/badge/←_back-repo-a78bfa?style=flat-square)](../README.md)

## Tiếng Việt

Agent này **không viết content** — chỉ gợi ý ý tưởng từ nội dung đã được duyệt trong repo.

Mỗi gợi ý gồm: chủ đề, góc nhìn, hook idea, folder tham chiếu.

Bạn tự viết — vì tone của bạn không AI nào bắt chước được.

### Cách dùng

```bash
git clone https://github.com/thaolst/ai-growth-prompts.git
cd ai-growth-prompts/11-content-agent
cp config.example.json config.json
# Sửa config.json: repo_path trỏ đến thư mục clone
python3 content-agent.py                  # gợi ý 3 ideas
```

### Cấu trúc file

```
11-content-agent/
├── README.md
├── SKILL.md
├── content-agent.py        ← main agent (chạy được luôn)
├── config.example.json     ← config mẫu
└── config.json             ← config thật (đã .gitignore)
```

### Yêu cầu

- Python 3.8+
- Telegram bot token (tuỳ chọn — nhận gợi ý qua Telegram)

---

## English

This agent **does not write content** — it suggests ideas based on approved repo content.

Each suggestion includes: topic, angle, hook ideas, folder reference.

You write — because your tone is unique.

### Usage

```bash
cp config.example.json config.json
python3 content-agent.py                  # suggest 3 ideas
```
