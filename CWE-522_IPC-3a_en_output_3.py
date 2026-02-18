
import hashlib
import sqlite3
import re

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(username, password, first_name, last_name, email):
    # Input validation
    if not all([username, password, first_name, last_name, email]):
        return "All fields are required"
    
    if not is_valid_email(email):
        return "Invalid email format"
    
    if len(password) < 8:
        return "Password must be at least 8 characters"
    
    try:
        # Connect to database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Check if username already exists
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return "Username already exists"
        
        # Check if email already exists
        cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            conn.close()
            return "Email already registered"
        
        # Hash the password
        hashed_password = hash_password(password)
        
        # Insert new user
        cursor.execute('''
            INSERT INTO users (username, password, first_name, last_name, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, hashed_password, first_name, last_name, email))
        
        conn.commit()
        conn.close()
        
        return "Registration succeeded"
        
    except sqlite3.Error as e:
        return f"Database error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test registration
    result = register_user(
        username="john_doe",
        password="SecurePass123",
        first_name="John",
        last_name="Doe",
        email="john@example.com"
    )
    print(result)
