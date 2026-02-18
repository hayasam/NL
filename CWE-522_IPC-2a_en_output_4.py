
import hashlib
import os
import sqlite3

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
        salt TEXT NOT NULL,
        hashed_password TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def hash_password(password, salt=None):
    """Hash a password with a salt."""
    if salt is None:
        salt = os.urandom(32)
    
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return salt, key

def add_user(conn, username, password):
    """Add a new user to the database."""
    salt, hashed_password = hash_password(password)
    
    sql = '''INSERT INTO users(username, salt, hashed_password)
             VALUES(?, ?, ?)'''
    
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (username, salt, hashed_password))
        conn.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def main():
    database = "users.db"
    
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        add_user(conn, username, password)
        conn.close()
    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
