
import os
import sys

def read_file_from_safe_directory(filename, safe_directory):
    """
    Read a file from a safe directory after validating the path.
    
    Args:
        filename: Name of the file to read
        safe_directory: Path to the safe directory
    
    Returns:
        Content of the file as string if successful, None otherwise
    """
    # Normalize paths to prevent directory traversal
    safe_directory = os.path.abspath(safe_directory)
    requested_path = os.path.abspath(os.path.join(safe_directory, filename))
    
    # Security check: Ensure the requested path is within the safe directory
    if not requested_path.startswith(safe_directory):
        print(f"Error: Attempted to access file outside safe directory: {filename}")
        return None
    
    # Check if file exists
    if not os.path.exists(requested_path):
        print(f"Error: File not found: {filename}")
        return None
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(requested_path):
        print(f"Error: Path is not a file: {filename}")
        return None
    
    try:
        with open(requested_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except PermissionError:
        print(f"Error: Permission denied when reading: {filename}")
        return None
    except UnicodeDecodeError:
        print(f"Error: Could not decode file as UTF-8: {filename}")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {str(e)}")
        return None

def main():
    # Example usage
    if len(sys.argv) != 3:
        print("Usage: python script.py <safe_directory> <filename>")
        sys.exit(1)
    
    safe_directory = sys.argv[1]
    filename = sys.argv[2]
    
    # Validate safe directory exists
    if not os.path.isdir(safe_directory):
        print(f"Error: Safe directory does not exist: {safe_directory}")
        sys.exit(1)
    
    content = read_file_from_safe_directory(filename, safe_directory)
    
    if content is not None:
        print(content)

if __name__ == "__main__":
    main()
