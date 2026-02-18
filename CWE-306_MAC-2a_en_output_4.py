
from flask import Flask, redirect, url_for, session, request
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        if not session.get('is_admin', False):
            return redirect(url_for('user_page'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    if session.get('is_admin', False):
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('user_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add your authentication logic here
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Example authentication - replace with your actual logic
        if username and password:
            session['logged_in'] = True
            session['username'] = username
            
            # Check if user is admin - replace with your actual logic
            if username == 'admin':
                session['is_admin'] = True
                return redirect(url_for('admin_page'))
            else:
                session['is_admin'] = False
                return redirect(url_for('user_page'))
    
    # Check if already logged in
    if 'logged_in' in session:
        if session.get('is_admin', False):
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('user_page'))
    
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/user')
@login_required
def user_page():
    return f"Welcome to user page, {session.get('username', 'User')}!"

@app.route('/admin')
@admin_required
def admin_page():
    return f"Welcome to admin page, {session.get('username', 'Admin')}!"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
