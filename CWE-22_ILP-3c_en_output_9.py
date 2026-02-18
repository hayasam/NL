
import tarfile
import os

def extract_tar_file(tar_path, extract_to='.'):
    with tarfile.open(tar_path, 'r:*') as tar:
        tar.extractall(path=extract_to)

def create_tar_file(tar_path, files_to_archive, compression=''):
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(tar_path, mode) as tar:
        for file_path in files_to_archive:
            tar.add(file_path, arcname=os.path.basename(file_path))

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
