
import sqlite3
import hashlib
import secrets

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
                    password_hash TEXT NOT NULL
                )'''
        cur = conn.cursor()
        cur.execute(sql)
    except sqlite3.Error as e:
        print(e)

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    salted_password = salt + password
    hash_object = hashlib.sha256(salted_password.encode())
    password_hash = hash_object.hexdigest()
    return f"{salt}${password_hash}"

def insert_user(conn, username, password):
    password_hash = hash_password(password)
    sql = '''INSERT INTO users(username, password_hash)
             VALUES(?,?)'''
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
