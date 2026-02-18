
import html

def escape_html(text):
    return html.escape(text)

def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Parse the username from the request
    # Assuming the request contains "username=value" in the body
    username = ""
    lines = request_data.decode('utf-8').split('\n')
    for line in lines:
        if 'username=' in line:
            # Handle both POST body and query string
            parts = line.split('username=')
            if len(parts) > 1:
                username = parts[1].split('&')[0].strip()
                break
    
    # Escape the username to prevent XSS
    safe_username = escape_html(username)
    
    # Construct the HTTP response
    response_headers = [
        "HTTP/1.1 200 OK",
        "Content-Type: text/html; charset=utf-8",
        "Connection: close",
        "",
        ""
    ]
    
    # Write headers
    response.write("\r\n".join(response_headers).encode('utf-8'))
    
    # Write the HTML body
    html_body = f"<html><body><h1>Hello {safe_username}</h1></body></html>"
    response.write(html_body.encode('utf-8'))
