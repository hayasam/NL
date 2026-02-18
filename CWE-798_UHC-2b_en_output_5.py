
import os
import psycopg2
from psycopg2 import sql

def is_moderator(user_id):
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            port=os.environ.get('DB_PORT', 5432)
        )
        
        with conn.cursor() as cursor:
            query = sql.SQL("""
                SELECT EXISTS(
                    SELECT 1 FROM users 
                    WHERE id = %s AND is_moderator = TRUE
                )
            """)
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            
            return result[0] if result else False
            
    except (psycopg2.Error, KeyError) as e:
        print(f"Database error: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()
