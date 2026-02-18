
import os

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    if not os.path.isabs(filename):
        filepath = os.path.join(safe_dir, filename)
    else:
        filepath = filename
    
    normalized_path = os.path.normpath(filepath)
    
    if not normalized_path.startswith(os.path.normpath(safe_dir)):
        raise ValueError("File must be within the /safe/ directory")
    
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    if not os.path.isfile(normalized_path):
        raise ValueError(f"Path is not a file: {normalized_path}")
    
    try:
        with open(normalized_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError as e:
        raise IOError(f"Error reading file: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            content = read_safe_file(sys.argv[1])
            print(content)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: python script.py <filename>")
