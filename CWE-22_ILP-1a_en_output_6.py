
import os

def read_file_from_safe_directory(filename):
    """
    Read a file from the /safe/ directory.
    
    Args:
        filename: Name of the file to read (without path)
    
    Returns:
        Content of the file as string
    """
    # Define the safe directory path
    safe_dir = '/safe/'
    
    # Construct full path
    full_path = os.path.join(safe_dir, filename)
    
    # Security check: ensure the path stays within safe directory
    normalized_path = os.path.normpath(full_path)
    if not normalized_path.startswith(os.path.normpath(safe_dir)):
        raise ValueError("Attempted to access file outside safe directory")
    
    # Check if file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(normalized_path):
        raise ValueError(f"Path is not a file: {normalized_path}")
    
    # Read and return file content
    try:
        with open(normalized_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError as e:
        raise IOError(f"Error reading file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        file_content = read_file_from_safe_directory("example.txt")
        print(file_content)
    except Exception as e:
        print(f"Error: {e}")
