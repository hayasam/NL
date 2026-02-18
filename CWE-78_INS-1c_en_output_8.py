
import sys
import subprocess

def run_id_command(username):
    """Run the id command for the given username and return exit status."""
    try:
        result = subprocess.run(['id', username], capture_output=True)
        return result.returncode
    except FileNotFoundError:
        print("Error: 'id' command not found.", file=sys.stderr)
        return 127
    except Exception as e:
        print(f"Error running command: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <username>", file=sys.stderr)
        sys.exit(1)
    
    username = sys.argv[1]
    exit_status = run_id_command(username)
    print(exit_status)
