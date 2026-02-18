
import bcrypt
import sqlite3
import getpass

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
    """Create a users table if it doesn't exist."""
    try:
        sql_create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_users_table)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def insert_user(conn, username, password_hash):
    """Insert a new user into the users table."""
    sql = '''INSERT INTO users(username, password_hash) VALUES(?,?)'''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (username, password_hash))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def main():
    database = "users.db"
    
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password: ").strip()
        
        if username and password:
            password_hash = hash_password(password)
            insert_user(conn, username, password_hash)
        else:
            print("Username and password cannot be empty.")
        
        conn.close()
    else:
        print("Error: Cannot create database connection.")

if __name__ == '__main__':
    main()
