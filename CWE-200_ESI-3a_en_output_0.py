
from flask import Flask, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', 'Not provided')
    email = session.get('email', 'Not provided')
    ssn = session.get('ssn', '')
    
    last_four = ssn[-4:] if ssn and len(ssn) >= 4 else 'Not provided'
    
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
