# Mental Models: TRADING (1-30 Day Swing Trading)

**Version:** 1.0 | **Horizon:** 1-30 days | **Instruments:** Nifty options/futures  
**Principle:** Composable models — check which is "active" today, follow that playbook.

---

## MODEL 1: "FII Capitulation Reversal"

**Label:** TRADING  
**Type:** Contrarian bottom-fishing at selling exhaustion

### Trigger Conditions (ALL must be true):
- FII net selling > ₹5,000 Cr/day for 5+ consecutive sessions
- FII L/S ratio < 25% long (>75% short)
- PCR > 1.3 (heavy put writing = institutional floor building)
- India VIX > 20 and showing first signs of peaking/flattening

### Logic Chain:
```
IF FIIs are max short (L/S <25%) 
  AND selling pace >₹5000cr/day for 5+ days
  AND option writers are building put walls (PCR >1.3)
  AND VIX has spiked but stopped rising
THEN: FII selling is exhausting → short covering rally imminent
```

### Causal Mechanism:
FIIs can't sell forever — they have finite India allocation to liquidate. When L/S reaches extremes, any positive catalyst triggers forced short covering (they MUST buy back futures). Put writers become natural buyers at support levels. The combo of "no more sellers" + "forced buyers" creates violent V-shaped reversals.

### Historical Examples:
- **Oct 2022:** FII sold >₹40,000 Cr in 3 weeks, L/S hit ~22%. Nifty bottomed 16,800 → rallied 2,500 pts in 6 weeks
- **Jan 2023:** FII sold heavily post-budget fears, L/S dropped to ~28%. Sharp reversal post-budget
- **Mar 2020:** Extreme FII selling (COVID), L/S near 15%. Massive rally once VIX peaked

### Failure Modes:
1. Macro regime change (Fed surprise hike) → selling resumes after brief bounce
2. India-specific structural event (tax policy, SEBI rules) → FII selling justified, continues
3. Global contagion (China credit crisis) → all EM sold regardless of positioning

### Position Sizing:
- **Entry:** 3% of capital on first signal, add 2% on confirmation (VIX drops 10%+ from peak)
- **Stop:** Below the swing low where capitulation peaked + 1% buffer
- **Target:** Previous range midpoint (typically 3-5% move)
- **Max risk:** 1.5% of capital per trade

---

## MODEL 2: "Volatility Compression Breakout"

**Label:** TRADING  
**Type:** Energy release from artificially suppressed volatility

### Trigger Conditions (ALL must be true):
- India VIX < 12 and declining for 10+ sessions
- VIX term structure in steep contango (VIX << VIX3M)
- GEX strongly positive (dealers suppressing moves)
- Nifty daily range < 0.6% for 7+ consecutive sessions
- % above 20DMA between 40-60% (neutral breadth — no direction)

### Logic Chain:
```
IF VIX is artificially low (<12 for 10+ days)
  AND dealers are short gamma (positive GEX = selling vol)
  AND range is compressed (< 0.6%/day for 7+ days)
THEN: Energy is building → breakout imminent
  Direction unknown → use straddle or wait for swing break
```

### Causal Mechanism:
Low VIX means options are cheap → institutions sell premium → dealer gamma hedging suppresses moves → range tightens further → vol-targeting strategies increase leverage → a small shock creates outsized move because everyone is positioned for calm. It's a coiled spring.

### Historical Examples:
- **Pre-Dec 2022 expiry:** VIX crushed to 11.5 for 2 weeks. Nifty broke 350 pts in 2 days
- **Jan 2024:** VIX at 11, compressed 8 days. Budget week triggered 2% gap
- **Typical expiry pattern:** VIX compression Mon-Wed, explosive Thu-Fri

### Failure Modes:
1. Low VIX persists longer than expected (holiday-thinned markets, no catalyst)
2. Breakout is a fake-out — breaks one direction then reverses (whipsaw)
3. Compression resolves via slow grind, not explosive move (wasted premium on straddle)

