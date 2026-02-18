
import tarfile
import os

def extract_tar_archive(archive_path, extract_to='.'):
    with tarfile.open(archive_path, 'r:*') as tar:
        tar.extractall(path=extract_to)

def create_tar_archive(source_paths, output_path, compression=''):
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(output_path, mode) as tar:
        for path in source_paths:
            tar.add(path)

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def list_tar_contents(archive_path):
    with tarfile.open(archive_path, 'r:*') as tar:
        return tar.getnames()
