
import os

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    if not os.path.isabs(filename):
        filepath = os.path.join(safe_dir, filename)
    else:
        filepath = filename
    
    normalized_path = os.path.normpath(filepath)
    
    if not normalized_path.startswith(os.path.normpath(safe_dir)):
        raise ValueError("Access denied: File must be within /safe/ directory")
    
    try:
        with open(normalized_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {normalized_path}")
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
