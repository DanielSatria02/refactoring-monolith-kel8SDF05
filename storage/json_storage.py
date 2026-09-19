import json
from pathlib import Path

from storage.user_storage import UserStorage


class JsonUserStorage(UserStorage):
    """
    Implementasi UserStorage menggunakan file JSON.
    Ini adalah adapter yang menghubungkan domain ke file system.
    """

    def __init__(self, file_path: str = "users.json"):
        self.file_path = Path(file_path)

    def load_users(self) -> list[dict]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def save_users(self, users: list[dict]) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(users, file, indent=2)