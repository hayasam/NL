
from flask import Flask, render_template, request, redirect, url_for, session
import functools

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

def login_required(role="user"):
    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))
            if role == "admin" and session.get('role') != 'admin':
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Simple authentication logic - replace with proper authentication
    if username == 'admin' and password == 'admin123':
        session['username'] = username
        session['role'] = 'admin'
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == 'user123':
        session['username'] = username
        session['role'] = 'user'
        return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login'))

@app.route('/')
@login_required()
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/user')
@login_required(role="user")
def user_page():
    return render_template('user.html', username=session.get('username'))

@app.route('/admin')
@login_required(role="admin")
def admin_page():
    return render_template('admin.html', username=session.get('username'))

if __name__ == '__main__':
    app.run(debug=True)
