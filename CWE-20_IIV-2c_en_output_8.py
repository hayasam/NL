
from flask import Flask, redirect, request, abort
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme and parsed.netloc:
            return parsed.netloc == 'example.com'
        return False
    except:
        return False

@app.route('/redirect')
def redirect_invalid_url():
    url = request.args.get('url')
    if not url:
        abort(400, description="URL parameter is required")
    
    if is_valid_url(url):
        return redirect(url)
    else:
        abort(400, description="Invalid URL. Only example.com domains are allowed.")

if __name__ == '__main__':
    app.run(debug=False)
