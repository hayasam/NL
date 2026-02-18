
import sqlite3
import subprocess
import sys

def check_and_unsubscribe(email, db_path='database.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
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
                output = process.stdout.strip()
                if output == "0":
                    return 1
        except Exception:
            pass
            
        return 0
        
    except sqlite3.Error:
        return 0
    except Exception:
        return 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        email = sys.argv[1]
        result = check_and_unsubscribe(email)
        print(result)
    else:
        print(0)
