
from flask import Flask, request, render_template_string, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)

# HTML template for registration form
REGISTER_TEMPLATE = '''
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
    """Initialize the database and create users table if it doesn't exist."""
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

@app.route('/', methods=['GET', 'POST'])
def register():
    message = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            message = "Username and password are required!"
        else:
            password_hash = generate_password_hash(password)
            
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                    (username, password_hash)
                )
                conn.commit()
                conn.close()
                message = "Registration successful!"
            except sqlite3.IntegrityError:
                message = "Username already exists!"
            except Exception as e:
                message = f"An error occurred: {str(e)}"
    
    return render_template_string(REGISTER_TEMPLATE, message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
