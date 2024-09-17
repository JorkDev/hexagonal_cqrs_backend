from sqlalchemy.orm import Session
from infrastructure.database.models import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_username_or_email(self, username: str, email: str):
        return self.db.query(UserModel).filter(
            (UserModel.username == username) | (UserModel.email == email)
        ).first()

    def save(self, user):
        new_user = UserModel(username=user.username, email=user.email)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
