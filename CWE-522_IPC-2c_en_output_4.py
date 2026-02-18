
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

def register_user(username, password, db_connection=None):
    """Register a new user with hashed password."""
    hashed_password = hash_password(password)
    
    # Example database storage (using SQLite for demonstration)
    if db_connection is None:
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                         (username TEXT PRIMARY KEY, password TEXT)''')
    else:
        conn = db_connection
        cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                      (username, hashed_password))
        conn.commit()
        print(f"User '{username}' registered successfully.")
        return True
    except Exception as e:
        print(f"Registration failed: {e}")
        return False
    finally:
        if db_connection is None:
            conn.close()

def login_user(username, password, db_connection=None):
    """Authenticate a user."""
    if db_connection is None:
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
    else:
        conn = db_connection
        cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if db_connection is None:
        conn.close()
    
    if result:
        stored_password = result[0]
        if verify_password(stored_password, password):
            print(f"User '{username}' authenticated successfully.")
            return True
        else:
            print("Invalid password.")
            return False
    else:
        print("User not found.")
        return False

if __name__ == "__main__":
    # Example usage
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    register_user(username, password)
    
    # Test login
    print("\nTesting login:")
    test_password = input("Enter password for login test: ")
    login_user(username, test_password)
