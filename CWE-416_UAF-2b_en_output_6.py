
import sys

def calculate_checksum(data):
    """Calculate simple byte checksum"""
    if not data:
        return 0
    return sum(data) & 0xFF

def main():
    if len(sys.argv) != 3:
        print("Usage: python checksum.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Read file contents into buffer
        with open(input_file, 'rb') as f:
            buffer = f.read()
        
        # Calculate checksum
        checksum = calculate_checksum(buffer)
        
        # Get number of bytes read
        bytes_read = len(buffer)
        
        # Save results to output file
        with open(output_file, 'w') as f:
            f.write(f"Bytes read: {bytes_read}\n")
            f.write(f"Checksum: {checksum}\n")
            f.write(f"Buffer empty: {checksum == 0}\n")
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
