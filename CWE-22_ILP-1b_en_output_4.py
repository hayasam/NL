
import os
import sys

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    # Prevent directory traversal
    if '..' in filename or filename.startswith('/') or '~' in filename:
        return "Error: Invalid filename"
    
    filepath = os.path.join(safe_dir, filename)
    
    # Ensure the file is within the safe directory
    if not os.path.abspath(filepath).startswith(os.path.abspath(safe_dir)):
        return "Error: Access denied"
    
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Permission denied"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    result = read_safe_file(filename)
    print(result)
