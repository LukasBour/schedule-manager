import Hashing
import string
import random


def create_salt() -> str:
    salt_buffer: str = ""
    for i in range(100):
        salt_buffer += random.choice(string.ascii_letters)
    if not check_salt(salt_buffer):
        raise RuntimeError("Something went wrong while creating Salt. Length mismatch.")
    return salt_buffer


def check_salt(salt: str) -> bool:
    if len(salt) != 100:
        return False
    return True


class User:

    username: str
    password_hash: str
    salt: str

    def __init__(self, username: str, password: str):
        self.username = username
        self.salt = create_salt()
        self.password_hash = Hashing.hash_password(password, self.salt)

    def get_username(self) -> str:
        return self.username

    def get_password_hash(self) -> str:
        return self.password_hash
    