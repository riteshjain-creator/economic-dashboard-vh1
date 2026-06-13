# Economic Dashboard V-H1 — Blueprint

**Purpose:** A personal economic intelligence page that filters signal from noise, applies first-principles reasoning, and helps make investment/trading decisions.

**User:** Amateur investor. Personal use. Optimized for clarity, actionability, and low maintenance.

**Philosophy:** Embed what exists. Reason only where reasoning adds value. Fail loudly. Decay gracefully.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         HERMES SERVER                            │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────────────┐    │
│  │  LOOP 1     │  │  LOOP 2     │  │  LOOP 3              │    │
│  │  Monthly    │  │  Weekly     │  │  Daily               │    │
│  │  Structure  │  │  Synthesis  │  │  Morning Scan        │    │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬───────────┘    │
│         │                 │                     │                │
│         └────────────┬────┴─────────────────────┘                │
│                      ▼                                           │
│            dashboard-data.json                                   │
│                      │                                           │
│                      ▼                                           │
│              git push → GitHub                                   │
└─────────────────────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              GITHUB PAGES (Read-Only)                            │
│                                                                  │
│  index.html ──reads──▶ dashboard-data.json                      │
│                                                                  │
│  Static template. Renders content. Embeds TradingView widgets.  │
│  Never changes unless page design changes.                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Page Design — "So What?" First

### Mobile (Primary — 8AM phone check)

```
┌────────────────────────────────────────┐
│  ⏱️ Updated 47 min ago ✅              │
├────────────────────────────────────────┤
│                                        │
│  TODAY'S BIAS: CAUTIOUS ⚠️             │
│                                        │
│  Nifty near 24,200 support.           │
│  Oil +2.3% overnight on Iran news.    │
│  Watch: If 24,150 breaks, 23,900 next │
│                                        │
├────────────────────────────────────────┤
│                                        │
│  INDICATORS (text-first)               │
│  Nifty    24,289  ↓0.4%              │
│  VIX      14.2    ↑8%   ⚠️           │
│  USDINR   83.42   →flat              │
│  PCR      0.92    →neutral           │
│  Breadth  0.7     ↓bearish           │
│  Crude    $82.4   ↑2.3%  ⚠️          │
│  FII      -₹1,200cr (3-day selling)  │
│  MMI      42 (Fear zone)             │
│                                        │
│  [Tap any for source link]            │
│                                        │
├────────────────────────────────────────┤
│                                        │
│  ACTIVE THREATS (3)                    │
│  🔴 US-Iran Escalation — oil risk     │
│  🟡 RBI Jun decision — on hold likely │
│  🟢 Monsoon — normal forecast         │
│                                        │
│  [Tap to expand → web detail]         │
│                                        │
├────────────────────────────────────────┤
│  WEEKLY POV (Jun 8)                    │
│  "Oil is the variable. If Iran        │
│   de-escalates, Nifty has room to     │
│   24,800. If not, banks & auto drag." │
│                                        │
│  [Full analysis → web only]           │
└────────────────────────────────────────┘
```

### Web (Secondary — Deep dive, weekend review)

Everything mobile has, PLUS:
- TradingView interactive charts (Nifty, USDINR, VIX, Crude)
- Full weekly POV with council model reasoning
- Threat detail cards with timeline & model application
- Historical context (last 4 weekly POVs)
- Indicator explanation section (what each means, how to read it)
- Backlog / emerging threats
- Meta section: system health, last cron run, confidence

---

## The Three Loops

### Loop 3 — Daily Morning Scan
**Schedule:** Mon-Sat, 8:00 AM IST
**Runtime:** ~3 min
**Complexity:** LOW

