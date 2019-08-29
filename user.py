class User:

    def __init__(self):
        id = 0
        uid = ""
        email = ""
        password = ""
        is_authenticated = False
        is_active = False
        is_anonymous = True

    def is_authenticated(self, user_id):
        return True

    def is_active(self, user_id):
        return True

    def is_anonymous(self, user_id):
        return False

    def get_id(self):
        return self.id