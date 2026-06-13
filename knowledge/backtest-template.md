# 90-Day Backtest: Mental Models Explainability

**Period:** March 15 – June 13, 2026  
**Objective:** Can our 12 mental models (7 TRADING + 5 INVESTING) explain >80% of major moves?  
**Status:** TEMPLATE — fill with live data when accessible

---

## Known Macro Context (Q1-Q2 2026)

### Global Backdrop:
- Fed holding rates after 2024-25 cuts (neutral stance)
- US-China/India trade tariff uncertainty ongoing
- US election cycle influence on policy
- DXY: range-bound to slightly weak (dollar not strengthening)

### India Backdrop:
- RBI in accommodative-to-neutral mode (cuts completed or ongoing)
- FII flows: mixed (alternating buying/selling months)
- SIP flows: record highs (~₹25,000+ Cr/month)
- Budget 2026 executed in Feb; market digesting
- Election state results potential catalyst

---

## Explainability Framework

For each major move, score:
- **5/5** = Model predicted direction, timing, AND magnitude
- **4/5** = Model predicted direction and timing (magnitude off)
- **3/5** = Model identified risk correctly but timing was off by 2-3 days
- **2/5** = Model gave right direction but wrong trigger/mechanism
- **1/5** = Model vaguely related but not actionable
- **0/5** = Complete miss / Black swan

### Template Table (populate with actual dates):

| # | Date | Index | Move | Catalyst | Leading Indicators | Model(s) Active | Explainability |
|---|------|-------|------|----------|-------------------|-----------------|----------------|
| 1 | TBD | Nifty | +/-X% | Event | Signals before | Model # | /5 |

---

## Model Coverage Assessment (Theoretical)

### What each model CAN explain:

| Move Type | Model(s) That Catch It | Expected Frequency |
|-----------|----------------------|-------------------|
| FII selling → sharp dip → bounce | Model 1 (FII Capitulation) + Model 4 (Sentiment Extreme) | 2-3x per quarter |
| Low-vol compression → breakout | Model 2 (Vol Compression) | 1-2x per quarter |
| Rally that fails (distribution) | Model 3 (Smart Money Divergence) | 1-2x per quarter |
| Fed/RBI event → vol crush | Model 7 (Pre-Event Vol Harvest) | 4-6x per quarter |
| Gamma flip → trend acceleration | Model 5 (Gamma Flip) | 2-3x per quarter |
| Sustained trend with confirmations | Model 6 (Trend Pyramid) | 1x per quarter |
| Monthly allocation shift | Models I1-I5 (Investing) | Monthly rebalance |

### What NO model explains (true blind spots):
1. **Geopolitical shocks** (India-Pakistan, Middle East escalation) — no indicator leads
2. **Single-stock blow-ups** dragging index (e.g., Adani events) — idiosyncratic
3. **Regulatory surprises** (SEBI rule changes, tax policy) — no leading signal
4. **Flash crashes** (algo/technical) — too fast for any model
5. **Natural disasters** — unknowable

### Expected Coverage:
- **Regular moves** (flow-driven, sentiment-driven, positioning-driven): ~90-95% explainable
- **Event-driven** (scheduled: RBI, Fed, earnings): ~85-90% explainable (Model 7 covers)
- **True surprises** (geopolitical, regulatory): ~20-30% explainable at best
- **Weighted average** (by frequency): ~82-88% explainability expected

---

## Validation Checklist (for live backtest)

When you have actual market data, score each major move:

1. [ ] List all days with |move| > 1% on Nifty
2. [ ] List all 5-day stretches with |move| > 3%
3. [ ] For each: identify which indicators were signaling 1-3 days BEFORE
4. [ ] Map to the model that would have been "active"
5. [ ] Count: explained moves / total moves = explainability %
6. [ ] Target: >80% for framework to be validated

### Red Flags (framework needs revision if):
- Any move type occurs 3+ times with 0/5 explainability
- A new pattern emerges that no model covers
- False positive rate >30% (model signals but no move follows)

---

## How to Run This Backtest

### Data needed:
1. Nifty 50 daily OHLC (March 15 – June 13, 2026) — source: NSE/TradingView
2. FII/DII daily data — source: NSE/moneycontrol
3. VIX daily — source: NSE
4. PCR daily — source: NSE/Opstra
5. FII L/S ratio — source: NSE Bhavcopy
6. US 10Y yield daily — source: FRED/TradingView
7. USDINR daily — source: RBI/TradingView
8. Major event calendar — source: RBI/Fed calendar

### Scoring process:
For each big move day:
1. Check FII data T-1 to T-5 → was Model 1 or 3 triggered?
2. Check VIX pattern T-10 to T-1 → was Model 2 triggered?
3. Check sentiment composite → was Model 4 triggered?
4. Check GEX estimate → was Model 5 triggered?
5. Check swing structure → was Model 6 in play?
6. Check if event was on calendar → was Model 7 applicable?
7. Score 0-5 based on actionability

---

*Created: June 13, 2026*
*To be populated with live data from market terminals*
*Target: >80% explainability for framework validation*
