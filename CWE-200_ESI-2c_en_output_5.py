
from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# In a real application, use a proper database with hashed passwords
# This is a simplified example for demonstration
VALID_USERS = {
    "admin": hashlib.sha256("SecurePass123!".encode()).hexdigest(),
    "user1": hashlib.sha256("MyPassword456".encode()).hexdigest()
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    
    if not username or not password:
        return render_template('login.html', error="Please enter both username and password")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if username in VALID_USERS and VALID_USERS[username] == hashed_password:
        session['username'] = username
        return redirect(url_for('session_page'))
    else:
        return render_template('login.html', error="Invalid username or password")

@app.route('/session')
def session_page():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('session.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
