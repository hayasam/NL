
# login.html
'''
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
'''

# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

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
    
    # Add a test user if not exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
    if cursor.fetchone()[0] == 0:
        hashed_password = hashlib.sha256('password123'.encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                      ('admin', hashed_password))
    
    conn.commit()
    conn.close()

def check_user_credentials(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute('''
        SELECT * FROM users 
        WHERE username = ? AND password = ?
    ''', (username, hashed_password))
    
    user = cursor.fetchone()
    conn.close()
    
    return user is not None

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_user_credentials(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login_page'))
    
    return redirect(url_for('login_page'))

@app.route('/login-page')
def login_page():
    return render_template('login.html')

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
        <h2>Welcome, {}!</h2>
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
