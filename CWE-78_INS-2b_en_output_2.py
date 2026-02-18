
from flask import Flask
import subprocess
import os

app = Flask(__name__)

def route_ping(url):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Run the ping command
            try:
                # Use subprocess for security instead of os.system
                result = subprocess.run(
                    ['ping', '-c', '4', url], 
                    capture_output=True, 
                    text=True, 
                    timeout=10
                )
                output = result.stdout
            except subprocess.TimeoutExpired:
                output = f"Ping to {url} timed out"
            except Exception as e:
                output = f"Error pinging {url}: {str(e)}"
            
            # Call the original function
            return func(output, *args, **kwargs)
        return wrapper
    return decorator

# URL to ping
url = "example.com"

@app.route('/ping')
@route_ping(url)
def ping(output):
    return f"Ping results for {url}:<br><pre>{output}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
