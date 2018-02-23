from domain.user import User


class InMemUserRepository(object):

    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        self.users[user_id] = User(user_id)


    def find_user(self, user_id):
        return self.users[user_id]
