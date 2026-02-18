
import tarfile
import os

with tarfile.open('archive.zip', 'r') as tar:
    tar.extractall('/tmp/unpack')
