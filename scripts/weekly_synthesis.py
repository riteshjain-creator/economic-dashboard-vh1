#!/usr/bin/env python3
"""
Weekly synthesis script for Economic Dashboard V-H1.
Runs Saturday 2PM IST (8:30 UTC).
Archives previous week's POV, updates weekly section,
pushes dashboard-data.json.
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


def archive_weekly_pov(data):
    """Archive previous week's POV to history (keep last 8 weeks)."""
    history = data.get("history", {})
    povs = history.get("weekly_povs", [])
    previous = data.get("weekly", {})
    if previous.get("date") and previous.get("summary"):
        povs.append({
            "date": previous["date"],
            "summary": previous["summary"],
            "market_posture": previous.get("market_posture", ""),
            "threads": previous.get("threads", []),
        })
    data["history"]["weekly_povs"] = povs[-8:]


def update_weekly(data, new_weekly):
    """Archive previous week, replace weekly section."""
    archive_weekly_pov(data)
    data["weekly"] = new_weekly
    data["meta"]["last_updated"] = datetime.now(IST).isoformat()
    data["meta"]["last_loop2"] = datetime.now(IST).isoformat()

    # Update thread statuses in config to match weekly assessment
    thread_map = {t["name"]: t["status"] for t in new_weekly.get("threads", [])}
    for t in data.get("config", {}).get("threads", []):
        if t["name"] in thread_map:
            t["status"] = thread_map[t["name"]]

    # Move any new backlog items to config if promoted
    for backlog_item in new_weekly.get("promoted_threads", []):
        data["config"]["threads"].append({
            "name": backlog_item["name"],
            "added": datetime.now(IST).strftime("%Y-%m-%d"),
            "models": backlog_item.get("models", []),
            "status": backlog_item.get("status", "yellow")
        })


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: weekly_synthesis.py '<json_payload>'", file=sys.stderr)
        sys.exit(1)

    try:
        new_weekly = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"Invalid JSON payload: {e}", file=sys.stderr)
        sys.exit(1)

    data = load_data()
    update_weekly(data, new_weekly)
    save_data(data)

    today = datetime.now(IST).strftime("%Y-%m-%d")
    posture = new_weekly.get("market_posture", "")[:50]
    git_push(f"weekly: {today} synthesis — {posture}")
    print(f"Weekly synthesis complete.")
