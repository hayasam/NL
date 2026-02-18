
import hashlib
import secrets
import sqlite3
from typing import Optional, Tuple

def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn: sqlite3.Connection) -> None:
    """Create users table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def generate_salt() -> str:
    """Generate a random salt."""
    return secrets.token_hex(16)

def hash_password(password: str, salt: str) -> str:
    """Hash password with salt using SHA-256."""
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode()).hexdigest()

def register_user(conn: sqlite3.Connection, username: str, password: str) -> bool:
    """Register a new user."""
    if not username or not password:
        print("Username and password cannot be empty.")
        return False
    
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    stored_value = f"{password_hash}:{salt}"
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
            (username, stored_value, salt)
        )
        conn.commit()
        print(f"User '{username}' registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print(f"Username '{username}' already exists.")
        return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def verify_password(stored_hash: str, salt: str, provided_password: str) -> bool:
    """Verify a password against stored hash and salt."""
    provided_hash = hash_password(provided_password, salt)
    return secrets.compare_digest(provided_hash, stored_hash)

def login_user(conn: sqlite3.Connection, username: str, password: str) -> bool:
    """Authenticate a user."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash, salt FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    
    if result is None:
        print("Invalid username or password.")
        return False
    
    stored_value, salt = result
    stored_hash = stored_value.split(':')[0]
    
    if verify_password(stored_hash, salt, password):
        print(f"User '{username}' logged in successfully.")
        return True
    else:
        print("Invalid username or password.")
        return False

def main() -> None:
    """Main function to run the registration system."""
    database = "users.db"
    
    conn = create_connection(database)
    if conn is None:
        print("Error! Cannot create database connection.")
        return
    
    create_table(conn)
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            register_user(conn, username, password)
        
        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            login_user(conn, username, password)
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    conn.close()

if __name__ == "__main__":
    main()
