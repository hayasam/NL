
import os

def create_important_config():
    filename = "important_config"
    flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY
    mode = os.S_IRUSR | os.S_IWUSR
    
    try:
        fd = os.open(filename, flags, mode)
        with os.fdopen(fd, 'w') as f:
            # File is open for writing, add content if needed
            pass
    except OSError as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    create_important_config()
