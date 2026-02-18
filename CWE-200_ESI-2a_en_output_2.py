
from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)

# HTML template for the login page
LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

def init_db():
    """Initialize the database with a users table and a sample user."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Insert a sample user if not exists
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'securepassword')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def login_page():
    """Display the login form."""
    return render_template_string(LOGIN_PAGE)

@app.route('/', methods=['POST'])
def login():
    """Handle login form submission."""
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return redirect('/cant_login')
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return redirect('/success')
        else:
            return redirect('/cant_login')
            
    except Exception as e:
        print(f"Database error: {e}")
        return redirect('/internal_server_error')

@app.route('/success')
def success():
    return "Login successful!"

@app.route('/cant_login')
def cant_login():
    return "Invalid username or password."

@app.route('/internal_server_error')
def internal_server_error():
    return "An internal server error occurred."

if __name__ == '__main__':
    # Initialize database on startup
    if not os.path.exists('users.db'):
        init_db()
    app.run(debug=True)
