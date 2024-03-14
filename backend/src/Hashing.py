from hashlib import sha256


# Hashes a password with salt
def hash_password(password: str, salt: str) -> str:
    password_salt = password + ':' + salt
    return sha256(password_salt.encode('utf-8')).hexdigest()
