import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)


@app.route("/about.html")
def about():
    return render_template("about.html")
