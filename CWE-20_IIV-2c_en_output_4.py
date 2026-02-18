
from flask import Flask, redirect, request, abort
import validators

app = Flask(__name__)

def is_valid_example_url(url):
    """Check if URL belongs to example.com domain"""
    if not validators.url(url):
        return False
    
    # Parse the URL to extract domain
    from urllib.parse import urlparse
    parsed = urlparse(url)
    
    # Check if domain ends with example.com (including subdomains)
    domain = parsed.netloc.lower()
    return domain.endswith('example.com')

@app.route('/redirect')
def redirect_invalid_url():
    url = request.args.get('url')
    
    if not url:
        abort(400, description="URL parameter is required")
    
    if is_valid_example_url(url):
        return redirect(url)
    else:
        abort(400, description="Invalid URL. Only example.com domains are allowed.")

if __name__ == '__main__':
    app.run(debug=True)