```
INPUT:
  - Active threats (from JSON config)
  - Previous day's indicator snapshot

PROCESS:
  1. Web search: "[threat keyword] India today" for each active threat
  2. Web search: "Nifty market today" for general pulse
  3. Check if any major event occurred (earnings, policy, geopolitical)
  4. Generate:
     - Bias: Bullish / Cautious / Neutral (one word)
     - 3 lines: what happened + what it means + what to watch
     - Indicator values: Nifty, VIX, USDINR, Crude (from search)
     - Flag: any threat status change (🟢→🟡→🔴)

OUTPUT:
  - Updates `daily` section of dashboard-data.json
  - Adds staleness timestamp
  - Git push

FAILURE HANDLING:
  - If search returns <2 relevant results → mark "⚠️ Low confidence"
  - If git push fails → retry once, then alert in chat
  - If cron doesn't run → staleness badge shows on page automatically
```

### Loop 2 — Weekly Synthesis
**Schedule:** Saturday, 2:00 PM IST
**Runtime:** ~8 min
**Complexity:** MEDIUM

```
INPUT:
  - Active threats + their mental model assignments
  - This week's daily updates (from JSON history)
  - Council mental models

PROCESS:
  1. For each active threat:
     - Deep web search (5+ queries, credible sources)
     - Apply assigned mental models as reasoning lens
     - Form a POV: what happened this week + what it means + what's next
     - Assess threat status (escalating/stable/de-escalating)
  2. Scan for NEW emerging threats not currently tracked
     - If found: add to backlog with brief note
  3. Generate weekly summary:
     - Overall market posture for next week
     - One actionable "watch for" per threat
     - Confidence level per POV (high/medium/low based on source quality)

OUTPUT:
  - Updates `weekly` section of dashboard-data.json
  - Archives previous week's POV to `history[]`
  - Updates threat statuses
  - Adds any new backlog items
  - Git push

FAILURE HANDLING:
  - If search quality is poor for a threat → mark POV as "low confidence"
  - Source attribution mandatory (no ungrounded claims)
```

### Loop 1 — Monthly Structure Review
**Schedule:** 1st of month, 10:00 AM IST (OR on-demand via chat)
**Runtime:** ~5 min (produces proposal, waits for human)
**Complexity:** LOW (human-in-the-loop)

```
INPUT:
  - Current active threats + their age
  - Backlog accumulated from Loop 2
  - Previous month's POV accuracy (did predictions play out?)

PROCESS:
  1. Auto-archive any threat older than 4 weeks without reconfirmation
  2. Propose new threat list:
     - Carry forward active threats still relevant
     - Promote backlog items that gained significance
     - Suggest new threats from macro calendar (RBI policy, earnings, global)
  3. Assign 2-3 mental models per threat
  4. Review indicator set (anything to add/remove?)

OUTPUT:
  - Posts proposal in this chat
  - Waits for user confirmation/edits
  - Updates `config` section of dashboard-data.json
  - Git push

AUTO-DECAY RULE:
  - If no human response in 7 days → use proposed threats as-is
  - If no response in 14 days → send reminder
  - System never goes >5 weeks without a structural refresh
```

---

## Council — Mental Models

These are permanent reasoning frameworks, not live commentary tracking.

### The Five Lenses

| # | Model | Core Question | Indicators to Watch |
|---|-------|---------------|-------------------|
| 1 | **Formalization Thesis** (Mishra) | Is the organized sector gaining share? | GST collections, digital payments, credit penetration, formal employment |
| 2 | **Financial Stability** (Rajan) | Is the banking system healthy enough to support growth? | NPAs, credit-deposit ratio, household leverage, NBFC health |
| 3 | **Fiscal Quality** (Subramanian) | Is growth real or statistical? | Capex vs revenue spend, base effects, consumption decomposition, GFCF |
| 4 | **Monetary Transmission** (Chinoy) | Is RBI policy reaching the real economy? | Real rates, credit growth, inflation expectations, liquidity (LAF) |
| 5 | **Consumption Squeeze** (Roy) | Who's actually spending? | Rural wages, FMCG volume vs value, discretionary vs staples, MGNREGA demand |

### How Models Are Applied

Each active threat gets 2-3 assigned models. Example:

