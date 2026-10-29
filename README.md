# F1 Racing Intelligence Dashboard

An interactive Tableau dashboard and data story on F1 racing, shown together on one page using a Flask web app.

## Links
- Dashboard: https://public.tableau.com/app/profile/kanishka.arya/viz/F1Racing_17931361367640/F1RacingIntelligenceDashboardAnalysisReport
- Story: https://public.tableau.com/app/profile/kanishka.arya/viz/F1Racing_17931361367640/Story1

## Files
- `app.py` - Flask app
- `templates/index.html` - page layout with embedded Tableau views
- `requirements.txt` - Python packages

## Run locally
```
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000

## Deploy (Render)
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
