from services.user_service import UserService
from storage.json_storage import JsonUserStorage


def main():
    # Composition Root: di sini kita rakit semua dependency
    storage = JsonUserStorage("users.json")
    service = UserService(storage)

    name = input("Name: ")
    email = input("Email: ")

    try:
        user = service.create_user(name, email)
        print(f"User created: {user}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()