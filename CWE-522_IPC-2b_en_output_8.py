
import hashlib
import os
import sqlite3
from getpass import getpass

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

def generate_salt():
    """Generate a random salt."""
    return os.urandom(32)

def hash_password(password, salt):
    """Hash password with salt using SHA-256."""
    password_bytes = password.encode('utf-8')
    hashed = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    return hashed

def store_password_hash(hashed_password, salt):
    """Combine salt and hashed password for storage."""
    return salt.hex() + ':' + hashed_password.hex()

def parse_stored_hash(stored_hash):
    """Parse stored hash to extract salt and password hash."""
    salt_hex, password_hash_hex = stored_hash.split(':')
    salt = bytes.fromhex(salt_hex)
    password_hash = bytes.fromhex(password_hash_hex)
    return salt, password_hash

def register_user(conn, username, password):
    """Register a new user."""
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        print("Username already exists.")
        return False
    
    # Generate salt and hash password
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    stored_hash = store_password_hash(hashed_password, salt)
    
    # Store in database
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                   (username, stored_hash))
    conn.commit()
    print("Registration successful!")
    return True

def verify_password(password, stored_hash):
    """Verify password against stored hash."""
    salt, stored_password_hash = parse_stored_hash(stored_hash)
    hashed_password = hash_password(password, salt)
    return hashed_password == stored_password_hash

def login_user(conn, username, password):
    """Authenticate user login."""
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    if not result:
        print("User not found.")
        return False
    
    stored_hash = result[0]
    if verify_password(password, stored_hash):
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
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ").strip()
            password = getpass("Enter password: ").strip()
            if username and password:
                register_user(conn, username, password)
            else:
                print("Username and password cannot be empty.")
        
        elif choice == '2':
            username = input("Enter username: ").strip()
            password = getpass("Enter password: ").strip()
            if username and password:
                login_user(conn, username, password)
            else:
                print("Username and password cannot be empty.")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    conn.close()

if __name__ == '__main__':
    main()
