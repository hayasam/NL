
import html

def escape_html(text):
    return html.escape(text)

def http_hello_page(request, response):
    try:
        request_data = request.read().decode('utf-8')
        
        username = ""
        lines = request_data.split('\n')
        for line in lines:
            if 'username=' in line:
                if '?' in line:
                    query_part = line.split('?')[1].split(' ')[0]
                else:
                    query_part = line
                
                params = query_part.split('&')
                for param in params:
                    if param.startswith('username='):
                        username = param.split('=')[1]
                        username = escape_html(username)
                        break
                break
        
        response_headers = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "\r\n"
        )
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body>
            <h1>Hello {username}</h1>
        </body>
        </html>
        """
        
        response.write(response_headers.encode('utf-8'))
        response.write(html_content.encode('utf-8'))
        
    except Exception as e:
        error_response = (
            "HTTP/1.1 500 Internal Server Error\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            "\r\n"
            f"Error: {str(e)}"
        )
        response.write(error_response.encode('utf-8'))
