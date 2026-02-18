
import struct

def calculate_checksum(data):
    """Calculate simple byte sum checksum"""
    if not data:
        return 0
    return sum(data) & 0xFFFFFFFF

def process_file(input_filename, output_filename):
    try:
        # Read file contents into buffer
        with open(input_filename, 'rb') as f:
            buffer = f.read()
        
        # Calculate checksum
        checksum = calculate_checksum(buffer)
        
        # Check if buffer is empty (checksum == 0)
        is_empty = (checksum == 0)
        
        # Get number of bytes read
        bytes_read = len(buffer)
        
        # Save results to output file
        with open(output_filename, 'wb') as f:
            # Write bytes read (as 4-byte unsigned integer)
            f.write(struct.pack('I', bytes_read))
            # Write checksum (as 4-byte unsigned integer)
            f.write(struct.pack('I', checksum))
        
        return bytes_read, checksum, is_empty
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return 0, 0, True
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0, 0, True

# Example usage
if __name__ == "__main__":
    input_file = "input.bin"
    output_file = "output.bin"
    
    bytes_read, checksum, is_empty = process_file(input_file, output_file)
    
    print(f"Bytes read: {bytes_read}")
    print(f"Checksum: {checksum}")
    print(f"Buffer empty: {is_empty}")
