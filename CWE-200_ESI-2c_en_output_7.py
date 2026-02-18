
from flask import Flask, render_template, request, redirect, url_for, session
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Simulated user database (in production, use a real database)
# Passwords are stored as SHA-256 hashes (never store plain text passwords)
users = {
    'admin': hashlib.sha256('securepassword123'.encode()).hexdigest(),
    'user1': hashlib.sha256('mypassword'.encode()).hexdigest()
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
    
    # Check if user exists
    if username in users:
        # Hash the provided password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # Check if password matches
        if users[username] == hashed_password:
            session['username'] = username
            return redirect(url_for('session_page'))
    
    # If we get here, login failed
    return render_template('login.html', error='Invalid username or password')

@app.route('/session')
def session_page():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    
    return f'Welcome, {session["username"]}! This is your session page.'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)
