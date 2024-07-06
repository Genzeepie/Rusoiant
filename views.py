from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def Rusoniatchat():
    return render_template("index.html")


