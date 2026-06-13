# Market Indicators: A First-Principles Guide for Nifty & Indian Equity Traders

**Purpose:** Answer two questions every morning: "Is today a day to be aggressive or defensive?" and "What's the one thing to watch?"

**Philosophy:** You check once daily. You trade Nifty options/futures. You need signal, not noise. This guide is opinionated about what matters.

---

## FRAMEWORK: Leading vs Lagging vs Noise

Before diving into indicators, understand this hierarchy:

- **LEADING indicators** predict moves before they happen. They tell you where price is going. (e.g., FII flows, options positioning, global cues overnight)
- **COINCIDENT indicators** move with price. They tell you what's happening now. (e.g., breadth, sector rotation)
- **LAGGING indicators** confirm what already happened. They tell you where price was. (e.g., RSI, moving averages)
- **NOISE** for a daily-checker: anything that only matters on 5-min candles or requires continuous monitoring.

**Critical insight:** Most amateur traders overweight lagging indicators (RSI, support/resistance) and underweight leading ones (positioning data, global flows). Flip this.

---

## CRITIQUE OF YOUR CURRENT INDICATORS

| Indicator | Type | Verdict for Daily Checker |
|-----------|------|--------------------------|
| Breadth (A/D Ratio) | Coincident | ✅ Keep — but check END of day, not pre-market |
| USDINR | Leading/Macro | ✅ Keep — critical for FII flow direction |
| Fear & Greed / Market Mood Index | Contrarian signal | ⚠️ Useful only at extremes. Noise 80% of the time |
| Put Call Ratio (PCR) | Leading | ✅ Keep — one of the best pre-market signals |
| Open Interest | Leading | ✅ Keep — but only OI CHANGE matters, not absolute OI |
| RSI Levels | Lagging | ❌ Overrated for daily decisions. Confirms, doesn't predict |
| Swing High/Low & Gaps | Lagging | ⚠️ Useful for setting levels, not for directional bias |
| Sector Rotation (intraday) | Noise for daily checker | ❌ Remove from morning routine. This is an intraday tool |

**Redundancies:**
- Fear & Greed Index and PCR overlap heavily. PCR is more precise. Keep PCR, demote Fear & Greed to weekly contrarian check.
- RSI and Support/Resistance are both backward-looking price derivatives. You don't need both for a morning check.

**What's Missing (Critical Gaps):**
1. **SGX Nifty / Gift Nifty** — THE most important pre-market signal. Why isn't this #1?
2. **FII/DII Cash Flow Data** — The single biggest structural driver of Indian markets
3. **US Markets overnight close** — Nifty correlates ~0.6 with S&P 500 overnight moves
4. **India VIX** — Options pricing of expected volatility. Better than RSI for risk sizing
5. **US Dollar Index (DXY)** — Drives FII flows globally. Stronger dollar = EM pain
6. **Crude Oil** — India imports 85% of its oil. Crude up = fiscal stress + INR weakness

---

## TIER 1: Check Daily Before Market Open (9:00 AM Routine)

These 5 indicators, checked in this order, give you 80% of the information you need.

---

### 1. GIFT Nifty (formerly SGX Nifty)

**What it is:** Nifty futures traded on the NSE IFSC exchange in Gift City. Trades from 6:30 AM IST (essentially overnight Nifty futures reflecting global moves).

**Why it matters:** This IS what Nifty will open at, give or take 10-20 points. It incorporates all overnight global events — US close, Asia open, Europe futures. The causal mechanism: arbitrageurs ensure Gift Nifty and Nifty spot converge at 9:15 AM open. If Gift Nifty is +150 at 9 AM, Nifty WILL open up ~150.

**How to read it:**
- Gap up/down >100 pts: Strong directional open, trend likely continues in first hour
- Gap up/down 30-100 pts: Normal gap, may fill or extend — watch first 15 min
- Gap <30 pts: Flat open, intraday positioning matters more
- **Key edge:** Compare Gift Nifty move vs the move it "should" have based on S&P 500. If S&P was +1% but Gift Nifty is flat, India-specific selling is happening (likely FII)

