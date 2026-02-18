
from flask import Flask, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>User Information</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .info { background-color: #f5f5f5; padding: 20px; border-radius: 5px; }
        .field { margin: 10px 0; }
        .label { font-weight: bold; }
    </style>
</head>
<body>
    <h1>User Information</h1>
    <div class="info">
        <div class="field">
            <span class="label">Username:</span> {{ username }}
        </div>
        <div class="field">
            <span class="label">Email:</span> {{ email }}
        </div>
        <div class="field">
            <span class="label">SSN Last 4:</span> {{ ssn_last4 }}
        </div>
    </div>
</body>
</html>
"""

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', 'Not provided')
    email = session.get('email', 'Not provided')
    ssn = session.get('ssn', '')
    
    ssn_last4 = '****' if len(ssn) >= 4 else 'Not provided'
    if len(ssn) >= 4:
        ssn_last4 = f"***-**-{ssn[-4:]}"
    
    return render_template_string(HTML_TEMPLATE, 
                                 username=username, 
                                 email=email, 
                                 ssn_last4=ssn_last4)

if __name__ == '__main__':
    app.run(debug=True)
