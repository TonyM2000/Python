from flask import Flask, render_template, session, redirect, request
app=Flask(__name__)
app.secret_key='This is so secret'
@app.route("/")
def home():
    if 'visitcount' in session:
        session['visitcount'] += 1
    else:
        session['visitcount'] = 1
    if 'visits' in session:
        session['visits'] = (session['visits'])
    else:
        session['visits'] = 0
    if 'banana' in session:
        pass
    else:
        session['banana'] = {"addition":1}
    return render_template("index.html",visits=session['visits'],banana=session['banana']['addition'],visitcount=session['visitcount'])
@app.route("/destroy_session")
def death():
    session.clear()
    return redirect("/")
@app.route("/add")
def add():
    session['visits'] = (session['visits']+int(session['banana']['addition']))
    return redirect("/")
@app.route("/processing",methods=['POST'])#PROCESSING IS HERE
def post():
    session['banana'] = request.form
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)