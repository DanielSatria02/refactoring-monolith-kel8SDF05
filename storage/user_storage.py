from abc import ABC, abstractmethod


class UserStorage(ABC):
    """
    Interface abstrak untuk storage user.
    Domain logic hanya bergantung pada interface ini,
    bukan pada implementasi konkret (JSON, DB, dll).
    """

    @abstractmethod
    def load_users(self) -> list[dict]:
        """Ambil semua user dari storage."""
        pass

    @abstractmethod
    def save_users(self, users: list[dict]) -> None:
        """Simpan semua user ke storage."""
        pass