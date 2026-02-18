
import os
import pathlib

def read_safe_file(filename):
    safe_dir = pathlib.Path('/safe/')
    
    if not safe_dir.is_dir():
        raise ValueError("Safe directory does not exist")
    
    file_path = safe_dir / filename
    
    # Security check: ensure the file is within the safe directory
    try:
        file_path.resolve().relative_to(safe_dir.resolve())
    except ValueError:
        raise ValueError("File path is outside the safe directory")
    
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {filename}")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    try:
        content = read_safe_file(sys.argv[1])
        print(content)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
