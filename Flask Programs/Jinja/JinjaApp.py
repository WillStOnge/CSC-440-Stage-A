""""
Author      : Wie Lie Sie
Date        : 9/10/2021
Description :   JinjaApp program that will render index, student pages,
                TemplateNotFound exception is handled by returning 404 page
"""

from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from datetime import date

from jinja2 import TemplateNotFound

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.version = 'v.1'


@app.route('/', methods=['GET', 'POST'])
def index():
    today = date.today()
    first_name = 'Chuck'
    last_name = 'Liddell'
    name = first_name + " " + last_name

    try:
        return render_template('index.html', name=name, app=app, date=today)
    except TemplateNotFound:
        abort(404)


@app.route('/student', methods=['GET', 'POST'])
def student():
    student_information = {'classes': ['CSC-440 Software Engineering',
                                       'CSC-407 Concept of Programming Languages',
                                       'CSC-350 Database Programming'],
                           'semester': 'Fall 2021',
                           'college': 'NKU'}
    student_grades = {'CSC-440': 'A',
                      'CSC-407': 'A+',
                      'CSC-350': 'A'}
    try:
        return render_template('student.html', student_information=student_information, app=app,
                               student_grades=student_grades)
    except TemplateNotFound:
        abort(404)


@app.route('/financial', methods=['GET', 'POST'])
def financial():
    try:
        return render_template('financial.html')
    except TemplateNotFound:
        abort(404)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', error_code=404), 404


if __name__ == '__main__':
    app.run()
