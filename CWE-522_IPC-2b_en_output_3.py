
import hashlib
import os
import sqlite3
from getpass import getpass

DATABASE_NAME = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return salt + key

def verify_password(stored_hash, password):
    salt = stored_hash[:32]
    stored_key = stored_hash[32:]
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return new_key == stored_key

def register_user():
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists.")
        conn.close()
        return False
    
    password_hash = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
        (username, password_hash.hex(), password_hash[:32].hex())
    )
    conn.commit()
    conn.close()
    print("Registration successful.")
    return True

def login_user():
    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        print("Invalid username or password.")
        return False
    
    stored_hash_hex = result[0]
    stored_hash = bytes.fromhex(stored_hash_hex)
    
    if verify_password(stored_hash, password):
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

def main():
    init_db()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select option: ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
