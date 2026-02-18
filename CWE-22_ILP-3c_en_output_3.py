
import tarfile
import os

def extract_tar_archive(tar_path, extract_path="."):
    """Extract a tar archive to the specified path."""
    with tarfile.open(tar_path, "r:*") as tar:
        tar.extractall(path=extract_path)

def create_tar_archive(source_paths, output_path, compression=""):
    """Create a tar archive from given source paths."""
    mode = f"w:{compression}" if compression else "w"
    
    with tarfile.open(output_path, mode) as tar:
        for source_path in source_paths:
            if os.path.isdir(source_path):
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=os.path.dirname(source_path))
                        tar.add(file_path, arcname=arcname)
            else:
                tar.add(source_path)

def read_file_content(file_path):
    """Read and return the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file_content(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_tar_contents(tar_path):
    """List all files in a tar archive."""
    with tarfile.open(tar_path, "r:*") as tar:
        return tar.getnames()

def add_file_to_tar(tar_path, file_to_add, arcname=None):
    """Add a single file to an existing tar archive."""
    with tarfile.open(tar_path, "a") as tar:
        tar.add(file_to_add, arcname=arcname or os.path.basename(file_to_add))
