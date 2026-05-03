# 02 · Segment analysis

Understand who to target and how — within the reach available at each campaign level.

---

## Prompt 04 · Analyze cohort drop to find intervention points

**When to use:** Retention data shows drop-off but cause and intervention aren't clear.

```
Here is retention data for a loyalty program cohort:

[Paste data — CSV, table, or written numbers]

Example:
Week 0:  100%
Week 1:  68%
Week 2:  45%
Week 4:  38%
Week 8:  29%
Week 12: 22%

Campaign level I can run in response: [S / M]

Please analyze:
1. Steepest drop point — what are users likely doing at that stage?
2. W0→W1 vs W1→W2 — which is more concerning and why?
3. 3 specific behavioral hypotheses for the drop
4. For each hypothesis, one experiment sized for [S/M]:
   - S: in-app mechanic or owned channel test, 1–2 weeks
   - M: can include a paid channel or comm planning layer
5. If only one intervention is possible this week, what is it?
```

---

## Prompt 05 · Segment users to allocate budget within level constraints

**When to use:** Budget is set (S or M threshold), need to allocate to the right groups.

```
I need to prioritize which user segments to target.

Campaign level: [S / M]
Available budget: [approximate — or <500M for S, <1B for M]
Channels available at this level:
- S: in-app + owned out-app
- M: above + [specify paid channels]

Data I have per user:
- Points balance
- Days since last transaction
- Voucher redemptions in past 30 days
- Preferred voucher category
- [Other if available]

Goal: [e.g. grow MAU / recover lapsed users / increase frequency]

Please suggest:
1. 3–4 segments max — needs to be executable with available channels
2. For each: characteristics, budget share, best voucher type, reasoning
3. Which segment(s) to skip at this budget level — and why
4. If budget only allows targeting 1 segment, which one and why?
```

---

## Prompt 06 · Find early churn signals for proactive intervention

**When to use:** Want to intervene before users go inactive — at S level, this relies entirely on owned channels and in-app mechanics.

```
I want to identify at-risk users early enough to intervene.

Campaign level for intervention: [S / M]
Intervention options available:
- S: push notification, in-app banner, in-app mechanic
- M: above + [paid retargeting / owned social / email]

Signals I can track:
- Days since last app open
- Days since last voucher redemption
- Points balance trend (growing / flat / declining)
- Notification engagement rate (past 30 days)
- [Other]

Please suggest:
1. Which signals are strongest predictors of churn?
2. Best signal combination for an early warning threshold
3. Specific threshold values — not too early (wasted effort), not too late (useless)
4. Intervention per risk tier, using only channels available at [S/M]:
   - Low risk → [lightweight action]
   - Medium risk → [stronger action]
   - High risk → [most direct action]
```
