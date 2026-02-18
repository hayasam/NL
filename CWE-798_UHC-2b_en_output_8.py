
import os
import psycopg2
from psycopg2 import pool

# Database connection pool (optional - adjust based on your needs)
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1, 10,
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT', 5432)
    )
except Exception:
    connection_pool = None

def is_moderator(user_id):
    if not connection_pool:
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                port=os.getenv('DB_PORT', 5432)
            )
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False
    else:
        conn = connection_pool.getconn()
    
    try:
        with conn.cursor() as cursor:
            query = """
                SELECT EXISTS(
                    SELECT 1 FROM users 
                    WHERE id = %s AND is_moderator = TRUE
                )
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()[0]
            return bool(result)
    except Exception as e:
        print(f"Query execution failed: {e}")
        return False
    finally:
        if connection_pool:
            connection_pool.putconn(conn)
        else:
            conn.close()
