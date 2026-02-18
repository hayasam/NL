
import sqlite3
import hashlib
import secrets

def create_connection(db_file):
    """Create a database connection."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
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

def hash_password(password, salt=None):
    """Hash password with SHA-256 and salt."""
    if salt is None:
        salt = secrets.token_hex(16)
    salted_password = salt + password
    hashed = hashlib.sha256(salted_password.encode()).hexdigest()
    return f"{salt}${hashed}"

def check_username_exists(conn, username):
    """Check if username already exists in database."""
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    return cursor.fetchone() is not None

def register_user(conn, username, password, first_name, last_name, email):
    """Register a new user."""
    if check_username_exists(conn, username):
        return "Username already exists"
    
    hashed_password = hash_password(password)
    
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, password, first_name, last_name, email)
            VALUES (?, ?, ?, ?, ?)
        """, (username, hashed_password, first_name, last_name, email))
        conn.commit()
        return "Registration succeeded"
    except sqlite3.Error as e:
        return f"Registration failed: {e}"

def main():
    # Database file
    database = "users.db"
    
    # Create database connection
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        
        # Example registration
        result = register_user(
            conn=conn,
            username="testuser",
            password="securepassword123",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        print(result)
        
        conn.close()
    else:
        print("Error: Cannot create database connection.")

if __name__ == '__main__':
    main()
