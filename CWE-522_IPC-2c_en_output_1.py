
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

# Example usage for registration
def register_user(username, password):
    # In a real application, this would connect to a database
    hashed_password = hash_password(password)
    # Store username and hashed_password in database
    print(f"User '{username}' registered successfully.")
    return hashed_password

# Example usage for login verification
def login_user(username, stored_hashed_password, provided_password):
    if verify_password(stored_hashed_password, provided_password):
        print(f"User '{username}' logged in successfully.")
        return True
    else:
        print("Invalid password.")
        return False

# Simulated database (in reality, use a proper database)
database = {}

def main():
    # Registration example
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed_pw = register_user(username, password)
    database[username] = hashed_pw
    
    # Login example
    print("\n--- Login ---")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    
    if login_username in database:
        login_user(login_username, database[login_username], login_password)
    else:
        print("User not found.")

if __name__ == "__main__":
    main()
