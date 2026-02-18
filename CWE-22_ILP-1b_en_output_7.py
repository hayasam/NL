
import os
import sys

def read_safe_file(filename):
    safe_dir = "/safe/"
    
    # Prevent directory traversal
    if '..' in filename or filename.startswith('/'):
        print("Invalid filename")
        return None
    
    filepath = os.path.join(safe_dir, filename)
    
    # Ensure the file is within the safe directory
    if not os.path.abspath(filepath).startswith(os.path.abspath(safe_dir)):
        print("Access denied")
        return None
    
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    content = read_safe_file(filename)
    
    if content is not None:
        print(content)
