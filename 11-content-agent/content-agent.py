#!/usr/bin/env python3
"""
Content Agent v0.5 — Content Idea Suggester
Không viết content thay Thảo.
Chỉ gợi ý ý tưởng dựa trên nội dung đã được duyệt trong repo.
Thảo viết content — agent hỗ trợ research + gợi ý góc nhìn + track.

Flow: Scan repo → Gợi ý idea → Track
"""
import json, os, sys, requests
from datetime import datetime, timedelta

# === Config ===
_DEFAULT = {
    "content_dir": "~/.openclaw/workspace-main",
    "output_dir": "~/.openclaw/workspace-main/posts",
    "repo_path": "~/Developer/ai-growth-prompts",
    "repo_url": "https://github.com/thaolst/ai-growth-prompts",
    "telegram_chat_id": "1606915846"
}
_cfg_path = os.path.join(os.path.dirname(__file__), "config.json")
_cfg_example = os.path.join(os.path.dirname(__file__), "config.example.json")
try:
    with open(_cfg_path) as f:
        _user = json.load(f)
except:
    try:
        with open(_cfg_example) as f:
            _user = {k: v for k, v in json.load(f).items()
                     if not str(v).startswith("YOUR_") and not str(v).startswith("sk-")}
    except:
        _user = {}
CONFIG = {k: os.path.expanduser(str(v)) if isinstance(v, str) and k not in ("telegram_token",) else v
          for k, v in {**_DEFAULT, **_user}.items()}

