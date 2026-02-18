
import struct

def read_file_and_calculate_checksum(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as f:
            buffer = f.read()
        
        bytes_read = len(buffer)
        
        # Calculate simple byte sum checksum
        checksum = 0
        for byte in buffer:
            checksum = (checksum + byte) & 0xFFFFFFFF
        
        # If checksum is 0, buffer is empty (or all bytes sum to 0 mod 2^32)
        if checksum == 0:
            buffer_empty = True
        else:
            buffer_empty = False
        
        # Save results to output file
        with open(output_filename, 'wb') as f:
            # Write bytes read (8 bytes) and checksum (4 bytes)
            f.write(struct.pack('QI', bytes_read, checksum))
        
        return bytes_read, checksum, buffer_empty
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return None, None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

# Example usage
if __name__ == "__main__":
    input_file = "input.bin"
    output_file = "output.bin"
    
    result = read_file_and_calculate_checksum(input_file, output_file)
    if result[0] is not None:
        print(f"Bytes read: {result[0]}, Checksum: {result[1]:08x}, Buffer empty: {result[2]}")
