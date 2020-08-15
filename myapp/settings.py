import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE.URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisIsMySuperSecretKey' or 'mySecuritySalt'

MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
MAIL_PORT = os.environ.get('MAIL_PORT') or 465
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'lynnsclan@gmail.com'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '!Sherri10!'
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or '"MyApp" <noreply@example.com>'
USER_APP_NAME = os.environ.get('USER_APP_NAME') or "Brian Moser Sports App"      
USER_ENABLE_USERNAME = os.environ.get('USER_ENABLE_USERNAME')  or False
USER_EMAIL_SENDER_NAME = os.environ.get('USER_EMAIL_SENDER_NAME') or USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = os.environ.get('USER_EMAIL_SENDER_EMAIL') or "noreply@example.com"
USER_COPYRIGHT_YEAR = os.environ.get('USER_COPYRIGHT_YEAR') or '2020' 
USER_CORPORATION_NAME = os.environ.get('USER_CORPORATION_NAME') or 'BM Sports Ltd.' 