**Where to check:** https://www.moneycontrol.com/indian-indices/gift-nifty-52.html (or search "Gift Nifty live" on Google)

**Frequency:** Every morning, 9:00-9:10 AM. This is your first look.

---

### 2. FII/DII Cash Market Flows (Previous Day)

**What it is:** Net buying or selling by Foreign Institutional Investors (FII) and Domestic Institutional Investors (DII) in the cash equity market, published daily after market hours.

**Why it matters:** FIIs move Indian markets. Period. They own ~17% of Indian equities and their flow direction sets multi-week trends. The causal chain: When FIIs sell, they also sell INR (to repatriate), weakening the rupee, which makes them sell more (currency loss compounds equity loss). This creates self-reinforcing cycles. DIIs (mutual funds, insurance) are the counter-force — they buy on domestic SIP flows.

**How to read it:**
- FII selling >₹3000 cr/day consistently: Bearish regime. Don't fight it with longs.
- FII buying >₹2000 cr/day consistently: Bullish tailwind. Buy dips.
- FII selling BUT DII buying more: Market may hold/chop. Watch for reversal.
- FII selling AND DII not buying enough: Fastest declines happen here.
- **Leading signal:** 5-day rolling sum of FII flows. If this turns from negative to positive, market bottom is likely in.

**Where to check:** https://www.moneycontrol.com/stocks/marketstats/fii_dii_activity/index.php (or NSDL website for provisional data by 7 PM)

**Frequency:** Every morning. Yesterday's data tells you today's trend persistence.

---

### 3. Nifty PCR (Put-Call Ratio) + Max Pain + OI Change at Key Strikes

**What it is:** PCR = total put open interest ÷ total call open interest on Nifty options. Max Pain = the strike price at which maximum options expire worthless (where option sellers make the most money).

**Why it matters:** Option sellers (institutions) are the "house." They have larger capital and generally win. The market gravitates toward max pain on expiry day. PCR tells you how the market is positioned:
- High PCR (>1.2): Lots of put writing = institutions are confident market won't fall. They're providing a floor. Bullish.
- Low PCR (<0.7): Lots of call writing = institutions capping upside. Bearish.
- The causal mechanism: Put writers must buy futures to hedge if market falls. So heavy put writing creates a "put wall" — the market literally has buying support at those strikes.

**How to read it:**
- PCR > 1.3: Very bullish positioning. But if sustained too long, can mean complacency (contrarian bearish at extremes >1.5)
- PCR 0.9 - 1.2: Neutral to mildly bullish
- PCR < 0.8: Bearish positioning. Market likely capped.
- PCR < 0.5: Extreme fear. Contrarian buy signal.
- **OI Change (more important than absolute OI):** Look at which strikes gained OI yesterday. If 24000 CE gained 50 lakh OI, that's a ceiling. If 23500 PE gained 50 lakh OI, that's a floor. Your likely range is between these two walls.
- **Max Pain:** Market drifts toward max pain as expiry approaches (strongest on Thursday expiry). Midweek, it's less relevant.

**Where to check:** https://www.opstra.definedge.com/open-interest (Opstra is best for OI visualization) or https://www.nseindia.com/option-chain (official NSE data)

**Frequency:** Daily, before market open. This is your "what are institutions positioned for?" check.

---

### 4. US Markets Close + Dollar Index (DXY)

**What it is:** How S&P 500, Nasdaq, and the US Dollar Index closed overnight.

**Why it matters:** Nifty has a ~0.6 correlation with S&P 500 overnight moves. This isn't random — FII allocation is global. When US markets fall, global risk-off begins: FIIs sell EM (India), buy dollars (DXY up), which weakens INR, which accelerates FII selling. The chain: US down → DXY up → INR weak → FII sell India → Nifty down. Reverse for bullish.

