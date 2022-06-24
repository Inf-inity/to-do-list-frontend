import requests

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("task.html")


@app.route("/team_invite")
def team_invite():
    pass


if __name__ == "__main__":
    app.run()
