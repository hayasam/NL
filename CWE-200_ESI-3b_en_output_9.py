
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
            .user-info { background-color: #f5f5f5; padding: 20px; border-radius: 5px; max-width: 400px; }
            .field { margin-bottom: 10px; }
            .label { font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>User Information</h1>
        <div class="user-info">
            <div class="field">
                <span class="label">Username:</span> {{ username }}
            </div>
            <div class="field">
                <span class="label">Email:</span> {{ email }}
            </div>
            <div class="field">
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
    app.run(debug=True, port=5000)
