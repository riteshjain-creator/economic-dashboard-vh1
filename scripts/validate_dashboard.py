#!/usr/bin/env python3
"""
validate_dashboard.py — Phase 4 health check.
Run manually or as a one-off test to verify the full pipeline works.
Usage: python3 scripts/validate_dashboard.py
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path(__file__).parent.parent
DATA_FILE = REPO / "dashboard-data.json"
IST = timezone(timedelta(hours=5, minutes=30))

PASS = "✅"
WARN = "⚠️ "
FAIL = "❌"

errors = []
warnings = []

def check(label, condition, warn=False, detail=""):
    sym = PASS if condition else (WARN if warn else FAIL)
    msg = f"{sym} {label}"
    if detail:
        msg += f"  [{detail}]"
    print(msg)
    if not condition:
        if warn:
            warnings.append(label)
        else:
            errors.append(label)


print("=" * 50)
print("DASHBOARD VALIDATION — Economic Dashboard V-H1")
print("=" * 50)

# 1. File exists
check("dashboard-data.json exists", DATA_FILE.exists())
if not DATA_FILE.exists():
    print(f"\n{FAIL} Cannot continue — data file missing.")
    sys.exit(1)

# 2. Valid JSON
try:
    data = json.loads(DATA_FILE.read_text())
    check("JSON parses cleanly", True)
except json.JSONDecodeError as e:
    check("JSON parses cleanly", False, detail=str(e))
    sys.exit(1)

# 3. Schema — top-level keys
for key in ["meta", "daily", "weekly", "config", "history"]:
    check(f"Top-level key '{key}' present", key in data)

meta = data.get("meta", {})
daily = data.get("daily", {})
weekly = data.get("weekly", {})
config = data.get("config", {})
history = data.get("history", {})

# 4. Meta
check("meta.last_updated present", bool(meta.get("last_updated")))
check("meta.version present", bool(meta.get("version")))

# 5. Staleness
last_updated_str = meta.get("last_updated")
if last_updated_str:
    try:
        last_updated = datetime.fromisoformat(last_updated_str)
        now = datetime.now(IST)
        age_hours = (now - last_updated).total_seconds() / 3600
        check("Data updated within 48h", age_hours < 48, warn=True, detail=f"{age_hours:.1f}h ago")
        if age_hours > 24:
            check("Data updated within 24h", False, warn=True, detail="Daily cron may have missed")
    except ValueError as e:
        check("meta.last_updated parses as datetime", False, detail=str(e))

# 6. Daily section
check("daily.bias present", bool(daily.get("bias")))
check("daily.bias is valid value", daily.get("bias") in ("bullish", "cautious", "neutral", "bearish"),
      detail=daily.get("bias"))
check("daily.confidence present", bool(daily.get("confidence")))
check("daily.indicators present", bool(daily.get("indicators")))

indicators = daily.get("indicators", {})
for ind in ["nifty", "vix", "usdinr", "pcr", "breadth", "fii", "crude", "mmi"]:
    present = ind in indicators
    check(f"indicator '{ind}' present", present)
    if present:
        val = indicators[ind].get("value", "--")
        check(f"  '{ind}' has non-empty value", val not in ("", None), warn=True,
              detail=f"value={val}")

# 7. Weekly section
check("weekly.summary present", bool(weekly.get("summary")))
check("weekly.market_posture present", bool(weekly.get("market_posture")), warn=True)
threads = weekly.get("threads", [])
check("weekly.threads non-empty", len(threads) > 0, detail=f"{len(threads)} threads")
check("weekly.threads ≤ 4", len(threads) <= 4, warn=True, detail=f"{len(threads)} threads")

for i, t in enumerate(threads):
    for field in ["name", "status", "pov", "watch_next_week"]:
        check(f"  thread[{i}].{field} present", bool(t.get(field)), warn=True)
    check(f"  thread[{i}].status valid", t.get("status") in ("red", "yellow", "green"), warn=True,
          detail=t.get("status"))

# 8. Config
config_threads = config.get("threads", [])
check("config.threads non-empty", len(config_threads) > 0)
check("config.decay_warning_at present", bool(config.get("decay_warning_at")), warn=True)

# 9. History scaffold
check("history.daily_biases is list", isinstance(history.get("daily_biases"), list))
check("history.weekly_povs is list", isinstance(history.get("weekly_povs"), list))

# 10. Scripts exist
for script in ["daily_scan.py", "weekly_synthesis.py", "monthly_review.py"]:
    check(f"scripts/{script} exists", (REPO / "scripts" / script).exists())

# 11. index.html exists
check("index.html exists", (REPO / "index.html").exists())

# Summary
print()
print("=" * 50)
total = len(errors) + len(warnings)
if not errors and not warnings:
    print(f"{PASS} ALL CHECKS PASSED — dashboard is healthy")
elif not errors:
    print(f"{WARN} {len(warnings)} warning(s), no blocking errors")
    for w in warnings:
        print(f"   ⚠️  {w}")
else:
    print(f"{FAIL} {len(errors)} error(s), {len(warnings)} warning(s)")
    for e in errors:
        print(f"   ❌ {e}")
    for w in warnings:
        print(f"   ⚠️  {w}")

print("=" * 50)
sys.exit(1 if errors else 0)
