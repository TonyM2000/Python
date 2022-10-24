from flask import Flask, render_template
from flask_app import app
from flask_app.controllers import burger_controller

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)