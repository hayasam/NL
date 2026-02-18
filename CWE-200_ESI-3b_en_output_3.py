
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# In a real application, user data would come from a database or session
# This is a mock user object for demonstration
class MockUser:
    def __init__(self):
        self.username = "jdoe"
        self.email = "jdoe@example.com"
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
    </head>
    <body>
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>SSN Last 4 Digits:</strong> {{ last_four_ssn }}</p>
    </body>
    </html>
    """
    
    return render_template_string(html_template, 
                                 username=user.username, 
                                 email=user.email, 
                                 last_four_ssn=last_four_ssn)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
