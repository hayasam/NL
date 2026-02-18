
import bcrypt
import sqlite3
from getpass import getpass

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
        password_hash TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def register_user(conn, username, password):
    """Register a new user."""
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
    if conn is not None:
        create_table(conn)
        
        print("=== User Registration ===")
        username = input("Enter username: ").strip()
        password = getpass("Enter password: ").strip()
        
        if username and password:
            register_user(conn, username, password)
        else:
            print("Username and password cannot be empty.")
        
        conn.close()
    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
