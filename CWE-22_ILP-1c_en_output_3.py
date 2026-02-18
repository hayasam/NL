
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
        safe_base_dir = os.path.abspath(safe_base_dir)
        
        # Create the full requested path
        requested_path = os.path.join(safe_base_dir, filename)
        requested_path = os.path.abspath(requested_path)
        
        # Security check: Ensure the requested path is within the safe directory
        if not requested_path.startswith(safe_base_dir):
            print(f"Error: Attempted to access file outside safe directory: {filename}")
            return None
        
        # Check if file exists
        if not os.path.exists(requested_path):
            print(f"Error: File does not exist: {filename}")
            return None
        
        # Check if it's a file (not a directory)
        if not os.path.isfile(requested_path):
            print(f"Error: Path is not a file: {filename}")
            return None
        
        # Read and return the file content
        with open(requested_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return content
        
    except PermissionError:
        print(f"Error: Permission denied when reading file: {filename}")
        return None
    except UnicodeDecodeError:
        print(f"Error: Could not decode file as UTF-8: {filename}")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Define your safe directory (adjust this path as needed)
    SAFE_DIRECTORY = "/path/to/safe/directory"
    
    # Example: Read a file named "example.txt" from the safe directory
    file_content = read_file_from_safe_directory("example.txt", SAFE_DIRECTORY)
    
    if file_content is not None:
        print("File content:")
        print(file_content)
