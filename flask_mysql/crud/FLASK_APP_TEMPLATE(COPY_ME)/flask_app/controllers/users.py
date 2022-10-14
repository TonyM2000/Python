from flask_app.models.user import User
from flask import render_template,redirect,request,session,flash
from flask_app import app
@app.route("/")
def createuser():
    return render_template("index.html")

@app.route("/userprocessing",methods=["POST"])
def userprocessing():
    data = request.form
    id = User.save(data)
    return redirect(f"/viewuser/{id}")

@app.route("/viewall")
def viewall():
    data = User.getall()
    return render_template("viewall.html",users=data)

@app.route("/viewuser/<int:id>")
def viewuser(id):
    data = {"id":id}
    user = User.userinfo(data)
    print(user)
    return render_template("viewuser.html",user=user)

@app.route("/edituser/<int:id>")
def edituser(id):
    data = {"id":id}
    user = User.userinfo(data)
    return render_template("edituser.html",user=user)

@app.route("/editprocess", methods=["POST"])
def editprocess():
    data =  request.form
    User.update(data)
    id = request.form["id"]
    return redirect(f"/viewuser/{id}")

@app.route("/deleteprocess/<int:id>")
def deleteprocess(id):
    data = {"id":id}
    User.deleteuser(data)
    return redirect("/viewall")