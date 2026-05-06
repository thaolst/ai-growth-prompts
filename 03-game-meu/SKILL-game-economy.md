# Game Economy Design / Thiết kế kinh tế game

## What this skill does / Skill này làm gì

**EN:** Design game economies that balance company revenue with user enjoyment — covering earn/burn ratios, leaderboard mechanics, and the critical first 72 hours where most users decide to stay or leave.

**VI:** Thiết kế kinh tế game cân bằng giữa lợi ích công ty và trải nghiệm user — bao gồm tỷ lệ earn/burn, cơ chế leaderboard, và 72 giờ đầu tiên quyết định user ở lại hay bỏ đi.

---

## When to use / Khi nào dùng

**EN:** Use when building or tuning a loyalty game mechanic — especially when drop-off is high in the first 3 days, or when the earn/burn ratio isn't sustainable for the business.

**VI:** Dùng khi xây dựng hoặc điều chỉnh cơ chế game loyalty — đặc biệt khi drop-off cao trong 3 ngày đầu, hoặc khi tỷ lệ earn/burn chưa bền vững cho công ty.

---

## Core insight / Insight cốt lõi

**EN:** Most loyalty games die in the first 72 hours — not because the mechanic is bad, but because users don't see a visible goal worth returning for. Leaderboard and jackpot only work if users believe they can reach them.

**VI:** Hầu hết loyalty game chết trong 72 giờ đầu — không phải vì cơ chế dở, mà vì user không thấy mục tiêu đủ rõ để quay lại. Leaderboard và jackpot chỉ có tác dụng khi user tin rằng mình có thể đạt được.

---

## Prompt 01 — Design leaderboard to drive daily retention

**EN:** Use when you have a working game mechanic but need a competitive layer to bring users back daily.
**VI:** Dùng khi game đã chạy được nhưng cần competitive layer để kéo user quay lại mỗi ngày.

```
I need to design a leaderboard for a loyalty game to increase daily retention.

Game context:
- Core mechanic: [e.g. rock-paper-scissors / spin / quiz]
- Earn mechanic: [e.g. win = +100 pts, draw = +50 pts, lose = +2 pts]
- Burn mechanic: [e.g. 50 pts per play, packages available]
- Current drop-off: [e.g. most users leave within 3 days]
- Target retention: [e.g. 6 weeks]

Reward structure available:
- Jackpot: [description]
- Vouchers: [description]
- Points: [description]

Business constraint:
- Burn must exceed earn by [e.g. 2.1x] to be sustainable

Please design:
1. Leaderboard structure — weekly or monthly? Individual or team?
   Which fits better with the earn/burn ratio above?
2. Reward tiers — how many ranks, what rewards per tier?
   Make top reward aspirational but middle rewards feel reachable
3. Reset mechanic — when does leaderboard reset and why?
   How does reset create a "fresh start" motivation?
4. Daily hook — what makes user open app specifically to check leaderboard?
   (position change notification / rival system / daily rank update)
5. How does this leaderboard help maintain the 2.1x burn/earn ratio?
```

**What good output looks like / Output tốt trông như thế nào:**
- Leaderboard structure fits the game's earn/burn pace
- Middle tier rewards feel reachable within 1 week for average user
- Daily hook is specific — not just "notify them"
- Business math is checked — burn still exceeds earn after rewards

---

## Prompt 02 — Fix activation in the first 72 hours

**EN:** Use when data or hypothesis shows most users drop off within the first 3 days — before they've formed any habit with the game.
**VI:** Dùng khi data hoặc hypothesis cho thấy phần lớn user bỏ trong 3 ngày đầu — trước khi họ hình thành thói quen với game.

```
I need to improve activation in the first 72 hours of a loyalty game.

Current experience:
- What user sees on Day 1: [describe onboarding or entry point]
- Free plays available: [number]
- Earn on win/draw/lose: [amounts]
- Burn per play: [amount]
- What goal is visible to user on Day 1: [jackpot / leaderboard / voucher / nothing clear]
- Current D3 retention: [% or "unknown — hypothesis only"]

Hypothesis for drop-off:
[Your best guess at why users leave — unclear goal / losing feels bad /
 reward too small / goal too far / other]

Please design the 72-hour activation journey:
1. Day 1 — what's the one thing user must understand and feel after first session?
   (not a list — one thing only)
2. What "visible progress" should user see after every play?
   (points toward next reward / leaderboard rank / distance to jackpot)
3. Day 2 trigger — what notification or in-app prompt brings them back?
   Make it specific to what they did on Day 1
4. Day 3 hook — if user hasn't returned, what's the re-engagement mechanic?
   Should feel like an opportunity, not a reminder
5. What's the minimum viable goal a new user can realistically reach in 3 days?
   Design the first milestone around that
```

**What good output looks like / Output tốt trông như thế nào:**
- Day 1 insight is one clear thing, not a checklist
- Visible progress is concrete — specific number or rank, not "show something motivating"
- Day 2 trigger references Day 1 behavior specifically
- 3-day milestone is achievable — not aspirational

---

## Prompt 03 — Balance earn/burn ratio for sustainability

**EN:** Use when the game economy feels off — either users are accumulating too many points (bad for business) or burning through points too fast (bad for retention).
**VI:** Dùng khi kinh tế game đang lệch — user tích điểm quá nhiều (không tốt cho công ty) hoặc tiêu điểm quá nhanh (không tốt cho retention).

```
I need to check and adjust the earn/burn ratio of a loyalty game.

Current economy:
Earn sources:
- [e.g. win: +100 pts]
- [e.g. draw: +50 pts]
- [e.g. play participation: +2 pts per play]
- [e.g. vouchers distributed in game: X pts value]

Burn sources:
- [e.g. cost per play: 50 pts]
- [e.g. premium packages: 100 pts / 2 plays, 3000 pts / 15 plays]
- [e.g. jackpot redemption: X pts]

Target ratio: burn must exceed earn by [e.g. 2.1x]
Average plays per user per day: [number or estimate]
Current win rate: [% or "unknown"]

Please analyze:
1. At average play frequency, is the current ratio above or below 2.1x?
   Show the math simply
2. Which earn source is the biggest risk to the ratio?
3. 3 adjustments to reach 2.1x without making the game feel punishing
   (adjust package pricing / adjust win rewards / adjust participation bonus)
4. What win rate keeps the ratio sustainable?
   If win rate is too high, what's the maximum sustainable win reward?
5. Sanity check: at the adjusted ratio, does an average user still feel
   like they're making progress? Or does it feel like a losing game?
```

**What good output looks like / Output tốt trông như thế nào:**
- Math is shown clearly, not hidden
- Adjustments are small and testable, not a full redesign
- Sanity check is honest — flags if the ratio makes the game feel unfair
