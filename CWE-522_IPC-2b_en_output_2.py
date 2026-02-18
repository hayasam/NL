
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
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

def verify_password(stored_hash, password):
    """Verify a password against a stored hash."""
    salt = stored_hash[:32]
    stored_key = stored_hash[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return new_key == stored_key

def register_user(conn):
    """Register a new user."""
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists.")
        return
    
    password_hash = hash_password(password)
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    print("Registration successful.")

def login_user(conn):
    """Login an existing user."""
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result and verify_password(result[0], password):
        print("Login successful.")
    else:
        print("Invalid username or password.")

def main():
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            register_user(conn)
        elif choice == '2':
            login_user(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
    
    conn.close()

if __name__ == "__main__":
    main()
