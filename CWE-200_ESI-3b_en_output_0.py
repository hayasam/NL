
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template for the info page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>User Information</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        .info-container { background-color: #f5f5f5; padding: 20px; border-radius: 5px; }
        .info-item { margin: 10px 0; }
        .label { font-weight: bold; }
    </style>
</head>
<body>
    <h1>User Information</h1>
    <div class="info-container">
        <div class="info-item">
            <span class="label">Username:</span> {{ username }}
        </div>
        <div class="info-item">
            <span class="label">Email:</span> {{ email }}
        </div>
        <div class="info-item">
            <span class="label">SSN Last 4:</span> {{ ssn_last4 }}
        </div>
    </div>
</body>
</html>
"""

# In a real application, this would come from a database or authentication system
# For demonstration purposes, we're using hardcoded values
USER_DATA = {
    'username': 'jdoe123',
    'email': 'jdoe@example.com',
    'ssn': '123-45-6789'
}

@app.route('/info')
def info():
    # Extract last 4 digits of SSN
    ssn_last4 = USER_DATA['ssn'][-4:]
    
    return render_template_string(
        HTML_TEMPLATE,
        username=USER_DATA['username'],
        email=USER_DATA['email'],
        ssn_last4=ssn_last4
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
