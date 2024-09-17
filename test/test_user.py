from core.use_cases.register_user import RegisterUser
from core.use_cases.get_user import GetUser
from uuid import uuid4

def test_register_user():
    repo = FakeUserRepository()
    use_case = RegisterUser(repo)
    user = use_case.execute("john_doe", "john@example.com")
    assert user.username == "john_doe"
    assert user.email == "john@example.com"

def test_get_user():
    repo = FakeUserRepository()
    user_id = uuid4()
    repo.add(User(id=user_id, username="john_doe", email="john@example.com"))
    use_case = GetUser(repo)
    user = use_case.execute(user_id)
    assert user.username == "john_doe"
