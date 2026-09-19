from dataclasses import dataclass


@dataclass
class User:
    """
    Entity User: representasi data user di domain.
    Tidak bergantung pada storage atau UI apa pun.
    """
    id: int
    name: str
    email: str


def validate_user(name: str, email: str) -> dict:
    """
    Validasi input user dan kembalikan dict yang sudah dinormalisasi.
    Fungsi ini murni (pure) - tidak bergantung pada storage/file.
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    if "@" not in email:
        raise ValueError("Invalid email")

    return {
        "name": name.strip(),
        "email": email.strip().lower(),
    }