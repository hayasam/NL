
import os

fd = os.open("important_config", os.O_RDWR | os.O_CREAT, 
             os.S_IRUSR | os.S_IWUSR | os.S_IRGRP | os.S_IROTH)
os.write(fd, b"important_config")
os.close(fd)
