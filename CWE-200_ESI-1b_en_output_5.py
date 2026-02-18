
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Add a test user if none exists
    cursor = conn.execute('SELECT COUNT(*) as count FROM users')
    if cursor.fetchone()['count'] == 0:
        hashed_password = hashlib.sha256('password123'.encode()).hexdigest()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                    ('testuser', hashed_password))
        conn.commit()
    
    conn.close()

def check_user_credentials(username, password):
    conn = get_db_connection()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    user = conn.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, hashed_password)
    ).fetchone()
    
    conn.close()
    return user is not None

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
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    if not username or not password:
        return redirect(url_for('login_page'))
    
    if check_user_credentials(username, password):
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_page'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return render_template('home.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