```
Threat: "Oil at $90+ on Iran escalation"
Models: Monetary Transmission + Consumption Squeeze

Application:
- Chinoy lens: $90 oil → imported inflation → RBI can't cut → transmission blocked
- Roy lens: Fuel price hike hits bottom 60% disproportionately → rural demand compressed
- So What: Avoid auto, paint, FMCG. Banks safe if RBI holds. Watch CPI print.
```

---

## Indicator Set — Practical Implementation

### Text-First (Always shown, mobile + web)

| Indicator | Data Source | Update Method |
|-----------|-------------|---------------|
| Nifty 50 level + % change | Web search / TradingView | Daily (Loop 3) |
| India VIX | Web search | Daily |
| USDINR | Web search | Daily |
| PCR (Put-Call Ratio) | NSE option chain page (manual check / search) | Daily |
| Breadth (A/D ratio) | Web search "NSE advance decline today" | Daily |
| Brent Crude | Web search | Daily |
| FII/DII net flow | Web search "FII DII flow today" | Daily |
| Market Mood Index | Tickertape page (value from search) | Daily |

Each shows: **Value + Direction Arrow + Alert if unusual**

Each links to: Source URL (tap to open NSE/Tickertape/TradingView in browser)

### Embedded Charts (Web only, TradingView widgets)

| Chart | TradingView Symbol |
|-------|--------------------|
| Nifty 50 (daily, 3-month) | NSE:NIFTY |
| India VIX | NSE:INDIAVIX |
| USDINR | FX:USDINR |
| Brent Crude | TVC:UKOIL |
| Nifty Bank | NSE:BANKNIFTY |

Only these 5. All confirmed embeddable. No others.

### Manual/Commentary (Part of weekly synthesis)

- Swing Highs/Lows + Gaps → written as text in weekly POV
- Sector rotation → noted in daily bias
- RSI levels → mentioned in commentary when extreme

---

## Data Schema — dashboard-data.json

```json
{
  "meta": {
    "last_updated": "2025-06-14T08:00:00+05:30",
    "last_loop3": "2025-06-14T08:00:00+05:30",
    "last_loop2": "2025-06-14T14:00:00+05:30",
    "version": "vh1"
  },
  "daily": {
    "date": "2025-06-14",
    "bias": "cautious",
    "bias_reason": "Oil +2.3% overnight, VIX rising, FII selling 3rd day",
    "watch": "Nifty 24,150 support. If breaks, 23,900 is next.",
    "commentary": "Iran tensions pushed crude above $82...",
    "confidence": "high",
    "indicators": {
      "nifty": { "value": "24,289", "change": "-0.4%", "alert": false },
      "vix": { "value": "14.2", "change": "+8%", "alert": true },
      "usdinr": { "value": "83.42", "change": "+0.1%", "alert": false },
      "pcr": { "value": "0.92", "change": "flat", "alert": false },
      "breadth": { "value": "0.7", "change": "-0.2", "alert": true },
      "crude": { "value": "82.4", "change": "+2.3%", "alert": true },
      "fii": { "value": "-1200cr", "note": "3-day selling streak", "alert": true },
      "mmi": { "value": "42", "zone": "fear", "alert": true }
    },
    "sectors_positive": ["IT", "Pharma"],
    "sectors_negative": ["Auto", "Realty", "Metal"]
  },
  "weekly": {
    "date": "2025-06-14",
    "summary": "Oil is the variable this week...",
    "threats": [
      {
        "name": "US-Iran Escalation",
        "status": "red",
        "models_applied": ["monetary_transmission", "consumption_squeeze"],
        "pov": "If oil sustains above $85, expect RBI to pause...",
        "watch_next_week": "Iran response timeline. Watch Tuesday OPEC meeting.",
        "confidence": "medium",
        "sources": ["Reuters Jun 12", "Mint analysis Jun 13"]
      }
    ],
    "backlog": [
      { "name": "China stimulus package", "reason": "Metal/commodity play if confirmed", "added": "2025-06-12" }
    ],
    "market_posture": "Defensive. Reduce leveraged positions until oil clarity."
  },
  "config": {
    "threats": [
      { "name": "US-Iran Escalation", "added": "2025-06-01", "models": ["monetary_transmission", "consumption_squeeze"], "status": "red" },
      { "name": "RBI June Decision", "added": "2025-06-01", "models": ["monetary_transmission", "financial_stability"], "status": "yellow" },
      { "name": "Monsoon 2025", "added": "2025-06-01", "models": ["consumption_squeeze", "formalization"], "status": "green" }
    ],
    "last_structural_review": "2025-06-01",
    "decay_warning_at": "2025-06-29"
  },
  "history": {
    "weekly_povs": [],
    "daily_biases": []
  }
}
```

