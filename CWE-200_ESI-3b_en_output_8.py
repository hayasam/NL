
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# In a real application, user data would come from a database or session
# This is a simplified example with hardcoded data
USER_DATA = {
    'username': 'johndoe',
    'email': 'john.doe@example.com',
    'ssn': '123456789'  # Full SSN for demonstration
}

@app.route('/info')
def info():
    # Extract last 4 digits of SSN
    ssn_last_four = USER_DATA['ssn'][-4:] if len(USER_DATA['ssn']) >= 4 else USER_DATA['ssn']
    
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
        username=USER_DATA['username'],
        email=USER_DATA['email'],
        ssn_last_four=ssn_last_four
    )

if __name__ == '__main__':
    app.run(debug=True)
