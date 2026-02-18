
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
        ValueError: If the requested file path is not within the safe directory
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    # Convert to absolute paths
    safe_dir = pathlib.Path(safe_directory).resolve()
    requested_path = (safe_dir / filename).resolve()
    
    # Security check: Ensure the requested path is within the safe directory
    try:
        # Check if requested_path is relative to safe_dir
        requested_path.relative_to(safe_dir)
    except ValueError:
        raise ValueError(f"Access to {requested_path} is not allowed. File must be within {safe_dir}")
    
    # Check if file exists
    if not requested_path.exists():
        raise FileNotFoundError(f"File {filename} not found in {safe_directory}")
    
    # Check if it's a file (not a directory)
    if not requested_path.is_file():
        raise IOError(f"{requested_path} is not a file")
    
    # Read and return the file content
    try:
        with open(requested_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # If utf-8 fails, try reading as binary
        with open(requested_path, 'rb') as file:
            return file.read()

# Example usage:
if __name__ == "__main__":
    # Define your safe directory
    SAFE_DIR = "/path/to/safe/directory"
    
    # Example: Read a file
    try:
        content = read_file_from_safe_directory("example.txt", SAFE_DIR)
        print("File content read successfully")
    except Exception as e:
        print(f"Error: {e}")
