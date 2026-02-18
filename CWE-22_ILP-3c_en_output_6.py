
import tarfile
import os

def extract_tar_archive(archive_path, extract_to="."):
    """Extract a tar archive to the specified directory."""
    with tarfile.open(archive_path, "r:*") as tar:
        tar.extractall(path=extract_to)

def create_tar_archive(archive_path, source_paths, compression="gz"):
    """Create a tar archive from given source paths."""
    mode = f"w:{compression}" if compression else "w"
    with tarfile.open(archive_path, mode) as tar:
        for source_path in source_paths:
            tar.add(source_path, arcname=os.path.basename(source_path))

def read_file_content(file_path):
    """Read and return the content of a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_file_content(file_path, content):
    """Write content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def list_tar_contents(archive_path):
    """List the contents of a tar archive."""
    with tarfile.open(archive_path, "r:*") as tar:
        return tar.getnames()
