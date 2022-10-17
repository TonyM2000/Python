from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash
from flask_app import app

@app.route("/")
def createdojo():
    return render_template("index.html",dojos = Dojo.getall())

@app.route("/dojoprocessing",methods=["POST"])
def dojoprocessing():
    Dojo.save(request.form)
    return redirect("/alldojos")

@app.route("/alldojos")
def alldojos():
    data = Dojo.getall()
    return render_template("index.html",dojos=data)

@app.route("/viewdojo/<int:id>")
def viewdojo(id):
    data = {"id":id}
    dojo = Dojo.dojoinfo(data)
    print(dojo)
    return render_template("viewdojo.html",dojos=dojo)
