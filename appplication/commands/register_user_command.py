from infrastructure.repositories.user_repository import UserRepository
from core.entities.user import User

class RegisterUserCommand:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, username: str, email: str):
        existing_user = self.user_repository.find_by_username_or_email(username, email)
        if existing_user:
            raise ValueError("Usuario y/o correo existentes")
        
        user = User(username=username, email=email)

        self.user_repository.save(user)

        return user
