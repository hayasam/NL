
from flask import Flask, request
import subprocess
import platform
import re

app = Flask(__name__)

def validate_url(url):
    """Basic URL validation for ping command safety"""
    if not url:
        return False
    
    # Remove protocol if present
    clean_url = re.sub(r'^https?://', '', url)
    
    # Check for basic domain pattern or IP address
    domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)*$'
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    return bool(re.match(domain_pattern, clean_url) or re.match(ip_pattern, clean_url))

@app.route('/ping')
def ping():
    url = request.args.get('url')
    
    if not url or not validate_url(url):
        return "Invalid URL provided", 400
    
    try:
        # Determine ping command based on OS
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        count = '4'  # Number of ping packets
        
        # Run ping command
        result = subprocess.run(
            ['ping', param, count, url],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout or result.stderr
        
        return output
    
    except subprocess.TimeoutExpired:
        return "Ping command timed out", 504
    except Exception as e:
        return f"Error executing ping: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
