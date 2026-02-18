
import struct

def read_file_and_calculate_checksum(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as f:
            buffer = f.read()
        
        bytes_read = len(buffer)
        
        if bytes_read == 0:
            checksum = 0
        else:
            checksum = 0
            for byte in buffer:
                checksum = (checksum + byte) & 0xFFFFFFFF
        
        with open(output_filename, 'wb') as f:
            f.write(struct.pack('I', bytes_read))
            f.write(struct.pack('I', checksum))
        
        return bytes_read, checksum
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

if __name__ == "__main__":
    input_file = "input.bin"
    output_file = "output.bin"
    read_file_and_calculate_checksum(input_file, output_file)
