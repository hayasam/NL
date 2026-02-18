
import os
import sys

def read_file_from_safe_directory(filename, safe_directory):
    """
    Read a file from a specified safe directory.
    
    Args:
        filename: Name of the file to read
        safe_directory: Path to the safe directory
    
    Returns:
        Content of the file as string
    
    Raises:
        ValueError: If filename contains path traversal attempts
        FileNotFoundError: If file doesn't exist
        IOError: If there are file reading issues
    """
    # Normalize paths
    safe_directory = os.path.abspath(safe_directory)
    requested_path = os.path.abspath(os.path.join(safe_directory, filename))
    
    # Security check: ensure the requested path is within safe directory
    if not requested_path.startswith(safe_directory):
        raise ValueError("Path traversal attempt detected")
    
    # Check if file exists
    if not os.path.exists(requested_path):
        raise FileNotFoundError(f"File '{filename}' not found in safe directory")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(requested_path):
        raise ValueError(f"'{filename}' is not a file")
    
    # Read and return file content
    try:
        with open(requested_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Fallback to binary mode if UTF-8 fails
        with open(requested_path, 'rb') as file:
            return file.read()

def main():
    # Example usage
    if len(sys.argv) != 3:
        print("Usage: python script.py <safe_directory> <filename>")
        sys.exit(1)
    
    safe_dir = sys.argv[1]
    filename = sys.argv[2]
    
    try:
        content = read_file_from_safe_directory(filename, safe_dir)
        print(content)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
