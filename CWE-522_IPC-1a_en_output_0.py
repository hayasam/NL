
from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3
import hashlib
import os

app = Flask(__name__)

# HTML template for the registration form
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
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
    """Initialize the database and create the users table if it doesn't exist."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash the password using SHA-256 with a salt."""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

@app.route('/', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            message = "Username and password are required."
        else:
            password_hash = hash_password(password)
            
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                             (username, password_hash))
                conn.commit()
                conn.close()
                message = "Registration successful!"
            except sqlite3.IntegrityError:
                message = "Username already exists."
            except Exception as e:
                message = f"An error occurred: {e}"
    
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
