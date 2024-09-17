from core.use_cases.register_user import RegisterUser

class RegisterUserCommand:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def handle(self, username: str, email: str):
        use_case = RegisterUser(self.user_repo)
        return use_case.execute(username, email)
