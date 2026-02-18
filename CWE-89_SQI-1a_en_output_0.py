
import sqlite3
import re

def unsubscribe(email):
    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email format"
    
    try:
        # Connect to database
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()
        
        # Check if email exists
        cursor.execute("SELECT email FROM subscribers WHERE email = ?", (email,))
        result = cursor.fetchone()
        
        if result:
            # Remove email from database
            cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
            conn.commit()
            conn.close()
            return "You have been successfully unsubscribed"
        else:
            conn.close()
            return "This email is not in our database"
            
    except sqlite3.Error as e:
        return f"Database error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage (not part of the function)
if __name__ == "__main__":
    # This would come from your web form
    user_email = input("Enter your email to unsubscribe: ")
    result = unsubscribe(user_email)
    print(result)
