
def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string
    request_text = request_data.decode('utf-8')
    
    # Parse the username from the request
    # Assuming the request contains a line like: "username=value"
    username = "Guest"  # Default value
    
    # Look for username in request parameters
    for line in request_text.split('\n'):
        if 'username=' in line:
            # Extract username value
            parts = line.split('username=')
            if len(parts) > 1:
                username = parts[1].strip()
                # Remove any trailing HTTP parameters or newlines
                username = username.split('&')[0]
                username = username.split(' ')[0]
                break
    
    # Construct the response
    response_text = f"Hello {username}"
    
    # Write HTTP headers
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/plain; charset=utf-8\r\n")
    response.write(b"Content-Length: " + str(len(response_text.encode('utf-8'))).encode() + b"\r\n")
    response.write(b"\r\n")
    
    # Write the response body
    response.write(response_text.encode('utf-8'))
