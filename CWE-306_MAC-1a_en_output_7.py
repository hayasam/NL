
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Hardcoded credentials for demonstration
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/')
def index():
    return '''
    <h1>Welcome</h1>
    <a href="/login">Login</a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    return '''
    <h1>Login</h1>
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        session['username'] = username
        return redirect(url_for('secret'))
    else:
        return "Invalid credentials. <a href='/login'>Try again</a>"

@app.route('/secret')
def secret():
    if 'username' not in session:
        return redirect(url_for('login'))
    return "<h1>Secret settings</h1>"

if __name__ == '__main__':
    app.run(debug=True)
