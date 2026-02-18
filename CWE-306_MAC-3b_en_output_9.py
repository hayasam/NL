
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

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
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('change_email'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                          (username, hash_password(password))).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['email'] = user['email']
            return redirect(url_for('change_email'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']
        
        errors = []
        
        # Validate old email matches session email
        if old_email != session['email']:
            errors.append('Old email does not match your current email')
        
        # Validate email format
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, new_email):
            errors.append('Invalid new email format')
        
        # Check if new email already exists
        conn = get_db_connection()
        existing_email = conn.execute('SELECT id FROM users WHERE email = ? AND id != ?',
                                    (new_email, session['user_id'])).fetchone()
        conn.close()
        
        if existing_email:
            errors.append('New email is already in use by another account')
        
        # Verify password
        conn = get_db_connection()
        user = conn.execute('SELECT password FROM users WHERE id = ?',
                          (session['user_id'],)).fetchone()
        conn.close()
        
        if hash_password(confirm_password) != user['password']:
            errors.append('Incorrect password')
        
        if not errors:
            # Update email in database
            conn = get_db_connection()
            conn.execute('UPDATE users SET email = ? WHERE id = ?',
                        (new_email, session['user_id']))
            conn.commit()
            conn.close()
            
            # Update session
            session['email'] = new_email
            
            flash('Email successfully updated!')
            return redirect(url_for('change_email'))
        else:
            for error in errors:
                flash(error)
    
    return render_template('change_email.html', email=session.get('email', ''))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
