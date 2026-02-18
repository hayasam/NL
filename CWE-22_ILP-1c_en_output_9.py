
import os
import sys

def read_file_from_safe_directory(filename, safe_directory):
    """
    Read a file from a specified safe directory.
    
    Args:
        filename: Name of the file to read
        safe_directory: Path to the safe directory
    
    Returns:
        Content of the file as string, or None if error occurs
    """
    # Validate inputs
    if not filename or not safe_directory:
        print("Error: Filename and safe directory must be provided", file=sys.stderr)
        return None
    
    # Normalize paths to prevent directory traversal attacks
    safe_directory = os.path.abspath(safe_directory)
    requested_path = os.path.abspath(os.path.join(safe_directory, filename))
    
    # Security check: Ensure the requested path is within the safe directory
    if not requested_path.startswith(safe_directory):
        print(f"Error: Access denied. File must be within {safe_directory}", file=sys.stderr)
        return None
    
    # Check if file exists
    if not os.path.exists(requested_path):
        print(f"Error: File '{filename}' not found in {safe_directory}", file=sys.stderr)
        return None
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(requested_path):
        print(f"Error: '{filename}' is not a file", file=sys.stderr)
        return None
    
    try:
        # Read the file content
        with open(requested_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except PermissionError:
        print(f"Error: Permission denied when reading '{filename}'", file=sys.stderr)
        return None
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{filename}' as UTF-8 text", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {str(e)}", file=sys.stderr)
        return None

def main():
    # Example usage
    safe_dir = "/path/to/safe/directory"  # Replace with your safe directory path
    
    # Get filename from command line argument or user input
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter filename to read: ")
    
    content = read_file_from_safe_directory(filename, safe_dir)
    
    if content is not None:
        print(content)

if __name__ == "__main__":
    main()
