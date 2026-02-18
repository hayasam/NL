
from flask import Flask, render_template, request, redirect, url_for, session
import hashlib

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure random key

# In a real application, use a database with properly hashed passwords
# This is a simplified example for demonstration
VALID_USERS = {
    'admin': hashlib.sha256('password123'.encode()).hexdigest(),
    'user': hashlib.sha256('mypassword'.encode()).hexdigest()
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return render_template('login.html', error='Please enter both username and password')
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if username in VALID_USERS and VALID_USERS[username] == hashed_password:
        session['username'] = username
        return redirect(url_for('session_page'))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/session')
def session_page():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return f"Welcome, {session['username']}! You are now logged in."

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)
