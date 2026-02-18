
from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/img')
def img():
    file = request.args.get('file')
    if file:
        try:
            return send_file(file)
        except Exception:
            return "File not found", 404
    return "No file specified", 400

if __name__ == '__main__':
    app.run(debug=True)
