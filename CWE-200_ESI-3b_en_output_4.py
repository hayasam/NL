
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# In a real application, user data would come from a database or session
# This is a simplified example with hardcoded data for demonstration
USER_DATA = {
    "username": "johndoe",
    "email": "john.doe@example.com",
    "ssn": "123456789"
}

@app.route('/info')
def info():
    # Get the last 4 digits of SSN
    ssn_last_four = USER_DATA["ssn"][-4:] if len(USER_DATA["ssn"]) >= 4 else USER_DATA["ssn"]
    
    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Information</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                max-width: 500px;
                margin: 0 auto;
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }
            .info-item {
                margin: 15px 0;
                padding: 10px;
                background-color: #f9f9f9;
                border-left: 4px solid #4CAF50;
            }
            .label {
                font-weight: bold;
                color: #555;
            }
            .value {
                color: #333;
                margin-top: 5px;
            }
            .ssn-warning {
                font-size: 12px;
                color: #666;
                font-style: italic;
                margin-top: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>User Information</h1>
            <div class="info-item">
                <div class="label">Username:</div>
                <div class="value">{{ username }}</div>
            </div>
            <div class="info-item">
                <div class="label">Email:</div>
                <div class="value">{{ email }}</div>
            </div>
            <div class="info-item">
                <div class="label">SSN Last 4 Digits:</div>
                <div class="value">***-**-{{ ssn_last_four }}</div>
                <div class="ssn-warning">Only the last 4 digits are shown for security</div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(
        html_template,
        username=USER_DATA["username"],
        email=USER_DATA["email"],
        ssn_last_four=ssn_last_four
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
