from flask import Blueprint, render_template

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")

@second.route("/view")
def swag():
    return render_template("view.html")
@second.route("/peanits")
def peanits():
    return "<h1>peanits</h1>"