
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
                    timeout=5
                )
                pong = result.stdout.decode('utf-8', errors='ignore')
                alive = result.returncode == 0
            except (subprocess.TimeoutExpired, Exception):
                pong = "Ping command failed or timed out"
                alive = False
            
            return func(pong=pong, alive=alive, *args, **kwargs)
        return wrapper
    return decorator

# Example usage
@ping_decorator(url="example.com")
def ping(pong, alive):
    if alive:
        return f"URL is alive\n{pong}"
    else:
        return f"URL is not alive\n{pong}"
