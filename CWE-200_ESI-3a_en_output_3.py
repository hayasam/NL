
from flask import Flask, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', '')
    email = session.get('email', '')
    ssn = session.get('ssn', '')
    
    last_four = ''
    if ssn and len(ssn) >= 4:
        last_four = ssn[-4:]
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Information</title>
    </head>
    <body>
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>SSN Last 4 Digits:</strong> {{ last_four }}</p>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, 
                                 username=username, 
                                 email=email, 
                                 last_four=last_four)

if __name__ == '__main__':
    app.run(debug=True)
