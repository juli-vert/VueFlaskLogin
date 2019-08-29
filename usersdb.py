_users = {'user1': 'pass1', 'user2': 'pass2'}

def userExists(name):
	global _users
	if name in _users.keys():
		return True
	else:
		return False

def returnUser(name):
	global _users
	if name in _users.keys():
		return 1
	else:
		return 0

def userLogin(name, passw):
	global _users
	if _users[name]==passw:
		return True
	else:
		return False
