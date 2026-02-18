
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
    salt = binascii.unhexlify(salt_hex.encode('ascii'))
    stored_hash = binascii.unhexlify(pwdhash_hex.encode('ascii'))
    pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash == stored_hash

def register_user(username, password, database):
    """Register a new user with hashed password."""
    if username in database:
        return False
    hashed_password = hash_password(password)
    database[username] = hashed_password
    return True

def login_user(username, password, database):
    """Login a user by verifying password."""
    if username not in database:
        return False
    return verify_password(database[username], password)

# Example usage
if __name__ == "__main__":
    # Simulating a database as a dictionary
    user_database = {}
    
    # Registration
    register_user("alice", "securepassword123", user_database)
    register_user("bob", "mypassword", user_database)
    
    # Login attempts
    print(login_user("alice", "securepassword123", user_database))  # True
    print(login_user("alice", "wrongpassword", user_database))      # False
    print(login_user("bob", "mypassword", user_database))           # True
    print(login_user("charlie", "password", user_database))         # False
