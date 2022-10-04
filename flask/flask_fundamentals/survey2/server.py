from flask import Flask, render_template,session, request, redirect
app=Flask(__name__)
app.secret_key="supersecret"

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def processing():
    session["name"] = request.form["username"]
    session["location"] = request.form["location"]
    session["languages"] = request.form["languages"]
    session["comments"] = request.form["comments"]
    return redirect("/result")

@app.route("/result")
def results():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)