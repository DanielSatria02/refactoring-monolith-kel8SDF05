import tempfile
from pathlib import Path

from storage.json_storage import JsonUserStorage


def test_save_and_load_users():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "users.json"
        storage = JsonUserStorage(str(file_path))

        users = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]
        storage.save_users(users)

        loaded = storage.load_users()
        assert loaded == users


def test_load_nonexistent_file_returns_empty():
    storage = JsonUserStorage("nonexistent_file.json")
    assert storage.load_users() == []