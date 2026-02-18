
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = "example.com"
    result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
    return result.stdout
