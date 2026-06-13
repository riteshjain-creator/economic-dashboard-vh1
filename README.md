# Economic Dashboard V-H1

A personal economic intelligence page. Signal over noise. First-principles reasoning for investment decisions.

**Live:** [GitHub Pages URL — TBD after deploy]

---

## What This Is

- A single webpage you check daily at 8AM
- Mobile-first: bias + indicators + threats in text
- Web: adds interactive charts + full weekly analysis
- Updated automatically by Hermes cron jobs
- No APIs to maintain. No data pipelines. No backend.

## What This Is NOT

- Not a professional trading terminal
- Not real-time (daily refresh)
- Not a recommendation engine ("buy X")
- Not multi-user

## Architecture

All intelligence lives in Hermes cron jobs on the server.  
The page is a dumb reader of `dashboard-data.json`.

Three loops:
1. **Daily (8AM):** Morning bias + indicator values + event flags
2. **Weekly (Sat 2PM):** Deep synthesis per threat + POV + backlog scan
3. **Monthly (1st):** Structural review — refresh threats, models, indicators

## Repo Structure

```
economic-dashboard-vh1/
├── BLUEPRINT.md          # Full system design (you're here ↑)
├── README.md             # This file
├── index.html            # The dashboard page (GitHub Pages)
├── dashboard-data.json   # Data file (updated by cron)
└── assets/
    └── style.css         # Extracted styles (optional)
```

## Setup

1. Enable GitHub Pages on `main` branch
2. Hermes cron jobs handle all updates
3. Open the page. That's it.

---

**Started:** June 2025  
**Version:** H1 (Hermes-native, first rewrite)  
**Status:** Blueprint complete. Building Phase 0.
