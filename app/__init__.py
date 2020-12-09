from flask import Flask, render_template, Blueprint
from flask_login import LoginManager, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
#from .models import User
#from config import config

app = Flask(__name__)
application = app

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    
    

    #app.config.from_object(config[config_name])
    #config[config_name].init_app(app)

    #bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app