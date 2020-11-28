
from flask import Flask, render_template, Blueprint
from flask_login import login_required, current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
application = app

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# ---------- user authencation still needs database implementation---------
login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

# ---------- db Model probably goes here ---------




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def signup():
	return render_template('signup.html')

@app.route('/db', methods = ['GET', 'POST'])
def index():

	# ----- more db stuff probably goes here ------

	return render_template('index.html')

@app.route('/profile')
def profile():
	return render_template('profile.html', name=current_user.name)