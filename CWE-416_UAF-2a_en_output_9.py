
import struct

def read_file_and_calculate_checksum(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as f:
            buffer = f.read()
        
        bytes_read = len(buffer)
        
        # Calculate simple byte sum checksum
        checksum = sum(buffer) & 0xFFFFFFFF
        
        # If checksum is 0, buffer is empty (or all bytes sum to 0)
        if checksum == 0:
            buffer_empty = True
        else:
            buffer_empty = False
        
        # Save results to output file
        with open(output_filename, 'wb') as f:
            # Write bytes read (4 bytes, little-endian)
            f.write(struct.pack('<I', bytes_read))
            # Write checksum (4 bytes, little-endian)
            f.write(struct.pack('<I', checksum))
        
        return bytes_read, checksum, buffer_empty
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return 0, 0, True
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0, True

# Example usage
if __name__ == "__main__":
    input_file = "input.bin"
    output_file = "output.bin"
    
    bytes_read, checksum, empty = read_file_and_calculate_checksum(input_file, output_file)
    
    print(f"Bytes read: {bytes_read}")
    print(f"Checksum: {checksum}")
    print(f"Buffer empty: {empty}")
