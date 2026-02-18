
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
                result = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=5
                )
                pong = result.stdout
                is_alive = result.returncode == 0
            except subprocess.TimeoutExpired:
                pong = "Ping timeout"
                is_alive = False
            except Exception as e:
                pong = f"Error: {str(e)}"
                is_alive = False
            
            return func(pong, is_alive, *args, **kwargs)
        return wrapper
    return decorator

# Example usage with Flask (uncomment if using Flask)
# from flask import Flask
# app = Flask(__name__)

# @app.route('/ping')
# @ping_decorator(url="example.com")
# def ping(pong, is_alive):
#     if is_alive:
#         return f"URL is alive\n{pong}"
#     else:
#         return f"URL is not alive\n{pong}"
