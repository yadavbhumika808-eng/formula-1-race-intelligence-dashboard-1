from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public embed addresses (views/WORKBOOK/SHEET format)
DASHBOARD_URL = "https://public.tableau.com/views/F1Racing_17931361367640/F1RacingIntelligenceDashboardAnalysisReport"
STORY_URL = "https://public.tableau.com/views/F1Racing_17931361367640/Story1"

# Normal links to open on Tableau Public
DASHBOARD_LINK = "https://public.tableau.com/app/profile/kanishka.arya/viz/F1Racing_17931361367640/F1RacingIntelligenceDashboardAnalysisReport"
STORY_LINK = "https://public.tableau.com/app/profile/kanishka.arya/viz/F1Racing_17931361367640/Story1"


@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL,
        dashboard_link=DASHBOARD_LINK,
        story_link=STORY_LINK,
    )


if __name__ == "__main__":
    app.run(debug=True)
