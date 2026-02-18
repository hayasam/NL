
import os
import pathlib

def read_safe_file(filename):
    # Define the safe directory
    safe_dir = pathlib.Path('/safe/').resolve()
    
    # Validate filename doesn't contain path traversal
    if '..' in filename or filename.startswith('/'):
        raise ValueError("Invalid filename")
    
    # Create the full path
    file_path = safe_dir / filename
    
    # Ensure the file is within the safe directory
    try:
        file_path.resolve().relative_to(safe_dir)
    except ValueError:
        raise ValueError("File path is outside safe directory")
    
    # Check if file exists
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {filename}")
    
    # Read and return file content
    with open(file_path, 'r') as file:
        return file.read()

# Example usage
if __name__ == "__main__":
    try:
        filename = input("Enter filename to read from /safe/: ")
        content = read_safe_file(filename)
        print(content)
    except Exception as e:
        print(f"Error: {e}")
