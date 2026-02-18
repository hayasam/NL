
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# In a real application, user data would come from a database or session
# This is a mock user for demonstration purposes
MOCK_USER = {
    'username': 'johndoe',
    'email': 'john.doe@example.com',
    'ssn_last_four': '1234'
}

@app.route('/info')
def user_info():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Information</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .info-container { max-width: 600px; margin: 0 auto; }
            .info-item { margin: 15px 0; }
            .label { font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="info-container">
            <h1>User Information</h1>
            <div class="info-item">
                <span class="label">Username:</span> {{ username }}
            </div>
            <div class="info-item">
                <span class="label">Email:</span> {{ email }}
            </div>
            <div class="info-item">
                <span class="label">SSN Last 4 Digits:</span> {{ ssn_last_four }}
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(
        html_template,
        username=MOCK_USER['username'],
        email=MOCK_USER['email'],
        ssn_last_four=MOCK_USER['ssn_last_four']
    )

if __name__ == '__main__':
    app.run(debug=True)
