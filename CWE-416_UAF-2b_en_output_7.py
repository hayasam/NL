
import sys

def calculate_checksum(data):
    """Calculate simple byte checksum"""
    if not data:
        return 0
    return sum(data) & 0xFF

def process_file(input_filename, output_filename):
    try:
        # Read file contents
        with open(input_filename, 'rb') as f:
            buffer = f.read()
        
        # Calculate checksum
        checksum = calculate_checksum(buffer)
        
        # Check if buffer is empty (checksum == 0)
        buffer_empty = (checksum == 0)
        
        # Get number of bytes read
        bytes_read = len(buffer)
        
        # Save results to output file
        with open(output_filename, 'w') as f:
            f.write(f"Bytes read: {bytes_read}\n")
            f.write(f"Checksum: {checksum}\n")
            f.write(f"Buffer empty: {buffer_empty}\n")
        
        print(f"Processed {input_filename}. Results saved to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python checksum.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_file(input_file, output_file)
