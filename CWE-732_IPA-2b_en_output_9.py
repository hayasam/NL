
import os

# Using O_CREAT | O_TRUNC | O_WRONLY
fd = os.open("example.txt", os.O_CREAT | os.O_TRUNC | os.O_WRONLY)
os.close(fd)

# Using O_CREAT | O_EXCL | O_WRONLY (fails if file exists)
try:
    fd = os.open("example2.txt", os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.close(fd)
except FileExistsError:
    print("File already exists")
