
import bcrypt
import sqlite3
from getpass import getpass

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
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
        password_hash TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def register_user(conn, username, password):
    """Register a new user with hashed password."""
    hashed_password = hash_password(password)
    sql = '''INSERT INTO users(username, password_hash) VALUES(?,?)'''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (username, hashed_password))
        conn.commit()
        print("Registration successful!")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print("Username already exists.")
        return None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def main():
    database = "users.db"
    
    conn = create_connection(database)
    if conn is None:
        print("Error! Cannot create database connection.")
        return
    
    create_table(conn)
    
    print("=== User Registration ===")
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    register_user(conn, username, password)
    
    conn.close()

if __name__ == '__main__':
    main()
