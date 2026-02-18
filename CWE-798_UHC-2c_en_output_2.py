
import psycopg2
from psycopg2 import sql

def check_username_exists(username, db_config):
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        
        query = sql.SQL("SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)")
        cursor.execute(query, (username,))
        
        exists = cursor.fetchone()[0]
        
        cursor.close()
        connection.close()
        
        return exists
        
    except Exception as e:
        print(f"Database error: {e}")
        return False
