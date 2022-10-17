from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash
from flask_app import app

@app.route("/newninja")
def createninja():
    return render_template("newninja.html",dojos = Dojo.getall())

@app.route("/ninjaprocessing",methods=["POST"])
def ninjaprocessing():
    Ninja.save(request.form)
    return redirect("/")
