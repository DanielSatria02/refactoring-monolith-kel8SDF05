from domain.user import validate_user


def test_validate_user():
    user = validate_user(" Alice ", "ALICE@example.com")

    assert user == {
        "name": "Alice",
        "email": "alice@example.com",
    }


def test_invalid_email():
    try:
        validate_user("Alice", "invalid-email")
        assert False, "Expected ValueError"
    except ValueError as error:
        assert str(error) == "Invalid email"


def test_empty_name():
    try:
        validate_user("", "alice@example.com")
        assert False, "Expected ValueError"
    except ValueError as error:
        assert str(error) == "Name cannot be empty"