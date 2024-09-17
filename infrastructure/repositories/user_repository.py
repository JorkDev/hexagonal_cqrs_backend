from core.entities.user import User
from infrastructure.database.models import UserModel
from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, user: User):
        user_model = UserModel(id=str(user.id), username=user.username, email=user.email)
        self.db.add(user_model)
        self.db.commit()

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        user_model = self.db.query(UserModel).filter_by(id=str(user_id)).first()
        if user_model:
            return User(id=user_model.id, username=user_model.username, email=user_model.email)
        return None
