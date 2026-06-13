# Mental Models: INVESTING (1-12 Month Allocation)

**Version:** 1.0 | **Horizon:** 1-12 months | **Decision:** Equity / Debt / Cash allocation  
**Principle:** Answer one question monthly: "Should I be adding to equities or reducing?"

---

## MODEL 1: "The Liquidity Tide"

**Label:** INVESTING  
**Type:** Global flow regime detector — the single strongest multi-month predictor

### Regime Identification:
Tracks: US Real Yields → DXY/USDINR → FII Flows → India equity direction

### Logic Chain:
```
IF US Real Yields falling (or stable-low)
  AND DXY weakening (or stable)
  AND FII monthly flows turning positive
  AND India-US 10Y spread > 2% (carry trade attractive)
THEN: LIQUIDITY TIDE IS RISING → Increase equity allocation
      Target: 70-90% equity

IF US Real Yields rising rapidly (>50bps in 2 months)
  AND DXY strengthening
  AND FII selling consistently (monthly totals negative)
  AND India-US 10Y spread narrowing
THEN: LIQUIDITY TIDE IS RECEDING → Reduce equity, increase debt/cash
      Target: 40-60% equity

SUB-SIGNAL: EM ROTATION (added from backtest — W15/W16 gap)
IF China CSI 300 outperforms Nifty for 3+ consecutive weeks
  AND FII net-selling India while buying EM/China
  AND DXY neutral (102-104 range — not driving flows, ROTATION is)
THEN: LIQUIDITY TIDE IS ROTATING (not receding globally, just away from India)
      Action: Reduce India equity by 10-15%; don't panic (DXY not spiking)
      Watch for: rotation exhaustion (China valuation hits ceiling, India PE compresses to attractive)
      Rationale: Mar 2026 — CSI 300 +5% while FII sold ₹8,000Cr/week from India. DXY was only 103 (neutral).
      The selling wasn't "risk-off" — it was reallocation. Different from I1-recede.
```

### What To Do:

| Tide Direction | Equity | Debt | Cash | Sector Tilt |
|---------------|--------|------|------|-------------|
| Rising strongly | 85-90% | 5-10% | 5% | High-beta: Banks, Realty, Metals |
| Rising moderately | 70-80% | 15-20% | 5-10% | Broad market, midcaps |
| Flat/unclear | 55-65% | 25-30% | 10-15% | Large-cap quality, balanced |
| Receding moderately | 40-50% | 35-40% | 15-20% | Defensive: Pharma, IT, FMCG |
| Receding strongly | 25-35% | 40-50% | 20-30% | Min equity, max optionality |

### Historical Examples:
- **2020-21:** Fed QE → DXY collapsed → FII bought $36B in Indian equities → Nifty doubled. TIDE WAS SURGING.
- **2022:** Fed hiked 425bps → DXY hit 114 → FII sold $33B from India → Nifty -15%. TIDE RECEDED.
- **2023 H2:** US yields peaked → DXY stabilized → FII returned → Nifty +20%. TIDE TURNED.
- **2018:** US tightening + EM crisis (Turkey, Argentina) → INR hit 74 → FII sold → Nifty volatile. TIDE RECEDED.

### Exit/Reversal Signal:
- Tide rising → receding: US 10Y real yield rises >25bps in 1 month + FII turns net seller for 2+ weeks
- Tide receding → rising: DXY breaks below 3-month trend + FII turns net buyer for 2+ weeks

---

## MODEL 2: "The Domestic Engine (SIP Floor vs. FII Ceiling)"

**Label:** INVESTING  
**Type:** Structural demand/supply balance for Indian equities

### Regime Identification:
Post-2017, India has a structural domestic buyer (MF SIPs ~₹20,000+ Cr/month). This creates a "floor" that didn't exist before. The question is: does the floor hold?

