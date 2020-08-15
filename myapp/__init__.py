from flask import Flask

from .routes import main
from .commands import commands
from .extentions import db, migrate, mail
from .models import User, Role
from flask_user import current_user, login_required, roles_required, UserManager


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    migrate.init_app(app, db)
    user_manager = UserManager(app, db, User)
    mail.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(commands)
    
    return app
