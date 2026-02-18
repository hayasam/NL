
import os

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    # Prevent directory traversal
    if '..' in filename or filename.startswith('/') or '\\' in filename:
        raise ValueError("Invalid filename")
    
    # Ensure file is within safe directory
    full_path = os.path.join(safe_dir, filename)
    normalized_path = os.path.normpath(full_path)
    
    if not normalized_path.startswith(os.path.abspath(safe_dir)):
        raise ValueError("Access denied")
    
    # Check if file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {filename}")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(normalized_path):
        raise ValueError("Not a regular file")
    
    # Read and return file content
    with open(normalized_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    try:
        filename = input("Enter filename to read from /safe/ directory: ")
        content = read_safe_file(filename)
        print(content)
    except Exception as e:
        print(f"Error: {e}")
