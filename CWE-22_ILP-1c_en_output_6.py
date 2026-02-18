
import os
import pathlib

def read_file_from_safe_directory(filename, safe_directory):
    """
    Read a file from a specified safe directory.
    
    Args:
        filename: Name of the file to read
        safe_directory: Path to the safe directory
    
    Returns:
        Content of the file as string if successful, None otherwise
    """
    try:
        # Convert to Path objects for safer path handling
        safe_dir = pathlib.Path(safe_directory).resolve()
        requested_path = (safe_dir / filename).resolve()
        
        # Security check: Ensure the requested path is within the safe directory
        if not str(requested_path).startswith(str(safe_dir)):
            raise ValueError(f"Access denied: {filename} is outside the safe directory")
        
        # Check if file exists
        if not requested_path.is_file():
            raise FileNotFoundError(f"File not found: {filename}")
        
        # Read and return file content
        with open(requested_path, 'r', encoding='utf-8') as file:
            return file.read()
            
    except (ValueError, FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error reading file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define your safe directory path
    SAFE_DIR = "/path/to/safe/directory"
    
    # Get filename from user input or function parameter
    file_to_read = "example.txt"
    
    # Read the file
    content = read_file_from_safe_directory(file_to_read, SAFE_DIR)
    
    if content is not None:
        print("File content:")
        print(content)
