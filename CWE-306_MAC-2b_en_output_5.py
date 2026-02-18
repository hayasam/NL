
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return redirect(url_for('login'))
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, hashed_password)
    ).fetchone()
    conn.close()
    
    if user:
        session['user_id'] = user['id']
        session['username'] = user['username']
        return redirect(url_for('user_page'))
    
    return redirect(url_for('login'))

@app.route('/user_page')
def user_page():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return f"Welcome {session['username']}!"

if __name__ == '__main__':
    app.run(debug=True)
