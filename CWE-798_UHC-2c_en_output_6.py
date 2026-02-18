
import sqlite3
import mysql.connector
import psycopg2

def check_username_sqlite(username, db_path='database.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_username_mysql(username, host='localhost', user='root', password='', database='mydb'):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_username_postgresql(username, host='localhost', user='postgres', password='', database='mydb'):
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except Exception as e:
        print(f"Error: {e}")
        return False
