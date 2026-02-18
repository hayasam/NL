
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
            port=os.getenv('DB_PORT', 5432)
        )
        
        with conn.cursor() as cursor:
            query = sql.SQL("""
                SELECT EXISTS(
                    SELECT 1 FROM users 
                    WHERE id = %s AND is_moderator = TRUE
                )
            """)
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()[0]
            
        conn.close()
        return bool(result)
        
    except Exception as e:
        print(f"Database error: {e}")
        return False
