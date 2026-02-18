
import sys

def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string if needed
    if isinstance(request_data, bytes):
        request_data = request_data.decode('utf-8')
    
    # Parse the username from the request
    username = "Guest"  # Default value
    
    # Look for username in query parameters (simplified parsing)
    lines = request_data.split('\n')
    for line in lines:
        if '?' in line and 'username=' in line:
            # Extract from query string
            query_part = line.split('?')[1].split(' ')[0]
            params = query_part.split('&')
            for param in params:
                if param.startswith('username='):
                    username = param.split('=')[1]
                    break
        elif 'username=' in line and '?' not in line:
            # Try to extract from POST data or other locations
            parts = line.split('username=')
            if len(parts) > 1:
                username = parts[1].split('&')[0] if '&' in parts[1] else parts[1]
    
    # Construct the response
    response_content = f"Hello {username}"
    
    # Write HTTP response headers
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html; charset=utf-8\r\n")
    response.write(f"Content-Length: {len(response_content)}\r\n".encode('utf-8'))
    response.write(b"\r\n")
    
    # Write the response body
    response.write(response_content.encode('utf-8'))
    response.flush()
