from domain.user import validate_user
from storage.user_storage import UserStorage


class UserService:
    """
    Service yang menangani business logic user.
    Bergantung pada abstraksi UserStorage, bukan implementasi konkret.
    """

    def __init__(self, storage: UserStorage):
        self.storage = storage

    def create_user(self, name: str, email: str) -> dict:
        users = self.storage.load_users()
        user = validate_user(name, email)

        if any(existing["email"] == user["email"] for existing in users):
            raise ValueError("Email already exists")

        user["id"] = len(users) + 1
        users.append(user)
        self.storage.save_users(users)

        return user

    def list_users(self) -> list[dict]:
        return self.storage.load_users()