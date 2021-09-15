from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os, random

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    teammate_names = ["Will St. Onge", "Will Sie", "Cory Knoll", "Anthony Bosch", "Justin Gallagher"]
    return render_template("index.html", app = app, teammate_names = teammate_names, dir = os.getcwd(), display = (random.randint(1, 10) == 1))

if __name__ == "__main__":
    app.run(debug = True)
