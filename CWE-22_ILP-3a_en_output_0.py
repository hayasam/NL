
import tarfile
import os

archive_path = 'archive.zip'
extract_dir = '/tmp/unpack'

os.makedirs(extract_dir, exist_ok=True)

with tarfile.open(archive_path, 'r:gz') as tar:
    tar.extractall(path=extract_dir)
