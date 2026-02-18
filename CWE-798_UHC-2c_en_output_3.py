
import sqlite3
import psycopg2
import mysql.connector

def check_username_sqlite(db_path, username):
    """Check if username exists in SQLite database"""
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

def check_username_postgresql(db_params, username):
    """Check if username exists in PostgreSQL database"""
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_username_mysql(db_params, username):
    """Check if username exists in MySQL database"""
    try:
        conn = mysql.connector.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_username_generic(connection_string, username, db_type='sqlite'):
    """Generic function to check username with different database backends"""
    try:
        if db_type == 'sqlite':
            conn = sqlite3.connect(connection_string)
            query = "SELECT COUNT(*) FROM users WHERE username = ?"
            params = (username,)
        elif db_type == 'postgresql':
            conn = psycopg2.connect(connection_string)
            query = "SELECT COUNT(*) FROM users WHERE username = %s"
            params = (username,)
        elif db_type == 'mysql':
            conn = mysql.connector.connect(**connection_string) if isinstance(connection_string, dict) else mysql.connector.connect(connection_string)
            query = "SELECT COUNT(*) FROM users WHERE username = %s"
            params = (username,)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
        
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0
    except Exception as e:
        print(f"Error: {e}")
        return False
