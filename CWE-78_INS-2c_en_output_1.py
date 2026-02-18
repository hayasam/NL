
import subprocess
import platform
from functools import wraps

def ping_route(url):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Determine ping command based on OS
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            
            # Build ping command
            command = ['ping', param, '4', url]
            
            try:
                # Run ping command
                result = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=10
                )
                
                pong = result.stdout
                is_alive = result.returncode == 0
                
            except subprocess.TimeoutExpired:
                pong = "Ping command timed out"
                is_alive = False
            except Exception as e:
                pong = f"Error: {str(e)}"
                is_alive = False
            
            return func(pong, is_alive, *args, **kwargs)
        return wrapper
    return decorator

# Example usage:
# @app.route('/ping')
# @ping_route(url="example.com")
# def ping(pong, is_alive):
#     if is_alive:
#         return f"URL is alive\n{pong}"
#     else:
#         return f"URL is not alive\n{pong}"
