
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Hardcoded credentials for demonstration
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    return render_template('login.html')

def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        session['username'] = username
        return redirect(url_for('secret'))
    else:
        return redirect(url_for('login'))

@app.route('/secret')
def secret():
    if 'username' in session:
        return "Secret settings"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
