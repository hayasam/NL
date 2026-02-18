
import sys
import os

def calculate_checksum(data):
    """Calculate simple byte checksum"""
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
        # Read file contents
        with open(input_file, 'rb') as f:
            buffer = f.read()
        
        # Calculate checksum
        checksum = calculate_checksum(buffer)
        
        # Determine if buffer is empty based on checksum
        is_empty = (checksum == 0)
        
        # Get number of bytes read
        bytes_read = len(buffer)
        
        # Save results to output file
        with open(output_file, 'w') as f:
            f.write(f"Bytes read: {bytes_read}\n")
            f.write(f"Checksum: {checksum}\n")
            f.write(f"Buffer empty: {is_empty}\n")
        
        print(f"Processed {input_file}: {bytes_read} bytes, checksum: {checksum}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    except IOError as e:
        print(f"Error processing files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
