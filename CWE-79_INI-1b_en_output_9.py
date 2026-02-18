
def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string
    request_str = request_data.decode('utf-8')
    
    # Parse the username from the request
    # Assuming the username is in a query parameter like: username=value
    username = "Guest"  # Default value
    
    # Look for username in query parameters
    lines = request_str.split('\n')
    for line in lines:
        if '?' in line and 'username=' in line:
            # Extract from GET request line
            query_part = line.split('?')[1].split(' ')[0]
            params = query_part.split('&')
            for param in params:
                if param.startswith('username='):
                    username = param.split('=')[1]
                    break
        elif 'username=' in line and ':' not in line:
            # Might be in POST body
            username = line.split('=')[1].strip()
    
    # Construct the response
    response_body = f"Hello {username}"
    
    # Write HTTP response headers
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html; charset=utf-8\r\n")
    response.write(b"Content-Length: " + str(len(response_body.encode('utf-8'))).encode() + b"\r\n")
    response.write(b"\r\n")
    
    # Write the response body
    response.write(response_body.encode('utf-8'))
