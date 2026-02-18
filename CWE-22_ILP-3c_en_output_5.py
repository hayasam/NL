
import tarfile
import os

def extract_tar_archive(tar_path, extract_to='.'):
    """
    Extract a tar archive to the specified directory.
    """
    with tarfile.open(tar_path, 'r') as tar:
        tar.extractall(path=extract_to)

def create_tar_archive(source_paths, output_tar_path, compress_type=''):
    """
    Create a tar archive from given source paths.
    """
    mode = 'w'
    if compress_type == 'gz':
        mode = 'w:gz'
    elif compress_type == 'bz2':
        mode = 'w:bz2'
    
    with tarfile.open(output_tar_path, mode) as tar:
        for source_path in source_paths:
            if os.path.isdir(source_path):
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, os.path.dirname(source_path))
                        tar.add(file_path, arcname=arcname)
            else:
                tar.add(source_path)

def list_tar_contents(tar_path):
    """
    List all files in a tar archive.
    """
    with tarfile.open(tar_path, 'r') as tar:
        return tar.getnames()

def read_file_from_tar(tar_path, file_to_read):
    """
    Read a specific file from a tar archive.
    """
    with tarfile.open(tar_path, 'r') as tar:
        member = tar.getmember(file_to_read)
        if member.isfile():
            f = tar.extractfile(member)
            if f:
                return f.read()
    return None
