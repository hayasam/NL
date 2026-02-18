
from flask import Flask, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>User Info</title>
</head>
<body>
    <h1>User Information</h1>
    <p><strong>Username:</strong> {{ username }}</p>
    <p><strong>Email:</strong> {{ email }}</p>
    <p><strong>SSN Last 4:</strong> {{ ssn_last4 }}</p>
</body>
</html>
"""

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', 'Not provided')
    email = session.get('email', 'Not provided')
    ssn = session.get('ssn', '')
    
    ssn_last4 = '****' if len(ssn) >= 4 else 'Invalid'
    if len(ssn) >= 4:
        ssn_last4 = ssn[-4:]
    
    return render_template_string(HTML_TEMPLATE, 
                                 username=username, 
                                 email=email, 
                                 ssn_last4=ssn_last4)

if __name__ == '__main__':
    app.run(debug=True)
