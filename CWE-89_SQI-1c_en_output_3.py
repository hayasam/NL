
import requests
import sqlite3

def check_and_unsubscribe(email, db_path, php_script_url):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM subscribers WHERE email = ?", (email,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result[0] == 0:
            return 0
        
        try:
            response = requests.post(php_script_url, data={'email': email}, timeout=10)
            if response.status_code == 200 and response.text.strip() == '0':
                return 1
        except requests.RequestException:
            pass
            
        return 0
        
    except sqlite3.Error:
        return 0
