
from flask import Flask, send_file
import os

app = Flask(__name__)

def check_file_exists(route):
    def decorator(func):
        def wrapper(filename):
            file_path = os.path.join('images', filename)
            if os.path.exists(file_path):
                return func(filename)
            else:
                return "File not found", 404
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

@app.route('/images/<filename>')
@check_file_exists('/images/<filename>')
def serve_image(filename):
    return send_file(os.path.join('images', filename))

if __name__ == '__main__':
    app.run(debug=True)
