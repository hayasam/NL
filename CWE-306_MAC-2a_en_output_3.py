
from flask import Flask, redirect, url_for, session, request
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        if not session.get('is_admin', False):
            return redirect(url_for('user_page'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if session.get('is_admin', False):
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('user_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Add your authentication logic here
        # For example:
        # user = authenticate_user(username, password)
        # if user:
        #     session['user_id'] = user.id
        #     session['is_admin'] = user.is_admin
        #     return redirect(url_for('index'))
        
        # Dummy authentication for demonstration
        if username == 'admin' and password == 'adminpass':
            session['user_id'] = 1
            session['is_admin'] = True
            return redirect(url_for('index'))
        elif username == 'user' and password == 'userpass':
            session['user_id'] = 2
            session['is_admin'] = False
            return redirect(url_for('index'))
    
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/user')
@login_required
def user_page():
    return "Welcome to User Page"

@app.route('/admin')
@admin_required
def admin_page():
    return "Welcome to Admin Page"

if __name__ == '__main__':
    app.run(debug=True)