**How to read it:**
- S&P 500 down >1%: Nifty will open weak. Be defensive. Don't buy the open.
- S&P 500 up >1%: Nifty will gap up. But don't chase — gap fills are common.
- DXY above 105: Structural headwind for all emerging markets including India.
- DXY below 100: Structural tailwind. FII money flows to EM.
- **The nuance:** India sometimes decouples from US for days/weeks (strong domestic flows). But when US falls >2% in a day, India NEVER decouples. Respect large US moves.

**Where to check:**
- S&P/Nasdaq: Google "S&P 500" (shows after-hours too)
- DXY: https://www.tradingview.com/symbols/TVC-DXY/

**Frequency:** Every morning, as part of the Gift Nifty check (Gift Nifty already reflects this, but knowing the WHY helps you gauge persistence).

---

### 5. India VIX

**What it is:** The "fear gauge" — NSE's volatility index. It measures how much volatility option prices are implying for the next 30 days. VIX of 15 means options market expects ~15% annualized moves (or ~1% daily swings).

**Why it matters:** VIX tells you whether to trade large or small. High VIX = wide swings = use smaller position sizes. Low VIX = tight range = can use larger positions. The causal mechanism: VIX rising means option premiums are expensive (fear is being priced in). VIX falling means complacency. For option buyers: high VIX = expensive options, you pay more premium. For option sellers: high VIX = juicy premiums but higher risk.

**How to read it:**
- VIX < 12: Extreme complacency. Market in tight range. Option selling works great BUT sudden spike risk is highest here. This is the "calm before storm" zone.
- VIX 12-16: Normal conditions. No special action needed.
- VIX 16-22: Elevated fear. Good for option sellers if you can handle swings. Market is nervous.
- VIX > 22: High fear. Don't sell options naked. Market is in crisis mode. Usually near a bottom for equities (contrarian buy in cash market).
- VIX > 30: Rare. Full panic. Buy equities for investment, stay away from options trading.
- **Key insight:** VIX RISES faster than it falls. A spike from 12 to 25 can happen in 2 days. A fall from 25 to 12 takes weeks. This asymmetry matters for position sizing.

**Where to check:** https://www.nseindia.com/products/content/equities/indices/india-vix.htm or simply Google "India VIX"

**Frequency:** Daily. This is your risk-sizing tool.

---

## TIER 2: Check 2-3x Per Week (Context Indicators)

These provide medium-term context. They don't change daily in meaningful ways.

---

### 6. Market Breadth (Advance/Decline Ratio + % Stocks Above 50 DMA)

**What it is:** A/D Ratio = number of stocks advancing ÷ declining on NSE. % above 50 DMA = what fraction of Nifty 500 stocks are in uptrends.

**Why it matters:** Breadth divergence is one of the most reliable topping signals in any market. When Nifty makes new highs but breadth narrows (fewer stocks participating), the rally is unhealthy and likely to reverse. Causal mechanism: A narrow rally means only a few heavyweights (Reliance, HDFC Bank, etc.) are dragging the index up while most stocks fall. This means institutional money is concentrating, not broadening — a sign of late-cycle positioning.

**How to read it:**
- Nifty up + >60% stocks above 50 DMA: Healthy bull market. Stay long.
- Nifty up + <40% stocks above 50 DMA: DIVERGENCE. The index is lying. Topping risk is high. Reduce longs.
- Nifty down + breadth improving (more stocks above 50 DMA): Bottoming signal. Market is healing even as index is flat.
- A/D Ratio > 2:1 for several days: Strong breadth thrust. Very bullish for next 1-3 months.
- **Why this is Tier 2 not Tier 1:** Breadth changes slowly. It's a multi-day/week signal. Checking it daily is overkill for a non-intraday trader.

**Where to check:** https://www.icharts.in/market-breadth-nifty500-charts.php or https://chartink.com/screener/nifty-500-stocks-above-50-dma

**Frequency:** 2-3x per week (Monday, Wednesday, Friday)

---

### 7. USDINR (Rupee vs Dollar)

**What it is:** How many rupees one US dollar buys. Higher = weaker rupee.

