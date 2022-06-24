import json
import requests

from flask import Flask, request, render_template


def get_data(endpoint: str, query: dict = None):
    res = requests.get(f"http://73a2-141-89-221-147.ngrok.io{endpoint}", params=query)

    return res


def post_data(endpoint: str, query: str = None):
    res = requests.post(f"http://73a2-141-89-221-147.ngrok.io{endpoint}", data=query)

    return res


app = Flask(__name__)

CACHE = {"user": None}


@app.route("/")
def index():
    return render_template("task.html", user_name=CACHE.get("user"))


@app.route("/new_user")
def new_user():
    pass


@app.route("/new_user_added")
def new_user_success():
    return render_template("task.html", user_name=CACHE.get("user"))


@app.route("/invite")
def invite():
    return render_template("invite.html", user_name=CACHE.get("user"))


@app.route("/invite_success", methods=["GET", "POST"])
def invite_success():
    if request.method == "POST":
        data = post_data("/new_user", json.dumps({"name": f"{request.form['user']}"}))
    return render_template("task.html", user_name=CACHE.get("user"))


if __name__ == "__main__":
    app.run()
