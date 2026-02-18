
from flask import Flask, request, redirect, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return "Missing username or password", 400
    
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone()
    conn.close()
    
    if user is None:
        return "User not found", 401
    
    hashed_password = hash_password(password)
    
    if user['password'] == hashed_password:
        session['user_id'] = user['id']
        session['username'] = user['username']
        return redirect('/home')
    
    return "Incorrect password", 401

if __name__ == '__main__':
    app.run(debug=True)
