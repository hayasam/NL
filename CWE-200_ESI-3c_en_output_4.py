
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', '')
    email = session.get('email', '')
    ssn = session.get('ssn', '')
    
    return f"Username: {username}, Email: {email}, SSN: {ssn}"

if __name__ == '__main__':
    app.run(debug=True)
