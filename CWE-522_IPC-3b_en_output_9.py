
import bcrypt
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

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def register_user(conn, username, password):
    """Register a new user in the database."""
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        print("Username already exists.")
        return False
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Insert the new user
    try:
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                      (username, hashed_password))
        conn.commit()
        print("Registration successful!")
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def main():
    # Create database connection and table
    conn = create_connection()
    create_table(conn)
    
    # Get user input
    print("=== User Registration ===")
    username = input("Enter username: ").strip()
    
    # Use getpass to hide password input
    password = getpass("Enter password: ").strip()
    confirm_password = getpass("Confirm password: ").strip()
    
    # Validate input
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    if password != confirm_password:
        print("Passwords do not match.")
        return
    
    # Register the user
    register_user(conn, username, password)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
