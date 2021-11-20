class UserInfoException(Exception):
    pass
class UserNotFound(UserInfoException):
    def __init__(self):
        self.status_code = 404
        self.details = 'User not found...'

class UserAlreadyExist(UserInfoException):
    def __init__(self):
        self.status_code = 409
        self.details = 'User already exist...'