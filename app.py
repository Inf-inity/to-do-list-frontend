import json
import requests

from flask import Flask, request, render_template


def get_data(endpoint: str, query: dict = None):
    res = requests.get(f"https://codenight.yannik-dittmar.de{endpoint}", params=query)

    return res


def post_data(endpoint: str, query: str = None):
    res = requests.post(f"https://codenight.yannik-dittmar.de{endpoint}", data=query)

    return res


app = Flask(__name__)

CACHE = {"id": 0, "user": None, "teams": []}


@app.route("/")
def index():
    return render_template("task.html", user_name=CACHE.get("user"), team_id=CACHE.get("teams"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logged_in", methods=["POST"])
def logged_in():
    if request.method == "POST":
        data = get_data(f"/users/by-name/{request.form['name']}")
        print(data)
    return render_template("task.html", user_name=CACHE.get("user"), team_id=CACHE.get("teams"))


@app.route("/new_user")
def new_user():
    return render_template("make_user.html")


@app.route("/make_user", methods=["POST"])
def new_user_success():
    if request.method == "POST":
        data = post_data("/users/new/", json.dumps({"Name": f"{request.form['user']}"}))
    return render_template("task.html", user_name=CACHE.get("user"))


@app.route("/invite")
def invite():
    return render_template("invite.html", user_name=CACHE.get("user"))


@app.route("/invite_success", methods=["GET", "POST"])
def invite_success():
    return render_template("task.html", user_name=CACHE.get("user"))


@app.route("/new")
def new():
    return render_template("new_task.html", user_name=CACHE.get("user"), team_id=CACHE.get("teams"))


@app.route("/new_task", methods=["GET", "POST"])
def added_task():
    if request.method == "POST":
        data = post_data("/tasks/new/", json.dumps({
            "Owner": CACHE.get('id'),
            "Title": f"{request.form['title']}",
            "Description": f"{request.form['desc']}",
            "Priority": int(request.form['prio']),
            "Deadline": f"{request.form['time']}T00:00:00Z"
        }))
    return render_template("task.html", user_name=CACHE.get("user"), team_id=CACHE.get("teams"))


@app.route("/profile")
def profile():
    pass


@app.route("/all_teams")
def get_teams():
    data = get_data(f"/users/{CACHE.get('id')}/")
    print(data)
    return render_template("teams.html", user_name=CACHE.get("user"), team_id=CACHE.get("teams"))


if __name__ == "__main__":
    app.run()
