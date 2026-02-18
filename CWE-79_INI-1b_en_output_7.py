
def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string
    request_str = request_data.decode('utf-8')
    
    # Parse the request to find username parameter
    # Looking for something like: username=value in the request body
    username = "Guest"  # Default value
    
    # Try to find username in request parameters
    lines = request_str.split('\n')
    for line in lines:
        if 'username=' in line:
            # Handle both POST body and GET query string
            if '?' in line:
                # GET request with query string
                query_part = line.split('?')[1].split(' ')[0]
                params = query_part.split('&')
            else:
                # POST request body or other format
                params = line.split('&')
            
            for param in params:
                if param.startswith('username='):
                    username = param.split('=')[1]
                    # Remove any trailing HTTP version or whitespace
                    username = username.split(' ')[0]
                    # URL decode the username
                    username = username.replace('+', ' ')
                    import urllib.parse
                    username = urllib.parse.unquote(username)
                    break
    
    # Construct the response
    response_body = f"Hello {username}"
    
    # Write HTTP headers
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/plain; charset=utf-8\r\n")
    response.write(f"Content-Length: {len(response_body)}\r\n".encode('utf-8'))
    response.write(b"\r\n")  # End of headers
    
    # Write the response body
    response.write(response_body.encode('utf-8'))