---

## Failure Modes & Mitigations

| Failure | Detection | Mitigation |
|---------|-----------|-----------|
| Cron doesn't run | Staleness badge on page ("⚠️ Last update: 2 days ago") | Auto-alert in chat if >36h stale |
| Search returns garbage | Low result count / irrelevant content | Mark output as "⚠️ Low confidence" + source count shown |
| Git push fails | Cron exit code | Retry once. If fails, alert in chat. JSON saved locally as backup |
| Threats go stale | `decay_warning_at` field | Auto-archive after 4 weeks. Nag user at 3 weeks |
| Commentary becomes formulaic | User feedback (weekly) | Prompt refinement in Loop 2. Track if same phrases repeat |
| GitHub Pages cache | Cache-busting query param on JSON fetch | `fetch('dashboard-data.json?t=' + Date.now())` |
| PAT expires | Git push auth failure | Alert in chat. Document renewal steps |

---

## What's NOT In Scope (Explicit)

- ❌ No trade execution or recommendations ("buy HDFC at 1,450")
- ❌ No custom data pipelines / scraping / APIs
- ❌ No real-time updates (once daily is the contract)
- ❌ No user auth / multi-user / sharing
- ❌ No historical data storage beyond git history
- ❌ No alerts/notifications (webpage pull, not push)
- ❌ No backtesting or quantitative models

---

## Implementation Order

1. **Phase 0 — Bootstrap (this session)**
   - Create repo structure
   - Write index.html (static template)
   - Seed dashboard-data.json with initial config
   - Deploy to GitHub Pages

2. **Phase 1 — Loop 3 (Daily)**
   - Build and test daily cron
   - Validate output quality for 3-5 days manually
   - Fix prompt issues

3. **Phase 2 — Loop 2 (Weekly)**
   - Build weekly synthesis cron
   - Run once manually, review output together
   - Tune mental model application

4. **Phase 3 — Loop 1 (Monthly)**
   - Build structural review cron
   - First run: set June 2025 threats together
   - Auto-decay logic

5. **Phase 4 — Harden**
   - Add staleness detection
   - Add failure alerting
   - Bootstrap 4 weeks of history (retroactive run)
   - Mobile UX refinement

---

## Maintenance Contract

| Frequency | Your Time | What |
|-----------|-----------|------|
| Daily | 2 min | Open page, read bias + indicators |
| Weekly | 0 min | Page auto-updates Saturday |
| Monthly | 10 min | Confirm/edit threat list when I propose |
| Quarterly | 15 min | Feedback on overall model quality |

**Total weekly time commitment: ~15 minutes.**

---

## Tech Stack

- **Frontend:** Single HTML file + CSS + vanilla JS. No framework. No build step.
- **Data:** Single JSON file. No database.
- **Hosting:** GitHub Pages (free, CDN, version-controlled).
- **Automation:** Hermes cron jobs (this server). Python/shell scripts.
- **Search:** Web search via Hermes tools.
- **Reasoning:** LLM (Claude) via Hermes cron prompt.
- **Version Control:** Git. Every update is a commit. Full history in git log.
