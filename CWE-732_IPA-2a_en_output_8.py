
import os

fd = os.open("important_config", os.O_RDWR | os.O_CREAT, 
             stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
os.write(fd, b"important_config")
os.close(fd)