### Logic Chain:
```
IF monthly SIP flows stable/growing (>₹18,000 Cr)
  AND total MF equity flows positive (no redemption panic)
  AND FII selling < DII buying capacity (floor holds)
THEN: FLOOR IS INTACT → Buy-the-dip works
      Dips of 5-8% are opportunities, not warnings.
      Target: Stay 65-75% equity, add on dips.

IF redemption pressure rising (equity MF net outflows)
  OR SIP pace declining month-over-month
  OR FII selling volume EXCEEDS DII capacity (>₹15,000 Cr/month gap)
THEN: FLOOR IS BREAKING → Historic support may not hold
      Dips can become crashes.
      Target: Reduce to 50-60% equity, don't catch falling knife.
```

### What To Do:

| Condition | Action | Reasoning |
|-----------|--------|-----------|
| Floor intact + FII buying | Add aggressively on any 3% dip | Double tailwind |
| Floor intact + FII selling | Hold, add selectively on 5%+ dips | Floor absorbs selling |
| Floor intact + FII neutral | Stay invested, no changes needed | SIPs do the work |
| Floor weakening | Stop adding, reduce 10-15% allocation | Structural support questioned |
| Floor breaking (redemptions) | Reduce 25-30%, raise cash | Once-in-5-year risk event |

### Historical Examples:
- **2022 (Floor held):** FII sold ₹1.2L Cr but SIP + DII absorbed it. Nifty only fell 15% vs global 25%. Buy-the-dip worked.
- **2018 (Floor tested):** IL&FS crisis threatened debt MFs. Some credit fund redemptions but equity SIPs held. Nifty recovered.
- **2020 Mar (Floor briefly broke):** SIPs held but panic redemptions spiked. Dip was deeper than "floor" predicted. But buying the panic was the right call.
- **Pre-2017 (No floor):** FII selling = sustained declines (2008, 2011, 2015). No domestic buyer to absorb.

### Exit/Reversal Signal:
- Floor breaking signal: 2 consecutive months of equity MF net outflows (last: Mar 2020 briefly)
- Floor restored signal: SIP pace recovers + FII selling slows below DII buying capacity

---

## MODEL 3: "The Policy Pivot Anticipator"

**Label:** INVESTING  
**Type:** Position ahead of interest rate cycle turns

### Regime Identification:
Rate cycles are the most powerful INVESTING signal for asset allocation between equity and debt. The key is to position BEFORE the pivot, not after.

### Logic Chain:
```
DETECTING UPCOMING RATE CUTS:
IF Yield curve steepening (short-term falling faster than long-term)
  AND Credit spreads stable/tightening (no systemic stress)
  AND PMI weakening toward 50 (growth slowing = need for stimulus)
  AND Inflation trajectory heading below target (gives RBI room)
  AND RBI language shifting from "vigilant" to "balanced" to "supportive"
THEN: RATE CUTS ARE COMING → 
  1. Buy long-duration government bonds (10Y+ gilts)
  2. Overweight rate-sensitive equities: Banks, NBFCs, Realty, Auto
  3. Increase equity to 75-85%

DETECTING UPCOMING RATE HIKES:
IF Yield curve flattening/inverting
  AND Credit spreads widening (stress building)
  AND Inflation rising above RBI comfort (>5.5%)
  AND RBI language shifting to "decisive action" / "whatever it takes"
THEN: RATE HIKES ARE COMING →
  1. Sell long-duration bonds, move to short-duration/liquid funds
  2. Underweight banks (NIMs compress in fear of bad loans)
  3. Reduce equity to 50-60%, increase liquid/short-term debt
```

### What To Do:

| Rate Cycle Phase | Equity Allocation | Debt Strategy | Sector Call |
|-----------------|-------------------|---------------|-------------|
| Pre-cut (RBI neutral→dovish) | 75-80% | Buy 10Y+ gilt funds | Overweight Banks, NBFC, Realty |
| Cutting (first 2-3 cuts) | 80-85% | Hold duration, ride bond rally | Stay in rate-sensitives |
| Late cutting (last cut) | 70-75%, take profit on rate-sensitives | Reduce duration gradually | Rotate to broad market |
| Pre-hike (inflation rising) | 55-65% | Exit duration, go ultra-short | Defensive: IT, Pharma |
| Hiking | 45-55% | Liquid/overnight only | Underweight banks initially |

