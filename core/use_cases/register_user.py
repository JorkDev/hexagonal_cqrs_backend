from core.entities.user import User
from typing import Optional
from uuid import uuid4

class RegisterUser:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, username: str, email: str) -> User:
        new_user = User(id=uuid4(), username=username, email=email)
        self.user_repo.add(new_user)
        return new_user