**Why it matters:** Rupee weakness is both a SYMPTOM and a CAUSE of FII selling. The feedback loop: FIIs sell Indian stocks → convert INR to USD → rupee weakens → FII losses deepen (currency + equity) → they sell more. RBI intervenes to slow this (sells dollars from reserves), but can only slow, not stop structural moves. A stable/strengthening rupee means FIIs are not panicking.

**How to read it:**
- INR depreciating slowly (5-7% annually): Normal, don't worry. India runs a current account deficit, gradual depreciation is structural.
- INR depreciating fast (>1% in a week): Stress signal. FIIs are likely dumping. Be defensive.
- INR appreciating: Rare and very bullish. Means strong FII inflows overpowering structural deficit.
- RBI interventions (reserves declining): They're fighting depreciation. If reserves drop >$10B in a month, FII outflows are serious.
- **Key level to watch:** Whenever USDINR hits a round number all-time high (e.g., crosses 84, 85, 86), media panic increases but it's usually already priced in. The RATE of change matters more than the level.

**Where to check:** https://www.tradingview.com/symbols/USDINR/ or Google "USDINR"

**Frequency:** 2-3x per week. Only becomes Tier 1 during periods of rapid rupee weakness.

---

### 8. Crude Oil (Brent)

**What it is:** Global benchmark price for crude oil in USD/barrel.

**Why it matters:** India imports ~85% of its crude oil. Every $10/bbl increase in crude costs India ~$15 billion annually, widening the current account deficit, weakening INR, increasing inflation, and forcing RBI to keep rates higher. The causal chain for markets: Crude up → India's import bill up → CAD widens → INR weakens → inflation rises → RBI keeps rates high → equity valuations compress. Oil-sensitive stocks (OMCs, airlines, paints) move directly.

**How to read it:**
- Brent $60-75: Goldilocks for India. Low enough to not stress macro, high enough that energy stocks survive.
- Brent $75-90: Mild headwind. Inflation starts creeping up. Not a crisis.
- Brent >$90: Significant headwind for Indian markets. Inflation expectations rise, RBI turns hawkish.
- Brent >$100: Full macro stress. Short OMCs (BPCL, HPCL, IOC), avoid rate-sensitive stocks.
- Brent <$60: Tailwind for India. But may signal global recession (bad for Nifty for other reasons).

**Where to check:** Google "Brent crude price" or https://www.tradingview.com/symbols/TVC-UKOIL/

**Frequency:** 2-3x per week. Only daily during geopolitical crises (Middle East escalation, OPEC surprises).

---

### 9. Sector Rotation (Weekly, Not Intraday)

**What it is:** Which sectors are leading/lagging over the past 5-20 trading sessions.

**Why it matters:** Sector rotation tells you what PHASE of the market cycle we're in. Early bull markets: metals, banks rally first. Late bull markets: defensives (pharma, FMCG, IT) outperform. Rotation from cyclicals to defensives is a warning sign. Causal mechanism: Smart institutional money rotates early. If banks (rate-sensitive) start outperforming, institutions expect rate cuts. If IT starts outperforming, they expect rupee weakness (IT earns in USD).

**How to read it:**
- Banks outperforming: Institutions expect rate cuts or economic acceleration. Bullish for Nifty.
- IT outperforming: Usually happens during rupee weakness or US demand strength. Can be bullish or defensive.
- FMCG/Pharma outperforming while Nifty is flat/up: Defensive rotation. Late cycle. Be cautious.
- Metals/Realty outperforming: Early cycle / liquidity-driven rally. Bullish but volatile.
- PSU Banks outperforming Pvt Banks: Retail/speculative fervor. Usually late-stage bull market.

**Where to check:** https://www.tradingview.com — compare NIFTYBANK, NIFTYIT, NIFTYPHARMA, NIFTYMETAL relative performance. Or Moneycontrol sector heatmap.

**Frequency:** 2x per week (Monday and Thursday). NOT intraday — that's noise for a once-a-day checker.

---

### 10. US 10-Year Treasury Yield

**What it is:** The interest rate the US government pays on 10-year bonds. The global "risk-free rate."

