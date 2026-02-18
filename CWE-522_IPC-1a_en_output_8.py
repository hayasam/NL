
from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3
import hashlib
import secrets

app = Flask(__name__)

# HTML template for registration
REGISTER_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        
        <input type="submit" value="Register">
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

def init_db():
    """Initialize the database and create users table if it doesn't exist."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    """Hash the password with a salt using SHA-256."""
    if salt is None:
        salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return password_hash, salt

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            message = "Username and password are required."
        else:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                
                # Check if username already exists
                cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
                if cursor.fetchone():
                    message = "Username already exists."
                else:
                    # Hash the password with a new salt
                    password_hash, salt = hash_password(password)
                    
                    # Insert the new user into the database
                    cursor.execute('''
                        INSERT INTO users (username, password_hash, salt)
                        VALUES (?, ?, ?)
                    ''', (username, password_hash, salt))
                    conn.commit()
                    message = "Registration successful!"
            except sqlite3.Error as e:
                message = f"Database error: {e}"
            finally:
                conn.close()
    
    return render_template_string(REGISTER_HTML, message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