### Position Sizing:
- **Entry:** Long straddle at ATM (3% of capital in total premium)
- **Alternative:** Wait for swing break direction, then 4% directional
- **Stop:** Time-based — exit if no breakout in 5 trading days (premium decay)
- **Target:** 2x premium paid on straddle; 2-3% move on directional

---

## MODEL 3: "Smart Money Divergence"

**Label:** TRADING  
**Type:** Fade the false rally (distribution detection)

### Trigger Conditions (3 of 4 must be true):
- Nifty making new 5-day high BUT FII net sellers on those up-days
- RSI divergence: price higher high, RSI lower high (14-period)
- Open Interest declining on up-moves (long unwinding, not fresh buying)
- Credit spreads (HY OAS) widening even as equity rises

### Logic Chain:
```
IF index is rising (new 5-day high)
  BUT FIIs are selling into strength (distribution)
  AND momentum is weakening (RSI divergence)
  AND OI declining (old longs exiting, not new longs entering)
  AND/OR credit markets are nervous (spreads widening)
THEN: Rally is a sell-the-rip opportunity → short on confirmation
  Confirmation = break of swing low after divergence setup
```

### Causal Mechanism:
Smart money (FIIs) sells INTO rallies when they want to exit positions without crashing the market. They let retail buy the highs while they distribute. Declining OI confirms this — it's not new conviction, it's old positions exiting. Credit spreads widen first because bond markets are smarter than equity.

### Historical Examples:
- **Sep 2022 Nifty top:** Index near 18,000 but FII selling + RSI divergence. Dropped 2,500 pts over 3 weeks
- **Dec 2023 pre-election rally:** Narrow rally (3 stocks), FII selling underneath. Corrected post-election result shock
- **Jul 2023:** Nifty new highs, FII persistent sellers, breadth narrowing. 5% correction followed

### Failure Modes:
1. DII buying overwhelms FII selling (SIP flows too strong) → false divergence
2. New catalyst (rate cut announcement) resets the game — divergence invalidated
3. Divergence can persist 2-3 weeks before resolving — early shorts get squeezed

### Position Sizing:
- **Entry:** Short 3% ONLY after swing low break confirms divergence
- **Add:** 2% on first lower high after breakdown
- **Stop:** Above the divergence high + 0.5%
- **Target:** Previous support / value area (typically 3-5%)
- **Rule:** NEVER short on divergence alone — wait for price confirmation

---

## MODEL 4: "Sentiment Extreme Mean-Reversion"

**Label:** TRADING  
**Type:** Contrarian buy at maximum pessimism

### Trigger Conditions (3 of 5 must be true):
- NAAIM Exposure < 30 (managers underweight equities)
- PCR > 1.3 (heavy put writing = floor, or heavy put buying = fear)
- % above 20DMA < 20% (oversold breadth)
- VIX term structure inverted (backwardation — acute fear)
- MMI < 25 (extreme fear)

### Logic Chain:
```
IF professional sentiment is extremely bearish (NAAIM <30)
  AND breadth is washout (<20% above 20DMA)
  AND options market shows extreme positioning (PCR extreme)
  AND VIX structure confirms acute fear (backwardation)
THEN: Mean reversion rally imminent within 3-7 days
  Buy aggressively — this is the highest probability setup
```

### Causal Mechanism:
When EVERYONE is already positioned bearish, there are no marginal sellers left. Any positive catalyst (even "less bad" news) forces short covering, MF buying (due to SIP inflows they MUST deploy), and FOMO from underweight managers. Maximum pessimism = maximum potential energy for upside.

### Historical Examples:
- **Mar 2020 COVID bottom:** All sentiment at extreme fear. 80% rally in 12 months
- **Jun 2022 Fed 75bps:** NAAIM crashed to 22. S&P rallied 17% in 6 weeks
- **Oct 2023:** India VIX spiked, MMI at "Extreme Fear", % above 20DMA at 18%. Nifty rallied 12% into year-end

### Failure Modes:
1. "Can always get more extreme" — catching falling knife before true capitulation
2. Bear market rallies (30-40% of bear market time is up-days) → sentiment resets but trend resumes
3. Structural break (banking crisis, sovereign default) → sentiment stays extreme longer

