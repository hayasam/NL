
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# In a real application, user data would come from a database or session
# This is a mock user object for demonstration
class MockUser:
    def __init__(self):
        self.username = "johndoe"
        self.email = "john.doe@example.com"
        self.ssn = "123456789"

@app.route('/info')
def info():
    user = MockUser()
    # Extract last 4 digits of SSN
    last_four_ssn = user.ssn[-4:] if len(user.ssn) >= 4 else user.ssn
    
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
                <span class="label">SSN Last 4 Digits:</span> {{ last_four_ssn }}
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(
        html_template,
        username=user.username,
        email=user.email,
        last_four_ssn=last_four_ssn
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
