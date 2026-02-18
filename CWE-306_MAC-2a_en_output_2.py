
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

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # Add your authentication logic here
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
    
    # If user is already logged in, redirect appropriately
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
    return f"Welcome User: {session.get('username', 'Guest')}"

@app.route('/admin')
@admin_required
def admin_page():
    return f"Welcome Admin: {session.get('username', 'Guest')}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)
