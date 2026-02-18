
import sys

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "."
    
    import subprocess
    subprocess.run(["ls", directory])

if __name__ == "__main__":
    main()
