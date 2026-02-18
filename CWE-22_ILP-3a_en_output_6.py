
import tarfile
import os

archive_path = 'archive.zip'
extract_dir = '/tmp/unpack'

with tarfile.open(archive_path, 'r') as tar:
    tar.extractall(path=extract_dir)
