
import hashlib
import sqlite3
import re

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
    """Create users table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    """Basic email validation."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(username, password, first_name, last_name, email):
    """Register a new user."""
    if not all([username, password, first_name, last_name, email]):
        return "All fields are required."
    
    if not is_valid_email(email):
        return "Invalid email format."
    
    conn = create_connection()
    if conn is None:
        return "Database connection failed."
    
    create_table(conn)
    
    try:
        cursor = conn.cursor()
        
        # Check if username exists
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return "Username already exists."
        
        # Hash password
        hashed_password = hash_password(password)
        
        # Insert new user
        cursor.execute("""
            INSERT INTO users (username, password, first_name, last_name, email)
            VALUES (?, ?, ?, ?, ?)
        """, (username, hashed_password, first_name, last_name, email))
        
        conn.commit()
        conn.close()
        return "Registration succeeded."
        
    except sqlite3.Error as e:
        conn.close()
        return f"Database error: {e}"

def main():
    """Example usage."""
    # Get user input
    print("Registration Page")
    print("-" * 30)
    
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    
    # Register user
    result = register_user(username, password, first_name, last_name, email)
    print(result)

if __name__ == "__main__":
    main()
