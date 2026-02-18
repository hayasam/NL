
import os
import psycopg2
from psycopg2 import sql

def is_moderator(user_id):
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT', '5432')
        )
        
        cursor = conn.cursor()
        query = sql.SQL("SELECT is_moderator FROM users WHERE id = %s")
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return result[0] if result else False
        
    except Exception as e:
        print(f"Database error: {e}")
        return False
