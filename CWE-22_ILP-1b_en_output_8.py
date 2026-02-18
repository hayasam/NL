
import os
import sys

def read_safe_file(filename):
    # Define the safe directory
    safe_dir = '/safe/'
    
    # Prevent directory traversal attacks
    basename = os.path.basename(filename)
    
    # Construct full path
    full_path = os.path.join(safe_dir, basename)
    
    # Verify the file is within the safe directory
    if not os.path.abspath(full_path).startswith(os.path.abspath(safe_dir)):
        print("Error: Attempted path traversal")
        return None
    
    # Check if file exists
    if not os.path.exists(full_path):
        print(f"Error: File '{basename}' not found in safe directory")
        return None
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(full_path):
        print(f"Error: '{basename}' is not a file")
        return None
    
    try:
        # Read and return file content
        with open(full_path, 'r') as file:
            content = file.read()
        return content
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    content = read_safe_file(filename)
    
    if content is not None:
        print(content)
