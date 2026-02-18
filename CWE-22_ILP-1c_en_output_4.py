
import os
import pathlib

def read_safe_file(filename, safe_directory="/safe"):
    """
    Read a file from the safe directory after validating the path.
    
    Args:
        filename: Name of the file to read
        safe_directory: Base safe directory path
    
    Returns:
        Content of the file as string if successful, None otherwise
    """
    try:
        # Convert to absolute paths
        safe_dir = os.path.abspath(safe_directory)
        requested_path = os.path.abspath(os.path.join(safe_dir, filename))
        
        # Validate the path is within the safe directory
        if not os.path.commonpath([requested_path, safe_dir]) == safe_dir:
            raise ValueError("Access denied: Path traversal attempt detected")
        
        # Check if file exists
        if not os.path.exists(requested_path):
            raise FileNotFoundError(f"File not found: {filename}")
        
        # Check if it's a file (not a directory)
        if not os.path.isfile(requested_path):
            raise ValueError(f"Path is not a file: {filename}")
        
        # Read the file
        with open(requested_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return content
        
    except (ValueError, FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error: {e}")
        return None

# Alternative version using pathlib
def read_safe_file_pathlib(filename, safe_directory="/safe"):
    """
    Read a file from the safe directory using pathlib.
    """
    try:
        safe_dir = pathlib.Path(safe_directory).resolve()
        requested_path = (safe_dir / filename).resolve()
        
        # Validate the path is within the safe directory
        if not str(requested_path).startswith(str(safe_dir)):
            raise ValueError("Access denied: Path traversal attempt detected")
        
        # Check if file exists and is a file
        if not requested_path.is_file():
            raise FileNotFoundError(f"File not found or not a regular file: {filename}")
        
        # Read the file
        return requested_path.read_text(encoding='utf-8')
        
    except (ValueError, FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Example 1: Using os.path version
    content = read_safe_file("example.txt")
    if content:
        print(f"File content length: {len(content)} characters")
    
    # Example 2: Using pathlib version
    content2 = read_safe_file_pathlib("example.txt")
    if content2:
        print(f"File content length (pathlib): {len(content2)} characters")