**Why it matters:** This is the denominator in EVERY global valuation model. When US 10Y rises, the discount rate for all risky assets rises, compressing valuations worldwide. For India specifically: higher US yields → wider US-India rate differential → FIIs prefer US bonds over Indian equities → outflows from India. The causal chain: US 10Y up → FII sell India → Nifty falls + INR weakens.

**How to read it:**
- US 10Y < 4.0%: Supportive for EM equities including India. FII flows likely positive.
- US 10Y 4.0-4.5%: Neutral. Not driving flows either way.
- US 10Y > 4.5%: Headwind for India. FIIs have a compelling "safe" alternative in US bonds.
- US 10Y > 5.0%: Major headwind. Last seen in Oct 2023 — corresponded with heavy FII selling.
- **Rate of change matters more than level.** A sudden 30bps spike in a week is more damaging than a slow grind from 4% to 4.5% over months.

**Where to check:** https://www.tradingview.com/symbols/TVC-US10Y/ or Google "US 10 year yield"

**Frequency:** 2-3x per week.

---

## TIER 3: Check Weekly/Monthly (Structural & Macro)

These set the long-term backdrop. They don't change fast enough to matter daily.

---

### 11. RBI Policy Rate + Stance

**What it is:** The repo rate (rate at which RBI lends to banks) and the monetary policy stance (accommodative, neutral, or tightening).

**Why it matters:** Interest rates are the single biggest structural driver of equity valuations. Lower rates → cheaper borrowing → higher corporate earnings → higher PE multiples → stocks go up. The stance matters more than individual rate decisions because it signals DIRECTION. If RBI shifts from "tightening" to "neutral," rate cuts are coming even before they happen — and markets price this in immediately.

**How to read it:**
- Rate cut cycle beginning: Extremely bullish for rate-sensitive sectors (banks, realty, auto). Nifty typically rallies 15-25% during cutting cycles.
- Rate hike cycle beginning: Bearish for valuations. Banks may actually rally (higher NIMs) but broader market struggles.
- Pause/neutral stance: Market focuses on other factors. Rates are not the driver.
- **Look for:** RBI commentary on inflation vs growth tradeoff. If they prioritize growth, cuts are coming.

**Where to check:** https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx (RBI website, policy statements)

**Frequency:** Every 6 weeks (when MPC meets). Read the statement day-of. Then ignore until next meeting.

---

### 12. India CPI Inflation

**What it is:** Consumer Price Inflation — how fast prices are rising for the average Indian.

**Why it matters:** Inflation is RBI's constraint. If inflation is high, RBI CANNOT cut rates even if growth demands it. For markets: low inflation = room for rate cuts = bullish. High inflation = rates stay high or rise = bearish. The RBI targets 4% with a ±2% band. Below 4% is paradise for equities.

**How to read it:**
- CPI < 4%: RBI has room to cut. Bullish structural setup.
- CPI 4-5%: Neutral. RBI can stay accommodative.
- CPI 5-6%: RBI on watch. Unlikely to cut, may hike if persistent.
- CPI > 6%: RBI must act. Rate hikes coming. Bearish for equities.
- **Food inflation** drives India's CPI. It's monsoon-dependent and volatile. Core inflation (ex-food, ex-fuel) is what RBI actually watches for policy decisions.

**Where to check:** https://mospi.gov.in/ (released around 12th of every month for prior month)

**Frequency:** Monthly. Mark release date on calendar.

---

### 13. India GDP Growth + PMI

**What it is:** GDP = total economic output growth. PMI (Purchasing Managers Index) = monthly survey of manufacturing/services activity. PMI > 50 = expansion, < 50 = contraction.

**Why it matters:** GDP growth justifies equity valuations. India trading at 20+ PE requires 6-7%+ GDP growth. If growth slows, valuation compression follows. PMI is the real-time proxy — it comes monthly (vs GDP quarterly) and is forward-looking (it asks about NEW orders, not past output).

