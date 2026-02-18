
import tarfile
import os

def extract_tar_archive(tar_path, extract_to="."):
    """Extract a tar archive to the specified directory."""
    with tarfile.open(tar_path, 'r:*') as tar:
        tar.extractall(path=extract_to)

def create_tar_archive(source_paths, output_path, compression=''):
    """Create a tar archive from given source paths."""
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(output_path, mode) as tar:
        for source in source_paths:
            tar.add(source, arcname=os.path.basename(source))

def read_file_content(file_path):
    """Read and return the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_tar_contents(tar_path):
    """List all files in a tar archive."""
    with tarfile.open(tar_path, 'r:*') as tar:
        return tar.getnames()

def add_file_to_tar(tar_path, file_to_add, arcname=None):
    """Add a single file to an existing tar archive."""
    with tarfile.open(tar_path, 'a') as tar:
        tar.add(file_to_add, arcname=arcname or os.path.basename(file_to_add))
