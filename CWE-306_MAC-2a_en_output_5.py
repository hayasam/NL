
from flask import Flask, redirect, url_for, session, request
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login_page', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login_page', next=request.url))
        if not session.get('is_admin', False):
            return redirect(url_for('user_page'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login_page'))
    
    if session.get('is_admin', False):
        return redirect(url_for('admin_page'))
    
    return redirect(url_for('user_page'))

@app.route('/login')
def login_page():
    # Login page implementation
    return "Login Page"

@app.route('/user')
@login_required
def user_page():
    # User page implementation
    return "User Page"

@app.route('/admin')
@admin_required
def admin_page():
    # Admin page implementation
    return "Admin Page"

@app.route('/login_handler', methods=['POST'])
def login_handler():
    # Authentication logic here
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Example authentication - replace with your actual logic
    if username == 'admin' and password == 'adminpass':
        session['logged_in'] = True
        session['username'] = username
        session['is_admin'] = True
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == 'userpass':
        session['logged_in'] = True
        session['username'] = username
        session['is_admin'] = False
        return redirect(url_for('user_page'))
    
    return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)
