
from flask import Flask, request
import subprocess
import platform

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided"
    
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', url]
    
    try:
        output = subprocess.run(command, capture_output=True, text=True, timeout=10)
        return output.stdout if output.returncode == 0 else output.stderr
    except subprocess.TimeoutExpired:
        return "Ping request timed out"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
