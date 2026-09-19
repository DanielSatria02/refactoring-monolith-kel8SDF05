import pytest

from services.user_service import UserService
from storage.user_storage import UserStorage


class FakeUserStorage(UserStorage):
    """
    Fake storage untuk testing.
    Tidak menyentuh file system sama sekali!
    Inilah keuntungan utama dari Dependency Inversion.
    """

    def __init__(self):
        self.users = []

    def load_users(self):
        return list(self.users)

    def save_users(self, users):
        self.users = list(users)


def test_create_user():
    storage = FakeUserStorage()
    service = UserService(storage)

    user = service.create_user("Alice", "alice@example.com")

    assert user["name"] == "Alice"
    assert user["email"] == "alice@example.com"
    assert user["id"] == 1
    assert len(storage.users) == 1


def test_duplicate_email():
    storage = FakeUserStorage()
    service = UserService(storage)

    service.create_user("Alice", "alice@example.com")

    with pytest.raises(ValueError, match="Email already exists"):
        service.create_user("Budi", "alice@example.com")


def test_list_users():
    storage = FakeUserStorage()
    service = UserService(storage)

    service.create_user("Alice", "alice@example.com")
    service.create_user("Budi", "budi@example.com")

    users = service.list_users()

    assert len(users) == 2
    assert users[0]["name"] == "Alice"
    assert users[1]["name"] == "Budi"