**How to read it:**
- Manufacturing PMI > 55: Strong expansion. Bullish for industrials, capex plays.
- Services PMI > 55: Strong domestic economy. Bullish for banks, consumers.
- PMI 50-52: Slowing. Watch for trend.
- PMI < 50: Contraction. Rare for India. Very bearish if sustained.
- **GDP surprise matters more than absolute level.** If consensus expects 6.5% and actual is 7.2%, that's bullish. If consensus is 7% and actual is 6.8%, bearish even though 6.8% is good.

**Where to check:** PMI: https://www.pmi.spglobal.com/Public/Release/PressReleases (S&P Global India PMI, released 1st of every month). GDP: MOSPI website (quarterly).

**Frequency:** Monthly (PMI on 1st), Quarterly (GDP).

---

### 14. Global Liquidity / Fed Policy

**What it is:** Whether the US Federal Reserve is adding or removing liquidity from the global financial system (QE vs QT), and the direction of Fed Funds rate.

**Why it matters:** Global liquidity is the TIDE that lifts or sinks all boats. When the Fed is easing (cutting rates, doing QE), money flows to risky assets including EM. When the Fed is tightening, money flows back to USD. India's 2020-21 bull run was fueled by Fed QE. The 2022 correction was caused by Fed tightening. This is the single most important macro variable for multi-month Nifty direction.

**How to read it:**
- Fed cutting + QE: Strongest possible tailwind for Indian equities. Be aggressively long.
- Fed pausing (done hiking, not yet cutting): Usually okay. Market anticipates cuts.
- Fed hiking: Headwind. Each 25bps hike is incrementally bearish for EM.
- Fed doing QT (reducing balance sheet): Liquidity drain. Slow but persistent headwind.
- **The signal:** Watch Fed dot plots and CME FedWatch tool for rate expectations. Markets move on EXPECTATIONS, not actual decisions.

**Where to check:** https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html (probability of rate moves)

**Frequency:** Weekly check of FedWatch. Deep dive during FOMC weeks (8x per year).

---

### 15. FII Derivative Positioning (Long/Short Ratio)

**What it is:** The ratio of FII long positions to short positions in index futures, reported daily by NSE.

**Why it matters:** This is FIIs showing you their hand in derivatives. Unlike cash flows (which can be rebalancing), derivative positioning is directional. When FIIs are heavily short index futures, they expect markets to fall — and they often push markets in that direction through cash selling.

**How to read it:**
- FII Long/Short ratio > 70% long: Very bullish FII positioning. Market likely to sustain uptrend.
- FII Long/Short ratio 50-70% long: Neutral to mildly bullish.
- FII Long/Short ratio < 40% long (i.e., >60% short): Very bearish FII positioning. Expect selling pressure.
- FII ratio < 20% long: Extreme short positioning. Contrarian bullish (short covering rally likely).
- **Key insight:** When FII cash selling + derivative shorting align, the move down is real and sustained. When FIIs are selling cash but not shorting derivatives, the selling may be temporary rebalancing.

**Where to check:** https://www.nseindia.com/products/content/derivatives/equities/archieve_fo.htm (FII/DII derivative data) or Moneycontrol "FII DII Activity" section

**Frequency:** Weekly (Monday + Thursday, to see positioning before and after weekly expiry).

---

## MACRO FORCES THAT ACTUALLY MOVE NIFTY

Here's the honest hierarchy of what drives Indian market direction, ranked by importance:

### Structural (Sets the trend for months/quarters)
1. **FII flows direction** — Nothing else comes close for sustained trends
2. **US Fed policy cycle** — Determines global liquidity available for EM
3. **India's earnings growth** — Ultimately, stocks follow earnings. Nifty EPS growth of 15%+ sustains bull markets
4. **Oil prices** — India's Achilles heel. Every $10 rise is a macro tax

### Cyclical (Drives weeks-to-months moves)
5. **US Dollar (DXY) trend** — Strong dollar = weak EM. Weak dollar = strong EM.
6. **India rate cycle** — RBI cutting = bullish. RBI hiking = bearish.
7. **Global risk sentiment** — VIX, credit spreads, EM fund flows

