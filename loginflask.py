import flask_login
from flask import Flask, redirect, Response, url_for, request
from flask_cors import CORS, cross_origin
from user import User
import usersdb as udb

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "thisMustBeSecret"
app.config['SESSION_COOKIE_HTTPONLY'] = False


# Init the flask-login
from loginmanager import login_manager
login_manager.init_app(app)

# Enable CORS
CORS(app, supports_credentials=True, resources={r'/*': {'origins': 'localhost:8080'}})

@app.route('/login', methods=['GET', 'POST'])
@cross_origin()
def login():
	global _users
	# it doesn't apply, the SPA won't send GET requests
	if request.method == 'GET':
		pass
	data = request.form
	name = data['name']
	if udb.userExists(name):
		if udb.userLogin(name, data['password']):
			user1 = User()
			user1.id = name
			user1.uid = name
			flask_login.login_user(user1)
			return redirect(url_for('protected'), code=307)
	error = "Wrong Username or Password"
	return Response(error, status=200, mimetype='text/plain')

@app.route('/postlogin', methods=['POST'])
@flask_login.login_required
@cross_origin()
def protected():
	return Response('Logged in as: {0}'.format(flask_login.current_user.id), status=200, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=False)