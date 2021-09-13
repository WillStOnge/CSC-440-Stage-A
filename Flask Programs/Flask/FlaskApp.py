from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/food')
def food():
    return render_template('food.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ =="__main__":
    # starts the server and flask application
    # debug=True should only be in dev environment, not production
    app.run(debug=True)