
import hashlib
import os
import sqlite3
from getpass import getpass

def create_connection():
    """Create a database connection."""
    conn = sqlite3.connect('users.db')
    return conn

def create_table(conn):
    """Create the users table if it doesn't exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()

def hash_password(password, salt=None):
    """Hash a password with a salt."""
    if salt is None:
        salt = os.urandom(32)
    
    # Use PBKDF2 for key derivation
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000  # Number of iterations
    )
    
    # Return salt + key concatenated
    return salt + key

def verify_password(stored_hash, provided_password):
    """Verify a password against a stored hash."""
    # Extract salt from stored hash (first 32 bytes)
    salt = stored_hash[:32]
    stored_key = stored_hash[32:]
    
    # Hash the provided password with the same salt
    provided_key = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    
    # Compare the keys
    return provided_key == stored_key

def register_user(conn):
    """Register a new user."""
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists!")
        return
    
    # Hash the password
    password_hash = hash_password(password)
    
    # Store in database
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    conn.commit()
    print("Registration successful!")

def login_user(conn):
    """Login an existing user."""
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    
    cursor = conn.cursor()
    
    # Get user from database
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    
    if not result:
        print("Invalid username or password!")
        return False
    
    stored_hash = result[0]
    
    # Verify password
    if verify_password(stored_hash, password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

def main():
    """Main function."""
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            register_user(conn)
        elif choice == '2':
            login_user(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice!")
    
    conn.close()

if __name__ == "__main__":
    main()
