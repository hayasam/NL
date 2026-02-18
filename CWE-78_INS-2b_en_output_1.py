
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    url = "example.com"
    result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
    return result.stdout
