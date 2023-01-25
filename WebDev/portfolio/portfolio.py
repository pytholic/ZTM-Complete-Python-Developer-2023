import os
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", mode="a") as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "Did not save to database."
    else:
        return "Something went wrong. Try again."


# @app.route("/works.html")
# def work():
#     return render_template("works.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")
