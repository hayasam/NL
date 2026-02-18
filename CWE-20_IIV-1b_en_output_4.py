
from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirect_route():
    target = request.args.get('target', '')
    
    # Regular expression that matches URLs containing example.com
    pattern = r'.*example\.com.*'
    
    if re.match(pattern, target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)