class IdeaAgent:
    def __init__(self, config=None):
        self.cfg = {**CONFIG, **(config or {})}
        self.log_file = os.path.join(self.cfg["output_dir"], "social-performance-log.md")
        os.makedirs(self.cfg["output_dir"], exist_ok=True)

    # === SCAN REPO ===
    def _scan_repo_topics(self) -> list:
        """Đọc các folder trong repo để lấy chủ đề đã duyệt"""
        repo = self.cfg.get("repo_path", "")
        if not os.path.exists(repo):
            return self._fallback_topics()

        topics = []
        folder_map = {
            "00": "Campaign Level — S/M/L framework",
            "01": "Voucher Design — segment-based offers",
            "02": "Segment Analysis — targeting & intervention",
            "03": "Game Mechanics — engagement loops",
            "04": "Comm & Design Brief — communication planning",
            "05": "Automation Logic — design before coding",
            "06": "Retention Strategy — retention loops, point economy",
            "07": "Experiment Design — A/B testing framework",
            "08": "Growth Glossary — thuật ngữ growth",
            "09": "AI x Growth — AI prompts cho growth",
            "10": "n8n Growth Workflows — automation sẵn dùng",
            "11": "Content Agent — personal brand automation"
        }

        for folder in sorted(os.listdir(repo)):
            if folder[:2] in folder_map:
                readme = os.path.join(repo, folder, "README.md")
                desc = folder_map[folder[:2]]
                if os.path.exists(readme):
                    with open(readme) as f:
                        first_line = f.readline().strip().lstrip("# ")
                        if first_line:
                            topics.append({"prefix": folder[:2], "title": first_line, "desc": desc})
                        else:
                            topics.append({"prefix": folder[:2], "title": f"Folder {folder[:2]}", "desc": desc})
                else:
                    topics.append({"prefix": folder[:2], "title": f"Folder {folder[:2]}", "desc": desc})

        return topics

    def _fallback_topics(self):
        return [
            {"prefix": "09", "title": "AI x Growth Marketing", "desc": "AI prompts cho growth"},
            {"prefix": "10", "title": "n8n Growth Workflows", "desc": "automation sẵn dùng"},
            {"prefix": "11", "title": "Content Agent", "desc": "personal brand automation"}
        ]

    # === RESEARCH — gợi ý idea ===
    def suggest_ideas(self, count=3) -> list:
        """Quét repo → gợi ý ý tưởng content từ nội dung đã duyệt"""
        topics = self._scan_repo_topics()
        import random
        random.shuffle(topics)

        ideas = []
        for i, t in enumerate(topics[:count]):
            # Gợi ý góc nhìn khác nhau, không viết content
            angles = {
                "Campaign Level": ["Khi nào nên chọn mức S, khi nào M, khi nào L?", "Ước lượng campaign level trước khi làm — tiết kiệm bao nhiêu thời gian?"],
                "Voucher": ["Voucher cho new user khác gì voucher cho dormant?", "Thiết kế offer theo segment — không phải ai cũng thích giảm giá"],
                "Segment": ["Dormant 30 ngày vs 60 ngày — can thiệp khác nhau thế nào?", "Phân nhóm user trước khi launch campaign"],
                "Game": ["Cơ chế game nào giữ chân user lâu nhất?", "Streak, spin wheel, hay challenge — cái nào phù hợp campaign của bạn?"],
                "Retention": ["Retention không phải là engagement", "Xu economy — vì sao điểm thưởng giữ chân user tốt hơn giảm giá"],
                "Experiment": ["A/B test bao nhiêu sample là đủ?", "Cách đọc kết quả test — statistical significance cho marketer"],
                "Glossary": ["RAG, TF-IDF, Embedding — marketer có cần hiểu không?", "Thuật ngữ AI cơ bản cho growth team"],
                "AI x Growth": ["Prompt nào cho campaign nào?", "AI agents có thực sự cần thiết cho growth team 2026?"],
                "n8n": ["Tự động hoá campaign monitoring với n8n", "Workflow nào tiết kiệm nhiều thời gian nhất?"],
                "Content Agent": ["Cách mình dùng AI để gợi ý content idea", "Research → Queue → Draft → Track: luồng content cho personal brand"]
            }

            # Tìm angle phù hợp
            suggested_angle = "Chia sẻ kinh nghiệm thực tế từ repo"
            for key, vals in angles.items():
                if key.lower() in t["desc"].lower() or key.lower() in t["title"].lower():
                    suggested_angle = random.choice(vals)
                    break

            # Hook idea — chỉ là gợi ý cấu trúc, Thảo tự viết
            hook_ideas = [
                f"Chủ đề: {t['title']}. Góc nhìn: chia sẻ kinh nghiệm thực tế từ repo.",
                f"Chủ đề: {t['title']}. Góc nhìn: áp dụng vào campaign thực tế khác gì lý thuyết.",
                f"Chủ đề: {t['title']}. Góc nhìn: 3 điều rút ra sau khi áp dụng."
            ]

            ideas.append({
                "source_folder": f"{t['prefix']}-{t['title'].split('—')[0].strip().lower().replace(' ', '-')[:20]}",
                "topic": t["title"],
                "hook_ideas": hook_ideas,
                "suggested_angle": suggested_angle,
                "why_now": f"Folder {t['prefix']} đã được duyệt và public trong repo"
            })

        return ideas

    # === GỬI TELEGRAM ===
    def _telegram(self, text: str):
        """Gửi gợi ý content qua Telegram"""
        token = self.cfg.get("telegram_token", "")
        cid = self.cfg.get("telegram_chat_id", "")
        if token and cid:
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                          data={"chat_id": cid, "text": text, "parse_mode": "HTML"})

    # === TRACK ===
    def track(self, topic: str, platform: str):
        """Ghi log bài đã đăng — Thảo tự fill metrics sau"""
        entry = f"\n{datetime.now().strftime('%Y-%m-%d')} | {topic[:40]:40s} | {platform:10s} | posted | ? views | ? likes | ? comments"
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                f.write("date | topic | platform | status | views | likes | comments")
        with open(self.log_file, "a") as f:
            f.write(entry)

    # === RUN ===
    def run(self, mode="suggest"):
        if mode == "suggest":
            ideas = self.suggest_ideas(3)
            msg_lines = ["💡 GỢI Ý CONTENT IDEA — hôm nay"]
            msg_lines.append(f"Dựa trên nội dung đã duyệt trong repo\n")

            for i, idea in enumerate(ideas, 1):
                msg_lines.append(f"#{i} — {idea['topic']}")
                msg_lines.append(f"  Góc nhìn: {idea['suggested_angle']}")
                msg_lines.append(f"  Hook idea:")
                for h in idea['hook_ideas']:
                    msg_lines.append(f"    • {h}")
                msg_lines.append(f"  📁 {idea['source_folder']}")
                msg_lines.append("")

            msg = "\n".join(msg_lines)
            print(msg)
            self._telegram(msg)
            print("\n📁 Log: track performance tại", self.log_file)

        if mode == "track":
            topic = input("Topic đã đăng: ")
            platform = input("Platform: ")
            self.track(topic, platform)
            print("✅ Tracked")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "suggest"
    IdeaAgent().run(mode)
