
import hashlib
import sqlite3
import re

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL
                );'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(conn, username, password, first_name, last_name, email):
    if not all([username, password, first_name, last_name, email]):
        return "All fields are required."
    
    if not is_valid_email(email):
        return "Invalid email format."
    
    hashed_password = hash_password(password)
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT username FROM users WHERE username = ?", (username,))
        existing_user = cur.fetchone()
        
        if existing_user:
            return "Username already exists."
        
        sql = '''INSERT INTO users(username, password, first_name, last_name, email)
                 VALUES(?,?,?,?,?)'''
        cur.execute(sql, (username, hashed_password, first_name, last_name, email))
        conn.commit()
        return "Registration succeeded."
    except sqlite3.Error as e:
        return f"Database error: {e}"

def main():
    database = "users.db"
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn)
        
        print("=== Registration Page ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip()
        
        result = register_user(conn, username, password, first_name, last_name, email)
        print(result)
        
        conn.close()
    else:
        print("Error: Cannot create database connection.")

if __name__ == '__main__':
    main()
