
import os
import psycopg2
from psycopg2 import pool

# Database connection pool
db_pool = None

def init_db_pool():
    global db_pool
    if db_pool is None:
        try:
            db_pool = psycopg2.pool.SimpleConnectionPool(
                1, 20,
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                port=os.getenv('DB_PORT', '5432')
            )
        except Exception as e:
            print(f"Database connection failed: {e}")
            raise

def is_moderator(user_id):
    if db_pool is None:
        init_db_pool()
    
    conn = None
    try:
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            query = """
            SELECT EXISTS(
                SELECT 1 FROM users 
                WHERE id = %s AND is_moderator = TRUE
            )
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            return result[0] if result else False
    except Exception as e:
        print(f"Query failed: {e}")
        return False
    finally:
        if conn:
            db_pool.putconn(conn)
