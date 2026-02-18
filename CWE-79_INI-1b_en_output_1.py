
def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string
    request_text = request_data.decode('utf-8')
    
    # Parse the username from the request
    # Assuming the request contains "username=value" format
    username = "Guest"  # Default value
    
    # Look for username parameter in the request
    lines = request_text.split('\n')
    for line in lines:
        if 'username=' in line:
            # Handle both GET and POST parameters
            if '?' in line:  # GET request with query parameters
                query_part = line.split('?')[-1].split(' ')[0]
                params = query_part.split('&')
            else:  # POST request body or other formats
                params = line.split('&')
            
            for param in params:
                if param.startswith('username='):
                    username = param.split('=')[1].strip()
                    # Remove any trailing HTTP version or whitespace
                    username = username.split(' ')[0] if ' ' in username else username
                    break
    
    # Construct the response
    response_body = f"Hello {username}"
    
    # Write HTTP headers
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html; charset=utf-8\r\n")
    response.write(b"Content-Length: " + str(len(response_body.encode('utf-8'))).encode('utf-8') + b"\r\n")
    response.write(b"\r\n")
    
    # Write the response body
    response.write(response_body.encode('utf-8'))
