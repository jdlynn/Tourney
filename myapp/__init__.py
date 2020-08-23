from flask import Flask

from .routes import main
from .commands import commands
from .extentions import db, migrate, mail
from .models import User, Role
from flask_user import current_user, login_required, roles_required, UserManager
from .forms import CustomUserProfileForm
    

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(commands)
    
    class CustomUserManager(UserManager):
        def customize(self, app):
            self.EditUserProfileFormClass = CustomUserProfileForm
    
    user_manager = CustomUserManager(app, db, User)

    return app
