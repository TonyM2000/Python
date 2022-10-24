from flask_app.models.burger_model import Burger
from flask import render_template,redirect,request,session,flash
from flask_app import app
@app.route('/create', methods=['POST'])
def create_burger():
    data = {
        "name" : request.form['name'],
        "bun" : request.form['bun'],
        "meat" : request.form['meat'],
        "calories" : request.form['calories']
    }

    Burger.save(data)
    return redirect('/burgers')
# if there are errors:
# We call the staticmethod on Burger model to validate
    if not Burger.validate_burger(request.form):
# redirect to the route where the burger form is rendered.
        return redirect('/')
# else no errors:
    Burger.save(request.form)
    return redirect("/burgers")