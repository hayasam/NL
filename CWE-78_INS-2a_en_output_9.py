
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided"
    
    try:
        result = subprocess.run(['ping', '-c', '4', url], 
                              capture_output=True, text=True, timeout=10)
        output = result.stdout
        if result.returncode != 0:
            output += f"\nError: {result.stderr}"
    except subprocess.TimeoutExpired:
        output = "Error: Ping command timed out"
    except Exception as e:
        output = f"Error: {str(e)}"
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