### Tactical (Drives days-to-weeks moves)
8. **Options positioning** (PCR, max pain, OI changes)
9. **Gift Nifty / US market close** — Sets the opening tone
10. **Event calendar** — Expiry weeks, RBI policy, earnings season, elections

### What's NOISE for You:
- Daily GDP estimates from random economists
- CNBC-TV18 talking heads
- Social media "tips" and targets
- Gold price (weakly correlated with Nifty, not a driver)
- China markets (low correlation with India unless it's about FII rotation)
- Cryptocurrency moves (zero correlation)

---

## YOUR MORNING ROUTINE (10 Minutes)

**Step 1 (2 min):** Check Gift Nifty + US market close. Know your opening gap.

**Step 2 (3 min):** Check yesterday's FII/DII data. Know who's buying/selling.

**Step 3 (3 min):** Check Nifty PCR + OI at key strikes. Know your range and walls.

**Step 4 (1 min):** Check India VIX. Know your position size.

**Step 5 (1 min):** Glance at DXY and Crude. Know your macro backdrop.

**Decision framework after this routine:**
- Gift Nifty up + FII buying + PCR bullish + VIX low: BE AGGRESSIVE. Add to longs.
- Gift Nifty down + FII selling + PCR bearish + VIX rising: BE DEFENSIVE. Reduce exposure or hedge.
- Mixed signals: WAIT. Do nothing. Not every day requires action.

---

## THE ONE THING THAT MATTERS MOST

If you could track only ONE thing, track **FII cash market flows (5-day rolling sum)**.

Why: FIIs are marginal price setters in India. When they're buying consistently, market goes up. When they're selling consistently, market goes down. Everything else — technicals, options data, VIX — is downstream of this. It's not glamorous, it's not complex, but it's the closest thing to a single "is the market going up or down?" signal that exists for Indian equities.

The catch: It's a 1-day lagging indicator (you get yesterday's data today). But FII flow trends persist for weeks/months, so this lag is acceptable for a daily checker.

---

## INDICATORS YOU CAN SAFELY IGNORE

These are popular but add no edge for a once-daily amateur Nifty trader:

1. **RSI** — By the time RSI is "overbought," the move has happened. It tells you where you've been, not where you're going. Only useful as a mean-reversion signal on multi-week timeframes.

2. **Moving Averages (50/200 DMA)** — "Golden crosses" and "death crosses" are backtested to death and don't outperform in Indian markets. The media reports them; don't trade them.

3. **MACD** — Another lagging indicator. Derivative of moving averages. Tells you what already happened.

4. **Fibonacci levels** — No causal mechanism. Self-fulfilling prophecy at best, random noise at worst. The market doesn't know about Fibonacci.

5. **Astrology-based predictions** — Yes, this exists in Indian market culture. Obviously no causal mechanism.

6. **Daily FII/DII derivative activity in isolation** — Without context of cash flows and existing positioning, one day's derivative data is meaningless.

---

## CHEAT SHEET: Bull vs Bear Regime

**You're in a BULL regime when:**
- FIIs are net buyers (5-day rolling positive)
- India VIX is below 14 and falling
- Nifty PCR is above 1.0
- DXY is below 104 or falling
- More than 60% of Nifty 500 stocks above 50 DMA
- RBI is cutting rates or paused after cuts

**You're in a BEAR regime when:**
- FIIs are net sellers (5-day rolling negative, >₹2000 cr/day)
- India VIX is above 18 and rising
- Nifty PCR is below 0.7
- DXY is above 106 and rising
- Less than 35% of Nifty 500 stocks above 50 DMA
- RBI is hiking rates or inflation is above 6%

**In bull regimes:** Buy dips, sell options (puts), hold positions longer.
**In bear regimes:** Sell rallies, buy options (puts for protection), cut losses quickly.
**In mixed/transitional:** Reduce size, tighten stops, wait for clarity.

---

*Last updated: June 2025. Sources and links should be verified periodically as websites change.*
