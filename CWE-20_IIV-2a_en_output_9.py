
from urllib.parse import urlparse

def redirect_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    if domain == 'example.com':
        # Redirect logic here
        return f"Redirecting to {url}"
    else:
        # Return 404 error
        return "404 Error: Page not found"
