from flask_login import LoginManager
from user import User
import usersdb as udb

login_manager = LoginManager()
login_manager.remember_cookie_httponly = False

@login_manager.user_loader
def load_user(name):
    r = udb.returnUser(name)
    if r > 0:
        user = User()
        user.id = name
        user.uid = r
        return user
    else:
        return

@login_manager.request_loader
def request_loader(request):
    name = request.form.get('name')
    # name = "pere"
    r = udb.returnUser(name)
    if r > 0:
        user = User()
        user.id = name
        user.uid = name
        user.is_authenticated = True
        return user
    else:
        return

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'