
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
        salt TEXT NOT NULL,
        password_hash TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def hash_password(password, salt=None):
    """Hash a password with a salt."""
    if salt is None:
        salt = secrets.token_hex(16)
    
    salted_password = salt + password
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    
    return salt, password_hash

def insert_user(conn, username, password):
    """Insert a new user into the users table."""
    salt, password_hash = hash_password(password)
    
    sql = '''INSERT INTO users(username, salt, password_hash)
             VALUES(?,?,?)'''
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (username, salt, password_hash))
        conn.commit()
        print(f"User '{username}' added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Username '{username}' already exists.")
    except sqlite3.Error as e:
        print(e)
    
    return None

def main():
    database = "users.db"
    
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        if username and password:
            insert_user(conn, username, password)
        else:
            print("Username and password cannot be empty.")
        
        conn.close()
    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
