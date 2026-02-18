
import os
import pathlib

def read_file_from_safe_directory(filename, safe_base_dir):
    """
    Read a file from a safe directory after validating the path.
    
    Args:
        filename: Name of the file to read
        safe_base_dir: Base directory considered safe for file operations
    
    Returns:
        Content of the file as string if successful, None otherwise
    """
    try:
        # Convert to absolute paths
        safe_base_path = pathlib.Path(safe_base_dir).resolve()
        requested_path = (safe_base_path / filename).resolve()
        
        # Security check: Ensure the requested path is within the safe directory
        if not str(requested_path).startswith(str(safe_base_path)):
            print(f"Error: Attempted to access file outside safe directory: {filename}")
            return None
        
        # Check if file exists
        if not requested_path.is_file():
            print(f"Error: File not found: {filename}")
            return None
        
        # Read and return file content
        with open(requested_path, 'r', encoding='utf-8') as file:
            return file.read()
            
    except (OSError, IOError) as e:
        print(f"Error reading file {filename}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define your safe directory (adjust this path as needed)
    SAFE_DIRECTORY = "/path/to/safe/directory"
    
    # Example: Read a file named "example.txt" from the safe directory
    content = read_file_from_safe_directory("example.txt", SAFE_DIRECTORY)
    
    if content is not None:
        print("File content:")
        print(content)
