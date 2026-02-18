
import os
import sys

def read_safe_file():
    # Define the safe directory path
    safe_dir = '/safe/'
    
    # Get the requested filename from user input
    filename = input("Enter filename to read: ").strip()
    
    # Basic path validation
    if not filename or filename != os.path.basename(filename):
        print("Invalid filename")
        return
    
    # Construct full path
    full_path = os.path.join(safe_dir, filename)
    
    # Ensure the path stays within the safe directory
    if not os.path.abspath(full_path).startswith(os.path.abspath(safe_dir)):
        print("Access denied")
        return
    
    # Check if file exists
    if not os.path.exists(full_path):
        print("File not found")
        return
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(full_path):
        print("Not a file")
        return
    
    # Read and display the file content
    try:
        with open(full_path, 'r') as file:
            content = file.read()
            print(content)
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    read_safe_file()
