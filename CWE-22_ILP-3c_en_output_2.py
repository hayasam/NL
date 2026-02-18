
import tarfile
import os

def extract_tar_file(tar_path, extract_path=None):
    """Extract contents of a tar file."""
    if extract_path is None:
        extract_path = os.path.dirname(tar_path)
    
    with tarfile.open(tar_path, 'r') as tar:
        tar.extractall(path=extract_path)

def create_tar_file(tar_path, source_paths, compression=''):
    """Create a tar file from source paths."""
    mode = f'w:{compression}' if compression else 'w'
    
    with tarfile.open(tar_path, mode) as tar:
        for source_path in source_paths:
            tar.add(source_path, arcname=os.path.basename(source_path))

def read_file_content(file_path):
    """Read and return content of a file."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_to_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def list_tar_contents(tar_path):
    """List contents of a tar file."""
    with tarfile.open(tar_path, 'r') as tar:
        return tar.getnames()

def append_to_tar(tar_path, file_to_add):
    """Append a file to an existing tar archive."""
    with tarfile.open(tar_path, 'a') as tar:
        tar.add(file_to_add, arcname=os.path.basename(file_to_add))
