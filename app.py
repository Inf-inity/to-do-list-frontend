import requests

from flask import Flask, render_template


def get_data(query: str = None):
    res = requests.get("http://73a2-141-89-221-147.ngrok.io", params=query)

    return res


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("task.html")


if __name__ == "__main__":
    app.run()
