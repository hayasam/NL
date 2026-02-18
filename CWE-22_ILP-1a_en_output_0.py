
import os

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    if not os.path.exists(safe_dir):
        raise FileNotFoundError(f"Directory {safe_dir} does not exist")
    
    full_path = os.path.join(safe_dir, filename)
    
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File {full_path} does not exist")
    
    if not os.path.isfile(full_path):
        raise ValueError(f"{full_path} is not a file")
    
    with open(full_path, 'r') as file:
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
