
from flask import Flask, render_template, request, redirect, url_for, session
import functools

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Mock user database
USERS = {
    'user': {'password': 'userpass', 'role': 'user'},
    'admin': {'password': 'adminpass', 'role': 'admin'}
}

def login_required(role=None):
    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))
            if role and USERS.get(session.get('username'), {}).get('role') != role:
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/login', methods=['GET'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = USERS.get(username)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
        return redirect(url_for('index'))
    
    return render_template('login.html', error='Invalid credentials')

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/user_page')
@login_required(role='user')
def user_page():
    return render_template('user_page.html', username=session['username'])

@app.route('/admin_page')
@login_required(role='admin')
def admin_page():
    return render_template('admin_page.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