### Position Sizing:
- **Entry:** 5% of capital (this is highest conviction setup when all 5 align)
- **Entry with 3/5 triggers:** 3% of capital
- **Stop:** New low below the capitulation low + 1%
- **Target:** Previous range high (5-10% move typical)
- **Time stop:** If no bounce in 7 days, reassess (might be structural, not sentiment)

---

## MODEL 5: "Gamma Flip Momentum"

**Label:** TRADING  
**Type:** Ride amplified moves when dealer hedging flips

### Trigger Conditions (ALL must be true):
- GEX flips from positive to negative (dealers go from selling vol to chasing)
- Nifty Futures OI surging (new positions being built rapidly)
- GIFT Nifty gaps > 0.5% in direction of flip
- VIX rising > 15% from recent low

### Logic Chain:
```
IF GEX flips negative (dealers now AMPLIFY moves instead of dampening)
  AND new OI is building rapidly (conviction entering market)
  AND overnight gap confirms direction
  AND VIX confirms regime shift (rising from compressed levels)
THEN: Trend move underway → momentum will persist 2-5 days
  Go with the move, not against it. Positive feedback loop active.
```

### Causal Mechanism:
When GEX is positive, dealers sell rallies and buy dips (vol suppression). When GEX flips negative, dealers MUST buy to hedge on up-moves and sell on down-moves — they AMPLIFY the trend. This creates a positive feedback loop: move → dealer hedging → more move → more hedging. Moves are larger and more persistent than in positive GEX environment.

### Historical Examples:
- **Every major Nifty sell-off:** GEX flips negative → dealers sell futures to hedge → accelerates decline
- **Apr 2024 election volatility:** GEX flipped negative → 5% move in 3 sessions
- **US analog: Jan 2022 Nasdaq:** GEX deeply negative → 20% correction amplified by dealer hedging

### Failure Modes:
1. GEX measurement error (estimated from public OI data, not precise)
2. Expiry resets gamma — move may exhaust exactly at expiry
3. In liquid markets, GEX flip may be brief (24-48hrs) — must act fast

### Position Sizing:
- **Entry:** 4% of capital, direction aligned with gap
- **Trail stop:** ATR-based (1.5x ATR from entry)
- **Target:** Hold until GEX reverts to positive OR momentum exhausts (RSI >70/<30)
- **Time frame:** 2-5 days maximum. This is a momentum capture, not a position trade
- **Rule:** NEVER fade a negative GEX move

---

## MODEL 6: "Trend Confirmation Pyramid"

**Label:** TRADING  
**Type:** Build into confirmed trends with progressive entries

### Trigger Conditions (sequential — must occur in order):
1. Swing H/L break confirms new direction (higher high OR lower low)
2. FII flow confirms direction (buying in uptrend, selling in downtrend)
3. Fresh OI build in same direction (new conviction, not short covering)
4. % above 20DMA > 65% (uptrend) or < 35% (downtrend) — breadth confirms

### Logic Chain:
```
STEP 1: Swing break → Initial small position (2%)
STEP 2: FII flow confirmation → Add (2% more)
STEP 3: Fresh OI build in direction → Add (1.5% more)
STEP 4: Breadth confirms (>65% or <35%) → Final add (1.5% more)
= Total 7% at full conviction, built progressively
```

### Causal Mechanism:
Real trends have EVERYTHING aligned — price structure, flows, positioning, and breadth. Building progressively means you only reach full size when the trend is confirmed by multiple independent signals. This avoids full-size entries on false breakouts. Pyramiding into winners is the mathematical edge of trend-following.

### Historical Examples:
- **Oct 2023 - Jan 2024 Nifty rally:** Swing break → FII buying confirmed → OI built longs → breadth expanded. Textbook pyramid opportunity.
- **2022 Nifty decline (post-peak):** Swing low broken → FII selling confirmed → Short build in OI → Breadth collapsed. 15% decline caught.

