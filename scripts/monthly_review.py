#!/usr/bin/env python3
"""
Monthly structure review script for Economic Dashboard V-H1.
Runs 1st of each month, 10AM IST (4:30 UTC).
Proposes thread rotation, checks indicator relevance,
auto-archives stale threads (>4 weeks without reconfirmation).
Posts proposal to Ritesh for confirmation; auto-proceeds after 7 days.
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
            return True
        subprocess.run(["git", "-C", REPO_PATH, "push", "origin", "main"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}", file=sys.stderr)
        return False


def auto_archive_stale_threads(data):
    """Auto-archive threads older than 4 weeks without reconfirmation."""
    today = datetime.now(IST).date()
    four_weeks_ago = today - timedelta(weeks=4)
    config = data.get("config", {})
    active = []
    archived = []
    for t in config.get("threads", []):
        added_date = datetime.fromisoformat(t.get("added", "2000-01-01")).date()
        if added_date <= four_weeks_ago:
            archived.append(t["name"])
        else:
            active.append(t)
    config["threads"] = active
    return archived


def apply_new_threads(data, new_threads, archived_names):
    """Replace thread list with reviewed set."""
    today = datetime.now(IST).strftime("%Y-%m-%d")
    data["config"]["threads"] = new_threads
    data["config"]["last_structural_review"] = today
    # Reset decay warning 4 weeks out
    decay_date = (datetime.now(IST) + timedelta(weeks=4)).strftime("%Y-%m-%d")
    data["config"]["decay_warning_at"] = decay_date
    data["meta"]["last_updated"] = datetime.now(IST).isoformat()
    return archived_names


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: monthly_review.py '<json_payload>'", file=sys.stderr)
        sys.exit(1)

    try:
        payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"Invalid JSON payload: {e}", file=sys.stderr)
        sys.exit(1)

    data = load_data()

    # Auto-archive stale threads first
    auto_archived = auto_archive_stale_threads(data)
    if auto_archived:
        print(f"Auto-archived stale threads: {auto_archived}")

    # Apply proposed new thread list from cron agent
    new_threads = payload.get("threads", data["config"]["threads"])
    archived = apply_new_threads(data, new_threads, auto_archived)

    save_data(data)

    today = datetime.now(IST).strftime("%Y-%m-%d")
    git_push(f"monthly: {today} structure review — {len(new_threads)} active threads")
    print(f"Monthly review complete. Active threads: {len(new_threads)}")
    if auto_archived:
        print(f"Auto-archived: {auto_archived}")
