
import hashlib
import sqlite3
import re

def create_connection():
    return sqlite3.connect('users.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(username, password, first_name, last_name, email):
    if not all([username, password, first_name, last_name, email]):
        return "All fields are required."
    
    if not is_valid_email(email):
        return "Invalid email format."
    
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return "Username already exists."
        
        password_hash = hash_password(password)
        
        cursor.execute('''
            INSERT INTO users (username, password_hash, first_name, last_name, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, password_hash, first_name, last_name, email))
        
        conn.commit()
        conn.close()
        return "Registration succeeded."
        
    except sqlite3.Error as e:
        conn.close()
        return f"Database error: {e}"

if __name__ == "__main__":
    create_table()
    
    print("Registration Page")
    print("-----------------")
    
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip().lower()
    
    result = register_user(username, password, first_name, last_name, email)
    print(result)
