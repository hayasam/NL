
import os

# Create file if it doesn't exist, truncate if it does
fd = os.open("example.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

# Create file only if it doesn't exist (fails if file exists)
try:
    fd_excl = os.open("example_excl.txt", os.O_WRONLY | os.O_CREAT | os.O_EXCL)
except FileExistsError:
    print("File already exists")

# Write to file
os.write(fd, b"Hello, World!\n")

# Close file descriptors
os.close(fd)
if 'fd_excl' in locals():
    os.close(fd_excl)
