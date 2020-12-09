import os
import click
from flask_migrate import Migrate
from . import create_app, db
from .models import User, Achievement

#app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
application = app
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Achievement=Achievement)