### Failure Modes:
1. Late-stage trend entry (all confirmations come AFTER most of the move)
2. Chop/range market generates false swing breaks repeatedly (death by small stops)
3. Event disrupts confirmed trend (budget, policy shock)

### Position Sizing:
- **Progression:** 2% → 4% → 5.5% → 7% (as confirmations arrive)
- **Stop:** Below swing low (longs) / above swing high (shorts) for full position
- **Partial stop:** Each tranche has own stop (latest swing level)
- **Target:** Trail stop using swing structure — exit when new swing fails

---

## MODEL 7: "Pre-Event Volatility Harvest"

**Label:** TRADING  
**Type:** Two-phase strategy exploiting predictable IV cycles

### Trigger Conditions:
**Phase 1 (pre-event):** Major known event in 3-5 days (FOMC, RBI MPC, NFP, Budget, Election result)
**Phase 2 (post-event):** Event has passed, direction established, IV crushed

### Logic Chain:
```
PHASE 1 (T-5 to T-1):
  IV rises predictably before known events
  Market compresses range (uncertainty = no one takes directional risk)
  SELL premium: Iron condor or strangle at expected move boundaries
  
PHASE 2 (T+0 to T+3):
  IV crushes immediately after event (certainty restored)
  Direction established by market reaction
  BUY directional position: Direction of first 30-min candle post-event
  holds 70%+ of the time for that session and next day
```

### Causal Mechanism:
**Phase 1:** Options become expensive pre-event because uncertainty is high. But realized vol during the "waiting period" is actually LOW (nobody acts). You sell expensive options in a low-movement environment. Edge = implied vol > realized vol.

**Phase 2:** Post-event, uncertainty resolves → IV crushes → cheap options available for directional bet. Market's first reaction (30-min candle direction) tends to persist because the "new information" gets processed by algos immediately, then humans follow.

### Historical Examples:
- **Every RBI MPC:** VIX rises 15-20% in 3 days before policy. IV crush 10-15% same day. Short strangle profit 60-70% of times.
- **Budget Day:** IV premium peaks 2 days before. Post-budget direction held for 3-5 days in 7/10 last budgets.
- **US CPI/NFP:** Nasdaq IV spikes → crushes. First 30-min direction holds ~65%.

### Failure Modes:
1. Event delivers truly unexpected outcome (demonetization-level surprise) → short premium gets destroyed
2. "Sell the news" — market does opposite of consensus reaction (everyone positioned for outcome)
3. Gap too large to manage (limit move) → can't exit short options at reasonable price

### Position Sizing:
- **Phase 1 (premium selling):** 2% max loss on short positions. Define wings clearly.
- **Phase 2 (directional):** 3% directional with tight stop (below/above event candle)
- **Rule:** NEVER sell naked options pre-event. Always define max risk with spreads.
- **Rule:** If OI suggests >80% market positioned for one outcome, fade the consensus

---

## COMPOSABILITY MATRIX

| Condition | Active Models | Action |
|-----------|--------------|--------|
| FII capitulating + sentiment extreme | Model 1 + Model 4 | MAX CONVICTION BUY (7% position) |
| GEX flip + trend confirmed | Model 5 + Model 6 | MOMENTUM + PYRAMID (ride it fully) |
| Smart divergence + vol compressed | Model 3 + Model 2 | DISTRIBUTION TOP (short after break) |
| Sentiment extreme + pre-event | Model 4 + Model 7 | BUY THE FEAR, sell premium in the calm |
| No models active | — | DO NOTHING. Cash is a position. |

## CONFLICT RESOLUTION

- Model 1 (buy) vs Model 3 (sell) → Model with MORE confirming signals wins
- Model 5 (momentum) vs Model 4 (mean-revert) → GEX is tiebreaker: negative = momentum wins
- Any model vs upcoming major event → Halve all sizes (Model 7 risk overlay)

## CIRCUIT BREAKERS (override everything)
- Daily loss > 2% of capital → STOP trading today
- Weekly loss > 5% → Halve all positions, review
- Monthly loss > 10% → Go flat, reassess regime
- VIX spike > 50% intraday → Close all short options immediately
