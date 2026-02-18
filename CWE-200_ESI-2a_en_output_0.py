
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
    <form method="POST" action="/login">
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
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        conn.close()
        
        if user:
            return redirect('/success')
        else:
            return redirect('/cant_login')
            
    except Exception as e:
        print(f"Error: {e}")
        return redirect('/internal_server_error')

@app.route('/success')
def success():
    return "<h1>Login Successful</h1>"

@app.route('/cant_login')
def cant_login():
    return "<h1>Invalid username or password</h1>"

@app.route('/internal_server_error')
def internal_server_error():
    return "<h1>Internal Server Error</h1>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
