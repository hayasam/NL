
def http_hello_page(request, response):
    try:
        # Read request body (username)
        content_length = int(request.headers.get('Content-Length', 0))
        username = request.rfile.read(content_length).decode('utf-8').strip() if content_length > 0 else ""
        
        # Construct response body
        outputbuf = f"""<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello, {username if username else 'Guest'}!</h1>
</body>
</html>"""
        
        # Write response
        response.send_response(200)
        response.send_header('Content-Type', 'text/html; charset=utf-8')
        response.send_header('Content-Length', str(len(outputbuf.encode('utf-8'))))
        response.end_headers()
        response.wfile.write(outputbuf.encode('utf-8'))
        
    except Exception as e:
        response.send_response(500)
        response.end_headers()
        response.wfile.write(f"Error: {str(e)}".encode('utf-8'))
    
    # Close response stream
    response.wfile.flush()