### Historical Examples:
- **2019 (rate cuts):** RBI cut 135bps. Banking index rallied 25%. Long bonds returned 12%. Being early here was hugely profitable.
- **2020 (emergency cuts):** RBI cut 115bps. Longest duration gilts returned 15%+. Equity rallied after initial crash.
- **2022 (rate hikes):** Inflation spiked → RBI hiked 250bps. Long bonds lost 5-8%. Rate-sensitives underperformed.
- **2023 (pause):** Market anticipated pivot → banks rallied on hope of cuts ahead.

### Exit/Reversal Signal:
- Cut cycle ending: RBI language shifts to "appropriate" (neutral), inflation picks up, bond yields stop falling
- Hike cycle ending: Inflation returns to band, PMI recovery, RBI says "last hike" or "pause to assess"

---

## MODEL 4: "The Earnings-Flow Divergence Detector"

**Label:** INVESTING  
**Type:** Finds dangerous gaps between fundamentals and market price

### Regime Identification:
Markets can diverge from earnings for months (flow-driven bubbles or panics). The BEST investing opportunities occur when flows push prices FAR from earnings reality.

### Logic Chain:
```
OVERVALUED (Flows > Earnings):
IF Nifty PE > 22x (above 10-year average)
  AND earnings growth decelerating (quarterly results disappointing)
  AND FII buying still strong (flow-driven, not earnings-driven)
  AND credit spreads tight (no fear in market)
THEN: MARKET IS FLOW-RICH, EARNINGS-POOR →
  Reduce equity to 50-60%. Lock profits. Raise cash.
  The gap ALWAYS closes — either earnings catch up (rare) or price corrects (common)
  
UNDERVALUED (Earnings > Flows):
IF Nifty PE < 18x (below 10-year average)
  AND earnings growth accelerating (quarterly beats)
  AND FII selling (creating cheap entry)
  AND credit spreads stable (no systemic risk)
THEN: MARKET IS CHEAP RELATIVE TO FUNDAMENTALS →
  Increase equity to 80-90%. This is where multi-year wealth is built.
  Buy what institutions are forced to sell.
```

### What To Do:

| Divergence | Action | Risk |
|-----------|--------|------|
| Extreme overvaluation (PE >24, earnings falling, flows strong) | Max defensive: 40% equity | Bubble can persist 3-6 months |
| Moderate overvaluation (PE 20-24, earnings flat) | Cautious: 55-65% equity | Normal market, watch for trigger |
| Fair value (PE 16-20, earnings growing 10-15%) | Neutral: 65-75% equity | Stay invested, no changes |
| Moderate undervaluation (PE 14-18, earnings growing) | Aggressive: 75-85% equity | Can get cheaper short-term |
| Extreme undervaluation (PE <14, earnings inflecting up) | MAX: 85-95% equity + leverage | Generational opportunity (rare) |

### Historical Examples:
- **Early 2020 (extreme undervaluation):** Nifty PE crashed to ~14x, earnings were inflecting. Those who bought built 100%+ returns in 18 months.
- **Oct 2021 (overvaluation):** Nifty PE hit 26x on flow mania. Earnings growth was 15% but priced for 25%. Corrected 15% over 2022.
- **2018 (moderate overvaluation):** Small/midcaps at 35-40x PE with 10% earnings growth. Crashed 30-40% over 12 months.
- **2023 (flow > earnings in midcaps):** Midcap PE >25x, earnings growth ~12%. Risk building.

### Exit/Reversal Signal:
- Overvaluation correcting: Either 10%+ correction OR 2 quarters of 20%+ earnings growth that "catches up" to valuation
- Undervaluation filling: PE re-rates above 18x OR FII turns buyer (validates the cheap thesis)

---

## MODEL 5: "The Rupee Stress Thermometer"

**Label:** INVESTING  
**Type:** Override model — when USDINR goes disorderly, everything else is secondary

### Regime Identification:
India's recurring vulnerability is currency crisis. When INR weakens rapidly, it creates a self-reinforcing doom loop that overrides all other models.

