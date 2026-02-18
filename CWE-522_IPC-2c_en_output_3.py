
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
    stored_password = database[username]
    return verify_password(stored_password, password)

# Example usage
if __name__ == "__main__":
    # Simulating a database as a dictionary
    user_database = {}
    
    # Registration
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if register_user(username, password, user_database):
        print("Registration successful!")
    else:
        print("Username already exists.")
    
    # Login
    print("\nLogin test:")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    
    if login_user(login_username, login_password, user_database):
        print("Login successful!")
    else:
        print("Invalid credentials.")
