import hashlib
from datetime import datetime


class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = is_active

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()


class Administrator(User):
    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else []


class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_last_login(self):
        self.last_login = datetime.now()


class GuestUser(User):
    def __init__(self, username):
        super().__init__(username, password="", is_active=True)

    def verify_password(self, password):
        return False


class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)

        if user and user.is_active and user.verify_password(password):
            if isinstance(user, RegularUser):
                user.update_last_login()
            return user

        return None



if __name__ == "__main__":
    access = AccessControl()

    mykhailo = RegularUser(
        username="frolov_mykhailo",
        password="student123"
    )

    access.add_user(mykhailo)

    user = access.authenticate_user(
        username="frolov_mykhailo",
        password="student123"
    )

    if user:
        print(" Вхід успішний")
        print(" Користувач:", user.username)
        print(" Останній вхід:", user.last_login)
    else:
        print(" Помилка входу")