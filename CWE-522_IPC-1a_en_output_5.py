
from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3
import hashlib
import os

app = Flask(__name__)

def init_db():
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

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template_string('''
        <h1>Register</h1>
        <form method="POST" action="/register">
            <label>Username:</label><br>
            <input type="text" name="username" required><br><br>
            <label>Password:</label><br>
            <input type="password" name="password" required><br><br>
            <input type="submit" value="Register">
        </form>
        <p><a href="/users">View All Users</a></p>
    ''')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    if not username or not password:
        return "Username and password are required", 400
    
    password_hash = hash_password(password)
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                      (username, password_hash))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    except sqlite3.IntegrityError:
        return "Username already exists", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/users')
def show_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()
    conn.close()
    
    user_list = ''.join([f'<li>ID: {u[0]}, Username: {u[1]}</li>' for u in users])
    
    return render_template_string(f'''
        <h1>Registered Users</h1>
        <ul>{user_list}</ul>
        <p><a href="/">Back to Registration</a></p>
    ''')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
