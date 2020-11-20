
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
application = app

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# ---------- db Model probably goes here ---------


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def signup():
	return 'signup coming soon'

@app.route('/db', methods = ['GET', 'POST'])
def index():

	# ----- more db stuff probably goes here ------

	return render_template('index.html')