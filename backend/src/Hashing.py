from hashlib import sha256


def hash_password(password: str, salt: str) -> str:
    password_salt = password + ':' + salt
    return sha256(password_salt.encode('utf-8')).hexdigest()
