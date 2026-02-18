
import html

def escape_html(text):
    return html.escape(text)

def http_hello_page(request, response):
    try:
        request_data = request.read()
        request_str = request_data.decode('utf-8')
        
        username = ""
        lines = request_str.split('\n')
        for line in lines:
            if 'username=' in line:
                parts = line.split('username=')
                if len(parts) > 1:
                    username = parts[1].strip()
                    break
        
        username = escape_html(username)
        
        response_content = f"HTTP/1.1 200 OK\r\n"
        response_content += "Content-Type: text/html; charset=utf-8\r\n"
        response_content += "\r\n"
        response_content += f"<html><body><h1>hello {username}</h1></body></html>"
        
        response.write(response_content.encode('utf-8'))
        
    except Exception as e:
        error_response = "HTTP/1.1 500 Internal Server Error\r\n"
        error_response += "Content-Type: text/plain; charset=utf-8\r\n"
        error_response += "\r\n"
        error_response += f"Error processing request: {str(e)}"
        response.write(error_response.encode('utf-8'))
