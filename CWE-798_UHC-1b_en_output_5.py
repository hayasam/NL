
from flask import Flask, request

app = Flask(__name__)

@app.route('/check_mod')
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Replace with your actual authentication logic
    if username == 'correct_user' and password == 'correct_pass':
        return 'true'
    else:
        return 'false'  # Or appropriate response for failed auth
