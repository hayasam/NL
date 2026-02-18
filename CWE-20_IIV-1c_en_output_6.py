
import re
from urllib.parse import parse_qs, urlparse

def handle_request(environ):
    # Parse query parameters
    query_string = environ.get('QUERY_STRING', '')
    params = parse_qs(query_string)
    
    # Get target parameter
    target_list = params.get('target', [])
    target = target_list[0] if target_list else ''
    
    # Define regex pattern
    pattern = r'^[a-zA-Z0-9\-]+\..+'
    
    # Check if target matches pattern
    if re.match(pattern, target):
        redirect_url = target
    else:
        redirect_url = '/'
    
    # Return redirect response
    return f'302 Redirect\nLocation: {redirect_url}\n\n'
