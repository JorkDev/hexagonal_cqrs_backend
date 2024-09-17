from core.entities.user import User
from typing import Optional
from uuid import UUID

class GetUser:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id: UUID) -> Optional[User]:
        return self.user_repo.get_by_id(user_id)
