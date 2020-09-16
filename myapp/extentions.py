from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_user import UserMixin, login_required
from flask_admin import Admin


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
admin = Admin()
