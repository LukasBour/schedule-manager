import Hashing
import string
import random
import Logging


# Class defining a User of the program
class User:
    # Default constructor of a User
    def __init__(self, email: str, password: str, alias: str = ""):
        self.email = email
        self.salt = create_salt()
        self.password_hash = Hashing.hash_password(password, self.salt)
        self.alias = alias


# Creates a random 100 character salt for hashing a password
def create_salt() -> str:
    salt_buffer: str = ""
    for i in range(100):
        salt_buffer += random.choice(string.ascii_letters)
    if not check_salt(salt_buffer):
        raise RuntimeError("Something went wrong while creating Salt. Length mismatch.")
    return salt_buffer


# checks whether a squence of characters is a valid salt
# e.g. 100 characters long
def check_salt(salt: str) -> bool:
    if len(salt) != 100:
        return False
    return True
