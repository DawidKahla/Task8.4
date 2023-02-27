from flask import Flask
from flask import render_template, request, redirect


app = Flask(__name__)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        print("We received GET")
        return render_template("kontakt.html")
    elif request.method == "POST":
        print("We received POST")
        print(request.form)
        return redirect("/contact")


@app.route("/me", methods=["GET"])
def me():
    if request.method == "GET":
        print("We received GET")
        return render_template("o_mnie.html")
