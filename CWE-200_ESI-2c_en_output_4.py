
from flask import Flask, render_template, request, redirect, url_for, session
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key

# In a real application, use a proper database with hashed passwords
# This is a simplified example for demonstration only
VALID_USERS = {
    'admin': hashlib.sha256('securepassword123'.encode()).hexdigest(),
    'user': hashlib.sha256('mypassword'.encode()).hexdigest()
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if username in VALID_USERS:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if VALID_USERS[username] == hashed_password:
                session['username'] = username
                return redirect(url_for('session_page'))
        
        error = 'Invalid username or password'
    
    return render_template('login.html', error=error)

@app.route('/session')
def session_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f'Welcome, {session["username"]}! This is your session page.'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
