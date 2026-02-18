
import sqlite3
import hashlib
import os
from typing import Tuple, Optional

def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection to the SQLite database."""
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

def hash_password(password: str) -> str:
    """Hash a password using SHA-256 with a salt."""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return salt.hex() + key.hex()

def username_exists(conn: sqlite3.Connection, username: str) -> bool:
    """Check if username already exists in the database."""
    sql = "SELECT 1 FROM users WHERE username = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (username,))
    return cursor.fetchone() is not None

def register_user(
    conn: sqlite3.Connection,
    username: str,
    password: str,
    first_name: str,
    last_name: str,
    email: str
) -> Tuple[bool, str]:
    """Register a new user."""
    if username_exists(conn, username):
        return False, "Username already exists"
    
    password_hash = hash_password(password)
    
    sql = """
    INSERT INTO users(username, password_hash, first_name, last_name, email)
    VALUES(?, ?, ?, ?, ?)
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (username, password_hash, first_name, last_name, email))
        conn.commit()
        return True, "Registration succeeded"
    except sqlite3.Error as e:
        return False, f"Database error: {e}"

def main():
    # Database setup
    database = "users.db"
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn)
        
        # Example registration
        result, message = register_user(
            conn=conn,
            username="johndoe",
            password="securepassword123",
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )
        
        print(message)
        conn.close()
    else:
        print("Error: Cannot create database connection.")

if __name__ == "__main__":
    main()
