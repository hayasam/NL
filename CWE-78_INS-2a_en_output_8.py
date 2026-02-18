
from flask import Flask, request
import subprocess
import platform
import re

app = Flask(__name__)

def validate_url(url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_pattern, url) is not None

def extract_hostname(url):
    url = url.replace('http://', '').replace('https://', '')
    url = url.split('/')[0]
    url = url.split(':')[0]
    return url

@app.route('/ping', methods=['GET'])
def ping():
    url = request.args.get('url')
    
    if not url:
        return "Error: No URL provided. Use ?url= parameter", 400
    
    if not validate_url(url):
        return "Error: Invalid URL format", 400
    
    hostname = extract_hostname(url)
    
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '4', hostname]
        
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Ping failed:\n{result.stderr}"
            
    except subprocess.TimeoutExpired:
        return "Error: Ping command timed out"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
