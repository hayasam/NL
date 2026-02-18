
import subprocess
from flask import Flask, escape

app = Flask(__name__)

def bind_to_url(url):
    def decorator(func):
        @app.route(url)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@bind_to_url('/ping')
def ping():
    url = "example.com"
    result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
    return f'<pre>{escape(result.stdout)}</pre>'

if __name__ == '__main__':
    app.run()
