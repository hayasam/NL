
import hashlib
import os
import sqlite3
import binascii

def create_connection():
    """Create a database connection."""
    conn = sqlite3.connect('users.db')
    return conn

def create_table(conn):
    """Create users table if it doesn't exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()

def hash_password(password):
    """Hash a password with a randomly generated salt."""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

def verify_password(stored_hash, provided_password):
    """Verify a password against the stored hash."""
    salt = stored_hash[:32]
    stored_key = stored_hash[32:]
    provided_key = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    return stored_key == provided_key

def register_user(conn, username, password):
    """Register a new user."""
    cursor = conn.cursor()
    password_hash = hash_password(password)
    try:
        cursor.execute(
            'INSERT INTO users (username, password_hash) VALUES (?, ?)',
            (username, binascii.hexlify(password_hash).decode())
        )
        conn.commit()
        print("Registration successful!")
        return True
    except sqlite3.IntegrityError:
        print("Username already exists.")
        return False

def login_user(conn, username, password):
    """Login an existing user."""
    cursor = conn.cursor()
    cursor.execute(
        'SELECT password_hash FROM users WHERE username = ?',
        (username,)
    )
    result = cursor.fetchone()
    
    if result is None:
        print("User not found.")
        return False
    
    stored_hash_hex = result[0]
    stored_hash = binascii.unhexlify(stored_hash_hex)
    
    if verify_password(stored_hash, password):
        print("Login successful!")
        return True
    else:
        print("Invalid password.")
        return False

def main():
    """Main program loop."""
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(conn, username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(conn, username, password)
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
