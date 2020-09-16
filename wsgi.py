from myapp import create_app
from myapp.models import db, User, Role

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Role': Role}