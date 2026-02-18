
import os

# Using O_CREAT | O_WRONLY | O_TRUNC
fd = os.open("example.txt", os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
os.close(fd)

# Using O_CREAT | O_WRONLY | O_EXCL
try:
    fd = os.open("example_excl.txt", os.O_CREAT | os.O_WRONLY | os.O_EXCL)
    os.close(fd)
except FileExistsError:
    print("File already exists (O_EXCL flag worked)")
