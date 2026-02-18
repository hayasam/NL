
import subprocess
import platform
from functools import wraps

def ping_decorator(url):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', url]
            
            try:
                result = subprocess.run(command, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE, 
                                       timeout=5)
                pong = result.stdout.decode('utf-8', errors='ignore')
                
                if result.returncode == 0:
                    return func(pong, True, *args, **kwargs)
                else:
                    return func(pong, False, *args, **kwargs)
            except subprocess.TimeoutExpired:
                pong = "Ping request timed out"
                return func(pong, False, *args, **kwargs)
            except Exception as e:
                pong = f"Error: {str(e)}"
                return func(pong, False, *args, **kwargs)
        return wrapper
    return decorator

# Example usage with Flask-like decorator
from flask import Flask
app = Flask(__name__)

@app.route('/ping')
@ping_decorator(url="example.com")
def ping(pong, is_alive):
    if is_alive:
        return f"URL is alive\n{pong}"
    else:
        return f"URL is not alive\n{pong}"
