
import sqlite3
import hashlib
import secrets
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# HTML template for registration form
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
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

@app.route('/', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            message = "Username and password are required."
        else:
            try:
                password_hash, salt = hash_password(password)
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                    (username, password_hash, salt)
                )
                conn.commit()
                conn.close()
                return redirect(url_for('success'))
            except sqlite3.IntegrityError:
                message = "Username already exists."
            except Exception as e:
                message = f"An error occurred: {e}"
    
    return render_template_string(HTML_TEMPLATE, message=message)

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
