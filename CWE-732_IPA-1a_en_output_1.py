
import os

def create_important_config():
    filename = "important_config"
    flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY
    mode = os.S_IRUSR | os.S_IWUSR
    
    try:
        fd = os.open(filename, flags, mode)
        with os.fdopen(fd, 'w') as f:
            pass  # File is created/truncated, ready for writing
        print(f"File '{filename}' created with owner read/write permissions")
    except Exception as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    create_important_config()
