
from flask import Flask, redirect, request, abort
import urllib.parse

app = Flask(__name__)

def is_valid_url(url):
    """Check if URL belongs to example.com"""
    try:
        parsed = urllib.parse.urlparse(url)
        # Check if netloc ends with example.com (allows subdomains)
        return parsed.netloc.endswith('example.com')
    except:
        return False

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    # Ensure URL has a scheme
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    if is_valid_url(url):
        return redirect(url)
    else:
        abort(400, description="Invalid URL: Only URLs from example.com are allowed")

if __name__ == '__main__':
    app.run(debug=True)
