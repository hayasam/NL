
import bcrypt
import sqlite3

def create_user(username, password):
    # Hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Store in database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL
        )
    ''')
    
    # Insert user
    try:
        cursor.execute(
            'INSERT INTO users (username, password_hash) VALUES (?, ?)',
            (username, hashed_password)
        )
        conn.commit()
        print("User created successfully")
    except sqlite3.IntegrityError:
        print("Username already exists")
    finally:
        conn.close()

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_user(username, password)
