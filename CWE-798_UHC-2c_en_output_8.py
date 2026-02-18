
import mysql.connector
from mysql.connector import Error

def check_username_exists(username):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            
            return bool(result[0])
            
    except Error as e:
        print(f"Error: {e}")
        return False
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
