from core.use_cases.get_user import GetUser

class GetUserQuery:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def handle(self, user_id):
        use_case = GetUser(self.user_repo)
        return use_case.execute(user_id)
