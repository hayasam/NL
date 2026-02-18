
from flask import Flask, request
import subprocess
import platform
import re

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided"
    
    if not re.match(r'^[a-zA-Z0-9.-]+$', url):
        return "Error: Invalid URL format"
    
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    count = '4'
    
    try:
        result = subprocess.run(
            ['ping', param, count, url],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout or result.stderr
    except subprocess.TimeoutExpired:
        output = "Ping request timed out"
    except Exception as e:
        output = f"Error: {str(e)}"
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
