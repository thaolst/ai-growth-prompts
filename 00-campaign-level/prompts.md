# 00 · Decide campaign level first

This is the starting point for every campaign. Get the level wrong and everything downstream — assets, timeline, channels, team — is miscalibrated.

The framework has 4 levels. Most loyalty and promotion campaigns land on S or M.

```
Level  Nature                     Budget/month   Channels                         Assets
─────  ─────────────────────────  ─────────────  ───────────────────────────────  ────────────────────────────────
S      Business As Usual          < 500M VND     In-app + owned out-app           Content + Design
M      Special Promo / Launch     < 1B VND       Above + 1–2 paid media channels  + Comm planning + Media planning
L      Branding / Strategic       > 1B VND       Full channels                    + Concept creative + PM
XL     Company Campaign           > 1B VND       Full channels                    + All of the above
```

---

## Prompt 00 · Classify campaign level before starting

**When to use:** At the very beginning, before briefing anyone or designing anything.

```
I need to classify a campaign to determine the right level of execution.

Campaign overview:
- What is it: [e.g. monthly voucher push for inactive users /
               new game mechanic launch / seasonal promotion]
- Estimated budget: [amount in VND per month]
- Expected duration: [e.g. 2 weeks / 1 month]
- Business goal: [e.g. recover lapsed users / drive first-time redemption /
                  support a product milestone]
- Is this tied to a larger company initiative or standalone? [standalone / tied to ___]

Current quarter context:
- Any L or XL campaigns running in parallel? [yes / no / not sure]
- How many S campaigns already active? [number]

Based on this, please:
1. Recommend the appropriate campaign level (S / M / L) with reasoning
2. Flag if the budget and goal are misaligned
   (e.g. goals that require M-level reach but only S-level budget)
3. List what's included at that level:
   channels available, asset types, who owns what
4. Identify the earliest possible launch date given prep duration:
   S simple = 3–4 weeks, S complex = 5–6 weeks, M = ~2 months
5. One decision the team needs to make before briefing begins
```

**What good output looks like:**
- Clear level recommendation with reasoning, not a range
- Honest flag if goals don't match budget — better to know now
- Concrete prep timeline from today's date
- The one blocker to resolve before moving forward

---

## How level affects everything downstream

Once the level is set, use the corresponding prompts:

| If level is... | Use these prompts |
|----------------|-------------------|
| S | 01 (voucher), 02 (segment), 04-S (content + design brief only) |
| M | 01 (voucher), 02 (segment), 03 (game), 04-M (+ comm planning + media) |
| L / XL | Hand off to Marketing Manager — your role shifts to input provider |

**For S campaigns specifically:**
- Channels are in-app and owned out-app only — don't plan for paid media
- Assets = content copy + design (not concept creative)
- You work directly with in-house creative and media team via Jira
- Keep asset scope simple: complex assets push prep to 5–6 weeks

**For M campaigns:**
- Budget threshold is the trigger, not just ambition
- Adds communication planning and media planning as deliverables
- 1–2 paid channels need to be scoped and booked early
