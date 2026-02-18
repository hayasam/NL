
from flask import Flask, redirect, request, abort
import urllib.parse

app = Flask(__name__)

def is_valid_url(url):
    """Check if URL belongs to example.com domain"""
    try:
        parsed = urllib.parse.urlparse(url)
        # Check if netloc ends with example.com (allows subdomains)
        return parsed.netloc.endswith('example.com')
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
        abort(400, description="Invalid URL: Only example.com domains are allowed")

if __name__ == '__main__':
    app.run(debug=True)
