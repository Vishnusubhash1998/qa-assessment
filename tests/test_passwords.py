import pytest
from passwords import is_password_strong

@pytest.mark.parametrize(
    "password",
    [
        "Abcd1234!",
        "XyZ9#more",
        "PASSword5^",
        "GoodPwd8*$",
    ],
    ids=["bang", "hash", "caret", "multi-special"],
)
def test_is_password_strong_valid(password):
    assert is_password_strong(password) is True

@pytest.mark.parametrize(
    "password,reason",
    [
        ("Abc1!x", "too short"),
        ("abcdefg1!", "no uppercase"),
        ("ABCDEFG!", "no digit"),
        ("Abcdefg1", "no allowed special"),
        ("", "empty"),
        (None, "not a string"),
        (12345678, "not a string"),
        ("OnlyUpperCASE1", "missing !#$%^&*"),
        ("lower1!", "no uppercase & short"),
    ],
    ids=[
        "len<8", "no-upper", "no-digit", "no-special",
        "empty", "none", "int", "no-allowed-special", "two-problems"
    ]
)
def test_is_password_strong_invalid(password, reason):
    assert is_password_strong(password) is False, reason
