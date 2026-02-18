
import os

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    if not os.path.exists(safe_dir):
        raise FileNotFoundError(f"Directory {safe_dir} does not exist")
    
    full_path = os.path.join(safe_dir, filename)
    
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File {filename} not found in {safe_dir}")
    
    if not os.path.isfile(full_path):
        raise ValueError(f"{filename} is not a file")
    
    with open(full_path, 'r') as file:
        content = file.read()
    
    return content

if __name__ == "__main__":
    try:
        filename = input("Enter filename to read from /safe/ directory: ").strip()
        content = read_safe_file(filename)
        print(content)
    except Exception as e:
        print(f"Error: {e}")
