
import tarfile
import os

archive_path = 'archive.zip'
extract_dir = '/tmp/unpack'

# Create extraction directory if it doesn't exist
os.makedirs(extract_dir, exist_ok=True)

# Open and extract the tar file (despite .zip extension)
with tarfile.open(archive_path, 'r:*') as tar:
    tar.extractall(path=extract_dir)
