from infrastructure.repositories.user_repository import UserRepository
from uuid import UUID

class GetUserQuery:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, user_id: UUID):
        user = self.user_repository.find_by_id(user_id)
        return user
