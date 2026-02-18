
import sqlite3
import mysql.connector
import psycopg2
import pyodbc

# SQLite version
def check_username_sqlite(db_path, username):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False

# MySQL version
def check_username_mysql(host, user, password, database, username):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False

# PostgreSQL version
def check_username_postgresql(host, user, password, database, username):
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False

# Generic version with parameterized query
def check_username_generic(connection_func, username, query=None):
    try:
        conn = connection_func()
        cursor = conn.cursor()
        
        if query is None:
            query = "SELECT COUNT(*) FROM users WHERE username = %s"
        
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        exists = result[0] > 0
        
        cursor.close()
        conn.close()
        return exists
    except Exception as e:
        print(f"Error: {e}")
        return False
