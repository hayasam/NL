
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = "example.com"
    try:
        result = subprocess.run(['ping', '-c', '4', url], 
                              capture_output=True, text=True, timeout=10)
        return result.stdout if result.returncode == 0 else result.stderr
    except subprocess.TimeoutExpired:
        return "Ping request timed out"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
