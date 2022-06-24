import requests

from flask import Flask, request, render_template


def get_data(query: str = None):
    res = requests.get("http://73a2-141-89-221-147.ngrok.io", params=query)

    return res


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("task.html")


@app.route("/invite")
def invite():
    return render_template("invite.html")


@app.route("/invite_success", methods=["GET", "POST"])
def invite_success():
    if request.method == "POST":
        pass
    return render_template("task.html")


if __name__ == "__main__":
    app.run()
