
import bcrypt
import sqlite3
import getpass

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
        c = conn.cursor()
        c.execute(create_table_sql)
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
    cur = conn.cursor()
    try:
        cur.execute(sql, (username, password_hash))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def main():
    database = "users.db"
    
    # Get user input
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    # Create database connection and table
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        
        # Hash password
        hashed_password = hash_password(password)
        
        # Insert user into database
        insert_user(conn, username, hashed_password)
        
        conn.close()
    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
