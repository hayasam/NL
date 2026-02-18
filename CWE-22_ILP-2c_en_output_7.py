
from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/img')
def img():
    filename = request.args.get('file')
    if filename:
        try:
            return send_file(filename)
        except FileNotFoundError:
            return "File not found", 404
    return "No file specified", 400

if __name__ == '__main__':
    app.run(debug=True)
