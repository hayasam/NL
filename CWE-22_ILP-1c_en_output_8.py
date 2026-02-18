
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
        ValueError: If the file path is not within the safe directory
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    # Convert to absolute paths
    safe_dir = os.path.abspath(safe_directory)
    requested_path = os.path.abspath(os.path.join(safe_dir, filename))
    
    # Ensure the requested path is within the safe directory
    if not os.path.commonpath([requested_path, safe_dir]) == safe_dir:
        raise ValueError(f"Access to {filename} is not allowed")
    
    # Check if file exists
    if not os.path.exists(requested_path):
        raise FileNotFoundError(f"File {filename} not found in safe directory")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(requested_path):
        raise ValueError(f"{filename} is not a file")
    
    # Read and return file content
    try:
        with open(requested_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Fallback to binary read if UTF-8 fails
        with open(requested_path, 'rb') as file:
            return file.read()

# Alternative version using pathlib
def read_file_from_safe_directory_pathlib(filename, safe_directory):
    """
    Read a file from a safe directory using pathlib.
    
    Args:
        filename: Name of the file to read
        safe_directory: Path to the safe directory
    
    Returns:
        Content of the file as string
    
    Raises:
        ValueError: If the file path is not within the safe directory
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    safe_dir = pathlib.Path(safe_directory).resolve()
    requested_path = (safe_dir / filename).resolve()
    
    # Ensure the requested path is within the safe directory
    try:
        requested_path.relative_to(safe_dir)
    except ValueError:
        raise ValueError(f"Access to {filename} is not allowed")
    
    # Check if file exists and is a file
    if not requested_path.exists():
        raise FileNotFoundError(f"File {filename} not found in safe directory")
    
    if not requested_path.is_file():
        raise ValueError(f"{filename} is not a file")
    
    # Read and return file content
    try:
        return requested_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return requested_path.read_bytes()

# Example usage
if __name__ == "__main__":
    # Define your safe directory
    SAFE_DIR = "/path/to/safe/directory"
    
    # Example: Read a file
    try:
        content = read_file_from_safe_directory("example.txt", SAFE_DIR)
        print("File content:", content)
    except (ValueError, FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
