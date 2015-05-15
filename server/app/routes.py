from flask import Flask, render_template, request
from models import db

# set up app
app = Flask(__name__)
db.init_app(app)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.context_processor
def add_pages():
    return {"pages" : Navbar().routes}

@app.route("/")
def homepage():
    title = False
    return render_template("pages/home.jade", title=title)

@app.route("/completed")
def about():
    title = "Completed Tasks"
    return render_template("pages/about.jade", title=title)

@app.route("/task/<task_id>", methods=["GET", "POST"])
def addform():
    if request.method == "POST":
        # process the update
        pass
    else:
        # render the task details
        title = "Task Details"
        return render_template("task-detail.jade", title=title)

# @app.route("/competitions")
# def competitions():
#     title = gettext("Competitions")
#     return render_template("pages/competitions.jade", title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.jade"), 404

@app.errorhandler(500)
def site_down(e):
    return render_template("500.jade", error=e), 500

# helper methods
class Navbar:
    def __init__(self, other_routes=[]):
        self.routes = [
            {
                "url": "/about",
                "title": "About",
            },
            {
                "url": "/teams",
                "title": "Teams",
            },
            {
                "url": "/add-new-team",
                "title": "Add Your Team",
            },
        ]

        if other_routes:
            self.routes += other_routes
