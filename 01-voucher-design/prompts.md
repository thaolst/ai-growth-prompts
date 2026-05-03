# 01 · Voucher design

Design vouchers that fit both the user segment and the campaign level.
At S level, fewer channels means the voucher mechanic itself carries more weight.

---

## Prompt 01 · Design a voucher set for a specific segment

**When to use:** Segment is defined, campaign level is set. Need to design the right voucher within what's available at that level.

```
I need to design a voucher set for a loyalty campaign.

Campaign level: [S / M]
If S: channels are in-app + owned out-app only
If M: channels include in-app, owned out-app, and [specify 1–2 paid channels]

Segment profile:
- Points balance: [low / mid / high — or approximate range]
- Transaction frequency: [e.g. 1–2x per month]
- Recent behavior: [e.g. redeemed food vouchers, hasn't used game features]
- Days since last activity: [number]

Goal with this segment:
- [e.g. re-engage lapsed users / increase redemption frequency /
   drive first transaction]

Voucher budget per user: [approximate — or "tight / moderate / flexible"]

Please suggest:
1. 3 voucher options suited to both the segment and the level's channel scope
   (at S level: vouchers that work without paid media amplification)
2. Why each fits their behavioral pattern
3. Trigger logic — when to send, through which available channel
4. How to measure effectiveness at day 7 and day 14
```

**What good output looks like:**
- Options designed for the available channels, not idealized ones
- At S level: mechanic is self-contained — doesn't depend on paid reach to work
- Trigger is specific (day + behavior condition + channel)
- Metrics match what's actually trackable at that level

---

## Prompt 02 · Choose between voucher directions

**When to use:** 2–3 directions are on the table, need to pick one fast.

```
I'm choosing between voucher directions for a [S / M] campaign.

Option A: [brief description]
Option B: [brief description]
Option C: [if applicable]

Campaign level constraints:
- S: in-app + owned channels only, content + design assets, tight timeline
- M: adds 1–2 paid channels and comm planning

Primary KPI: [e.g. redemption rate / re-engagement / first transaction]
Budget constraint: [tight / moderate]
Risk to avoid: [e.g. cannibalizing already-active users / high abuse potential]

Please:
1. Which option fits best given the level constraints and KPI? Why?
2. What breaks down at S level that might work at M?
3. Final recommendation — one option, clear reason
```

---

## Prompt 03 · Diagnose an underperforming voucher campaign

**When to use:** Mid-campaign, redemption rate isn't hitting target. Need fast diagnosis.

```
Campaign level: [S / M]

Voucher running:
- Type and conditions: [brief description]
- Audience: [segment description]
- Channels used: [in-app banner / push / owned social / paid — per level]
- Days running: [number]

Results so far:
- Redemption rate: [actual vs. target]
- Notification CTR: [if applicable]
- Drop-off point: [where in the funnel are users stopping?]

Please diagnose:
1. Most likely failure point — voucher value, conditions, channel, or segment fit?
2. At [S/M] level, what can realistically change in the next 3 days?
   (No new channels at S. No concept creative changes mid-campaign.)
3. If only one thing: what is it?
```

**What good output looks like:**
- Diagnosis respects what's changeable at the given level
- Won't suggest adding paid channels if campaign is S
- Prioritizes highest-impact, lowest-effort fix
