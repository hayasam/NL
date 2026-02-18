
from flask import Flask, send_file
import os

app = Flask(__name__)

def check_image_exists(route):
    def decorator(func):
        def wrapper(filename):
            image_path = os.path.join('images', filename)
            if os.path.exists(image_path):
                return func(image_path)
            else:
                return "File not found", 404
        wrapper.__name__ = func.__name__
        app.route(route)(wrapper)
        return wrapper
    return decorator

@app.route('/')
def index():
    return "Image server is running"

@check_image_exists('/images/<filename>')
def serve_image(image_path):
    return send_file(image_path)

if __name__ == '__main__':
    app.run(debug=True)
