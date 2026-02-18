
import hashlib
import os
import sqlite3
import secrets

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
        salt = secrets.token_hex(16)
    
    # Combine password and salt
    salted_password = password + salt
    
    # Create SHA-256 hash
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    
    # Return hash with salt appended
    return f"{password_hash}:{salt}"

def verify_password(stored_hash, password):
    """Verify a password against a stored hash."""
    try:
        stored_password_hash, salt = stored_hash.split(':')
    except ValueError:
        return False
    
    # Hash the provided password with the same salt
    salted_password = password + salt
    provided_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    
    return secrets.compare_digest(provided_hash, stored_password_hash)

def register_user(conn, username, password):
    """Register a new user."""
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        print("Username already exists!")
        return False
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Insert the new user
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                   (username, hashed_password))
    conn.commit()
    
    print("Registration successful!")
    return True

def login_user(conn, username, password):
    """Login an existing user."""
    cursor = conn.cursor()
    
    # Get the stored hash
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    if not result:
        print("Invalid username or password!")
        return False
    
    stored_hash = result[0]
    
    # Verify the password
    if verify_password(stored_hash, password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

def main():
    """Main function to run the registration/login system."""
    # Initialize database
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
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
            print("Invalid choice!")
    
    conn.close()

if __name__ == "__main__":
    main()
