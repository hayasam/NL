
import sqlite3
import hashlib
import secrets
import string

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
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def generate_salt(length=16):
    """Generate a random salt."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_password(password, salt):
    """Hash password with salt using SHA-256."""
    salted_password = salt + password
    return hashlib.sha256(salted_password.encode()).hexdigest()

def insert_user(conn, username, password):
    """Insert a new user with hashed password."""
    salt = generate_salt()
    hashed_pw = hash_password(password, salt)
    
    sql = '''INSERT INTO users(username, salt, hashed_password)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    try:
        cur.execute(sql, (username, salt, hashed_pw))
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
    password = input("Enter password: ").strip()
    
    # Validate input
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    # Create database connection and table
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        insert_user(conn, username, password)
        conn.close()
    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()
