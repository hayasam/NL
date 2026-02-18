
from flask import Flask, render_template, request, redirect, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL)''')
    
    # Add a test user if none exists
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        hashed_password = hashlib.sha256('test123'.encode()).hexdigest()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  ('testuser', hashed_password))
    
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, hashed_password))
    user = c.fetchone()
    
    conn.close()
    return user is not None

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if verify_user(username, password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            return redirect('/login')
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 400px; margin: 50px auto; padding: 20px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; }
            input { width: 100%; padding: 8px; box-sizing: border-box; }
            button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
            .error { color: red; margin-top: 10px; }
        </style>
    </head>
    <body>
        <h2>Login</h2>
        <form method="POST">
            <div class="form-group">
                <label>Username:</label>
                <input type="text" name="username" required>
            </div>
            <div class="form-group">
                <label>Password:</label>
                <input type="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }}
            .welcome {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
            .logout {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="welcome">
            <h2>Welcome, {session['username']}!</h2>
            <p>You have successfully logged in.</p>
        </div>
        <div class="logout">
            <a href="/logout">Logout</a>
        </div>
    </body>
    </html>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
