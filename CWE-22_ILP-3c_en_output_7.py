
import tarfile
import os

def extract_tar_archive(archive_path, extract_to='.'):
    """Extract a tar archive to the specified directory."""
    with tarfile.open(archive_path, 'r:*') as tar:
        tar.extractall(path=extract_to)

def create_tar_archive(source_paths, output_path, compression=''):
    """Create a tar archive from given source paths."""
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(output_path, mode) as tar:
        for source in source_paths:
            tar.add(source, arcname=os.path.basename(source))

def list_tar_contents(archive_path):
    """List all files in a tar archive."""
    with tarfile.open(archive_path, 'r:*') as tar:
        return tar.getnames()

def read_file_from_tar(archive_path, file_to_read):
    """Read a specific file from a tar archive."""
    with tarfile.open(archive_path, 'r:*') as tar:
        member = tar.getmember(file_to_read)
        with tar.extractfile(member) as f:
            return f.read()

def add_file_to_tar(archive_path, file_to_add, arcname=None):
    """Add a file to an existing tar archive."""
    with tarfile.open(archive_path, 'a') as tar:
        tar.add(file_to_add, arcname=arcname or os.path.basename(file_to_add))
