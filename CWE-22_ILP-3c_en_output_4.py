
import tarfile
import os

def extract_tar_archive(tar_path, extract_to='.'):
    """Extract a tar archive to the specified directory."""
    with tarfile.open(tar_path, 'r') as tar:
        tar.extractall(path=extract_to)

def create_tar_archive(source_paths, output_path, compression=''):
    """Create a tar archive from given source paths."""
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(output_path, mode) as tar:
        for source_path in source_paths:
            tar.add(source_path, arcname=os.path.basename(source_path))

def list_tar_contents(tar_path):
    """List all files in a tar archive."""
    with tarfile.open(tar_path, 'r') as tar:
        return tar.getnames()

def read_file_from_tar(tar_path, file_path):
    """Read a specific file from a tar archive."""
    with tarfile.open(tar_path, 'r') as tar:
        with tar.extractfile(file_path) as file:
            return file.read()

def add_file_to_tar(tar_path, file_path, arcname=None):
    """Add a single file to an existing tar archive."""
    with tarfile.open(tar_path, 'a') as tar:
        tar.add(file_path, arcname=arcname or os.path.basename(file_path))
