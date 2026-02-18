
from flask import Flask, send_file
import os

app = Flask(__name__)

def serve_image(filename):
    def decorator(func):
        @app.route(filename)
        def wrapper():
            image_path = os.path.join('images', filename)
            if os.path.exists(image_path):
                return send_file(image_path)
            return func()
        return wrapper
    return decorator

@serve_image('example.jpg')
def image_not_found():
    return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True)
