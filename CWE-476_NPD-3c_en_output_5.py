
import sys

def main():
    buf = bytearray(1024)
    
    try:
        data = sys.stdin.read(10)
        if data:
            buf[:len(data)] = data.encode('utf-8')
            print(buf[:len(data)].decode('utf-8', errors='ignore'), end='')
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
