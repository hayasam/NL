
import sqlite3
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def unsubscribe(email):
    if not validate_email(email):
        return "Invalid email format"
    
    try:
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT email FROM subscribers WHERE email = ?", (email,))
        result = cursor.fetchone()
        
        if result:
            cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
            conn.commit()
            conn.close()
            return "You have been successfully unsubscribed"
        else:
            conn.close()
            return "This email address is not in our database"
            
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage (not part of the function):
if __name__ == "__main__":
    user_email = input("Enter your email address to unsubscribe: ")
    result = unsubscribe(user_email)
    print(result)