### Logic Chain:
```
MILD STRESS (USDINR depreciating 2-4% in a month):
  → Background headwind only. Other models still valid.
  → Slight tilt to USD-earning sectors (IT, Pharma)
  → No allocation change needed

MODERATE STRESS (USDINR depreciating 4-7% in a month):
  → FII outflows accelerating
  → Oil import bill rising (if crude also up)
  → Reduce equity by 10-15%. Buy IT/Pharma on dips.
  → Add USD-denominated assets if possible
  → Watch RBI reserves drawdown pace

SEVERE STRESS (USDINR depreciating >7% in a month OR >10% in a quarter):
  → THIS OVERRIDES ALL OTHER MODELS
  → Full defensive: 35-45% equity, 30% short-term debt, 25% cash/gold
  → Exit all rate-sensitive positions (banks, realty, NBFCs)
  → Only hold: IT, Pharma, MNCs with dollar revenues
  → Last time: 2013 taper tantrum, 2018 EM crisis
  → Recovery only after: RBI raises rates aggressively + FII selling exhausts
```

### What To Do:

| Stress Level | USDINR Move | Equity | Sector | Override? |
|-------------|-------------|--------|--------|-----------|
| Normal | <2%/month | Per other models | Per other models | No |
| Mild | 2-4%/month | -5% equity | Tilt to exporters | No |
| Moderate | 4-7%/month | -15% equity | Heavy IT/Pharma | Partially |
| Severe | >7%/month | -30% equity, raise cash | Only USD earners | YES — full override |

### Historical Examples:
- **2013 Taper Tantrum:** INR went from 54 to 68 (+26% in 4 months). Nifty crashed 20%. RBI hiked emergency. Full override was correct.
- **2018 EM Crisis:** INR from 64 to 74 (+15% in 6 months). Nifty fell 15% from peak. Moderate→severe stress.
- **2022:** INR from 74 to 83 (+12% over year). But gradual — mild to moderate stress only. Other models still valid.
- **2020 Mar:** Brief INR stress (76 → 76.5) but reversed fast. Not a true stress event.

### Exit/Reversal Signal:
- Severe → moderate: INR stabilizes for 2+ weeks + RBI signals adequate reserves + FII selling pace halves
- Moderate → mild: INR appreciates 1%+ from stress high + DXY weakening
- Key reversal signal: RBI hikes emergency (like 2013) → typically marks the INR bottom within 2-4 weeks

---

## SYNTHESIS: Monthly Decision Process

### Step 1: Score Each Model (-2 to +2)

| Model | Score Meaning |
|-------|---------------|
| Liquidity Tide | +2 surging, +1 rising, 0 flat, -1 receding, -2 draining |
| Domestic Engine | +2 floor strong + FII buying, +1 floor holds, 0 neutral, -1 weakening, -2 breaking |
| Policy Pivot | +2 cuts imminent, +1 dovish tilt, 0 pause, -1 hawkish tilt, -2 hikes coming |
| Earnings-Flow | +2 cheap + growing, +1 fair value, 0 fairly valued, -1 expensive, -2 bubble risk |
| Rupee Stress | 0 normal, -1 mild, -2 moderate, -3 severe (override) |

### Step 2: Total Score → Allocation

| Total Score | Equity Allocation | Posture |
|-------------|-------------------|---------|
| +7 to +10 | 85-90% | Full aggressive, overweight high-beta |
| +3 to +6 | 70-80% | Bullish, buy dips |
| 0 to +2 | 55-65% | Neutral, stay invested |
| -3 to -1 | 45-55% | Cautious, trim on rallies |
| -4 to -7 | 30-45% | Defensive, raise cash |
| -8 or worse | 25-30% | Maximum defensive + hedges |

### Step 3: Override Check
- If Rupee Stress = SEVERE → ignore total score, go to severe stress allocation
- If any single model is at -2 AND another is also at -2 → treat as -8 total regardless

### Monthly Rebalancing Rules:
- Max 15-20% allocation change per month (don't panic in/out)
- Exception: Rupee Stress severe → can do 30% reduction in one shot
- Always keep 10% in liquid instruments (opportunity fund for crashes)
- SIPs continue regardless of allocation (don't stop systematic investing)

---

*Last updated: June 13, 2026*
*Review monthly or when any model hits extreme reading.*
