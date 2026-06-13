#!/usr/bin/env python3
"""
Daily scan script for Economic Dashboard V-H1.
Runs at 8AM IST (2:30 UTC) Mon-Sat.
Fetches indicator data via web search, generates bias + commentary,
updates dashboard-data.json, git pushes.

Model split (per design):
- Data fetch/classify: Haiku (handled by cron prompt structure)
- Bias 3-liner commentary: Sonnet (this script produces structured context;
  the cron prompt uses Sonnet to write the actual commentary)
"""

import json
import subprocess
import sys
from datetime import datetime, timezone, timedelta

REPO_PATH = "/opt/data/economic-dashboard-vh1"
DATA_FILE = f"{REPO_PATH}/dashboard-data.json"
IST = timezone(timedelta(hours=5, minutes=30))


def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def git_push(message):
    try:
        subprocess.run(["git", "-C", REPO_PATH, "add", "dashboard-data.json"], check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", REPO_PATH, "commit", "-m", message],
            capture_output=True, text=True
        )
        if result.returncode != 0 and "nothing to commit" in result.stdout:
            print("Nothing to commit, skipping push.")
            return True
        subprocess.run(["git", "-C", REPO_PATH, "push", "origin", "main"], check=True, capture_output=True)
        print(f"Pushed: {message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}", file=sys.stderr)
        return False


def archive_daily_bias(data, previous_daily):
    """Keep last 30 daily biases in history."""
    history = data.get("history", {})
    biases = history.get("daily_biases", [])
    if previous_daily and previous_daily.get("date") and previous_daily.get("bias"):
        biases.append({
            "date": previous_daily["date"],
            "bias": previous_daily["bias"],
            "nifty": previous_daily.get("indicators", {}).get("nifty", {}).get("value", "--"),
            "fii": previous_daily.get("indicators", {}).get("fii", {}).get("value", "--"),
        })
    # Keep last 30
    data["history"]["daily_biases"] = biases[-30:]


def update_daily(data, new_daily):
    """Replace daily section, archive previous."""
    previous = data.get("daily", {})
    archive_daily_bias(data, previous)
    data["daily"] = new_daily
    data["meta"]["last_updated"] = datetime.now(IST).isoformat()
    data["meta"]["last_loop3"] = datetime.now(IST).isoformat()


def check_decay(data):
    """Warn if threads are getting stale."""
    config = data.get("config", {})
    decay_at = config.get("decay_warning_at")
    if decay_at:
        decay_date = datetime.fromisoformat(decay_at).date()
        today = datetime.now(IST).date()
        if today >= decay_date:
            print(f"⚠️  DECAY WARNING: Structural review due (was {decay_at}). Monthly review should have run.")


if __name__ == "__main__":
    # This script is called by the cron agent AFTER it has constructed
    # the new_daily dict. The cron prompt passes the JSON as first arg.
    if len(sys.argv) < 2:
        print("Usage: daily_scan.py '<json_payload>'", file=sys.stderr)
        sys.exit(1)

    try:
        new_daily = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"Invalid JSON payload: {e}", file=sys.stderr)
        sys.exit(1)

    data = load_data()
    update_daily(data, new_daily)
    check_decay(data)
    save_data(data)

    today = datetime.now(IST).strftime("%Y-%m-%d")
    bias = new_daily.get("bias", "neutral").upper()
    git_push(f"daily: {today} — bias {bias}")
    print(f"Daily scan complete. Bias: {bias}")
