
import sys

def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string if needed
    if isinstance(request_data, bytes):
        request_data = request_data.decode('utf-8')
    
    # Parse username from request (assuming simple GET request format)
    username = "Guest"  # Default value
    
    # Look for username parameter in query string
    lines = request_data.split('\n')
    if lines and '?' in lines[0]:
        # Parse the request line
        request_line = lines[0]
        # Extract query string part
        query_part = request_line.split('?', 1)[1].split(' ', 1)[0]
        
        # Parse query parameters
        params = query_part.split('&')
        for param in params:
            if '=' in param:
                key, value = param.split('=', 1)
                if key == 'username':
                    username = value
                    break
    
    # Construct response
    response_body = f"Hello {username}"
    
    # Write HTTP response
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/plain\r\n")
    response.write(b"Content-Length: " + str(len(response_body)).encode() + b"\r\n")
    response.write(b"\r\n")
    response.write(response_body.encode('utf-8'))
    response.flush()
