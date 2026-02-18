
import os

def create_file_exclusive(filename):
    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.close(fd)
        return True
    except FileExistsError:
        return False

def create_or_truncate_file(filename):
    fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY)
    os.close(fd)
    return True
