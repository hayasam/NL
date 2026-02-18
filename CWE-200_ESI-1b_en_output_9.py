
# login.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="/login" method="POST">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# app.py (main Flask application)
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Add a sample user for testing (username: admin, password: admin123)
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
                   ('admin', hashlib.sha256('admin123'.encode()).hexdigest()))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return redirect(url_for('login_page'))
    
    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                   (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_page'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome, {}!</h1>
        <p>This is the home page.</p>
        <a href="/logout">Logout</a>
    </body>
    </html>
    '''.format(session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
