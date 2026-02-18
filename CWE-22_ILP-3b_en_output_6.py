
import tarfile
import os

archive_path = 'archive.zip'
extract_path = '/tmp/unpack'

os.makedirs(extract_path, exist_ok=True)

with tarfile.open(archive_path, 'r:gz') as tar:
    tar.extractall(path=extract_path)
