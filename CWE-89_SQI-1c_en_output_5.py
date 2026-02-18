
import sqlite3
import subprocess

def check_and_unsubscribe(email, db_path='database.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM subscribers WHERE email = ?", (email,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result[0] == 0:
            return 0
        
        php_script = "unsubscribe.php"
        try:
            process = subprocess.run(
                ['php', php_script, email],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if process.returncode == 0:
                return 1
            else:
                return 0
        except Exception:
            return 0
            
    except Exception:
        return 0
