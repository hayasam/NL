
import os
import pathlib

def read_file_from_safe_directory(filename, safe_directory):
    """
    Read a file from a safe directory after validating the path.
    
    Args:
        filename: Name of the file to read
        safe_directory: Path to the safe directory
    
    Returns:
        Content of the file as string
    
    Raises:
        ValueError: If path traversal is attempted
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
    """
    # Convert to absolute paths
    safe_dir = pathlib.Path(safe_directory).resolve()
    requested_path = (safe_dir / filename).resolve()
    
    # Check if the requested path is within the safe directory
    try:
        requested_path.relative_to(safe_dir)
    except ValueError:
        raise ValueError("Path traversal attempt detected")
    
    # Check if file exists
    if not requested_path.exists():
        raise FileNotFoundError(f"File '{filename}' not found in safe directory")
    
    # Check if it's a file (not a directory)
    if not requested_path.is_file():
        raise IOError(f"'{filename}' is not a regular file")
    
    # Read and return file content
    try:
        with open(requested_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Fallback to binary mode if UTF-8 fails
        with open(requested_path, 'rb') as file:
            return file.read()

# Example usage
if __name__ == "__main__":
    # Define your safe directory
    SAFE_DIR = "/path/to/safe/directory"
    
    try:
        # Get filename from user input or other source
        requested_file = "example.txt"
        content = read_file_from_safe_directory(requested_file, SAFE_DIR)
        print(content)
    except Exception as e:
        print(f"Error: {e}")
