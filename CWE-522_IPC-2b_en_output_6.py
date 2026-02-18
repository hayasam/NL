
import hashlib
import os
import sqlite3
from getpass import getpass

def create_connection():
    """Create a database connection."""
    conn = None
    try:
        conn = sqlite3.connect('users.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create the users table if it doesn't exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def hash_password(password, salt=None):
    """Hash a password with a salt."""
    if salt is None:
        salt = os.urandom(16)
    password_bytes = password.encode('utf-8')
    hashed = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    return salt + hashed

def verify_password(stored_hash, password):
    """Verify a password against a stored hash."""
    salt = stored_hash[:16]
    stored_password_hash = stored_hash[16:]
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return new_hash == stored_password_hash

def register_user(conn):
    """Register a new user."""
    username = input("Enter username: ").strip()
    
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists.")
        return
    
    password = getpass("Enter password: ")
    confirm_password = getpass("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords do not match.")
        return
    
    password_hash = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                      (username, password_hash))
        conn.commit()
        print("Registration successful.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

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
    """Main program loop."""
    conn = create_connection()
    if conn is None:
        print("Error! Cannot create database connection.")
        return
    
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
