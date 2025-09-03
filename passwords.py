# passwords.py
SPECIALS = set("!#$%^&*")

def is_password_strong(password: str) -> bool:
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in SPECIALS for c in password):
        return False
    return True
