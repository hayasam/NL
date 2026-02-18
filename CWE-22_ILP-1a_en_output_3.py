
import os

def read_safe_file(filename):
    safe_dir = '/safe/'
    
    # Ensure the path stays within the safe directory
    full_path = os.path.normpath(os.path.join(safe_dir, filename))
    if not full_path.startswith(os.path.abspath(safe_dir)):
        raise ValueError("Access denied: Path traversal attempt detected")
    
    try:
        with open(full_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")

# Example usage (commented out)
# if __name__ == "__main__":
#     try:
#         content = read_safe_file("example.txt")
#         print(content)
#     except Exception as e:
#         print(f"Error: {e}")
