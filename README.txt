Car SuperCard 13.5 — Stability Baseline

This release intentionally retains the exact working 13.3 index.html game code.
The only runtime change is a new service-worker cache version (135) to ensure clean deployment.
No economy, collection, save format, card data, or gameplay logic has been modified.

DEPLOY: Upload index.html and sw.js to the GitHub Pages repository root.
Keep existing icon/manifest/assets in place. Do not reset or clear game data.
After deploying, reload the app; if an installed PWA appears stale, close and reopen it.

This is a stabilization baseline, NOT a claim that all bugs or performance problems are fixed.
The included regression_check.py runs static syntax and preservation checks.
