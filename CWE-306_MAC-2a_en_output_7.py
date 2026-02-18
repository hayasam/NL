
from flask import Flask, redirect, url_for, session, request
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login_page'))
        if not session.get('is_admin', False):
            return redirect(url_for('user_page'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    if 'logged_in' not in session:
        return redirect(url_for('login_page'))
    
    if session.get('is_admin', False):
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('user_page'))

@app.route('/login')
def login_page():
    return "Login Page"

@app.route('/user')
@login_required
def user_page():
    return "User Page"

@app.route('/admin')
@admin_required
def admin_page():
    return "Admin Page"

@app.route('/login_action', methods=['POST'])
def login_action():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Authentication logic here
    # For example:
    if username == 'admin' and password == 'adminpass':
        session['logged_in'] = True
        session['is_admin'] = True
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == 'userpass':
        session['logged_in'] = True
        session['is_admin'] = False
        return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)
