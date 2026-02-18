
import sqlite3
import hashlib
import secrets

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            salt TEXT NOT NULL,
            hashed_password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    
    salted_password = salt + password
    hashed = hashlib.sha256(salted_password.encode()).hexdigest()
    return salt, hashed

def insert_user(username, password):
    salt, hashed_password = hash_password(password)
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, salt, hashed_password) VALUES (?, ?, ?)',
            (username, salt, hashed_password)
        )
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def main():
    create_database()
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username and password:
        insert_user(username, password)
    else:
        print("Username and password cannot be empty!")

if __name__ == "__main__":
    main()
