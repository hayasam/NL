
from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided"
    
    if not re.match(r'^[a-zA-Z0-9.-]+$', url):
        return "Error: Invalid URL format"
    
    try:
        result = subprocess.run(
            ['ping', '-c', '4', url],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout
        if result.returncode != 0:
            output += f"\nPing failed with return code: {result.returncode}"
    except subprocess.TimeoutExpired:
        output = "Ping command timed out"
    except Exception as e:
        output = f"Error executing ping: {str(e)}"
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
