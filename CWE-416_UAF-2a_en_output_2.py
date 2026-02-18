
import struct
import sys

def calculate_checksum(data):
    """Calculate simple byte sum checksum."""
    if not data:
        return 0
    return sum(data) & 0xFFFFFFFF

def main():
    if len(sys.argv) != 3:
        print("Usage: python checksum.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(input_file, 'rb') as f:
            buffer = f.read()
        
        bytes_read = len(buffer)
        checksum = calculate_checksum(buffer)
        
        with open(output_file, 'wb') as f:
            f.write(struct.pack('Q', bytes_read))
            f.write(struct.pack('I', checksum))
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
