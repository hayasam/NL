
import os
import hashlib
import binascii

def hash_password(password):
    """Hash a password with a randomly generated salt."""
    salt = os.urandom(16)
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    salt = binascii.hexlify(salt)
    return salt.decode('ascii') + ':' + pwdhash.decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user."""
    salt_hex, pwdhash_hex = stored_password.split(':')
    salt = binascii.unhexlify(salt_hex)
    stored_hash = binascii.unhexlify(pwdhash_hex)
    pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash == stored_hash

def register_user(db_connection, username, password):
    """Register a new user with hashed password."""
    hashed_password = hash_password(password)
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    db_connection.commit()
    cursor.close()

def authenticate_user(db_connection, username, password):
    """Authenticate a user by username and password."""
    cursor = db_connection.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    cursor.close()
    
    if result:
        stored_password = result[0]
        return verify_password(stored_password, password)
    return False
