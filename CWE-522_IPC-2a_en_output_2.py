
import sqlite3
import hashlib
import secrets
import string

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

def generate_salt(length=16):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_password(password, salt):
    salted_password = salt + password
    return hashlib.sha256(salted_password.encode()).hexdigest()

def register_user(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, salt, hashed_password)
            VALUES (?, ?, ?)
        ''', (username, salt, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def main():
    create_database()
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username and password:
        register_user(username, password)
    else:
        print("Username and password cannot be empty!")

if __name__ == "__main__":
    main()
