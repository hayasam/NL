
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# In a real application, user data would come from a database or session
# This is a mock user object for demonstration
class MockUser:
    def __init__(self):
        self.username = "johndoe"
        self.email = "john.doe@example.com"
        self.ssn = "123-45-6789"

@app.route('/info')
def info():
    user = MockUser()
    
    # Extract last 4 digits of SSN
    ssn_last_four = user.ssn.replace('-', '')[-4:]
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Information</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .info-container { max-width: 500px; margin: 0 auto; }
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
    
    return render_template_string(html_template, 
                                 username=user.username, 
                                 email=user.email, 
                                 ssn_last_four=ssn_last_four)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
