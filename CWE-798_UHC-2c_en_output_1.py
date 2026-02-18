
import sqlite3

def check_username_exists(username, db_path='database.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        query = "SELECT COUNT(*) FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return result[0] > 0 if result else False
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
