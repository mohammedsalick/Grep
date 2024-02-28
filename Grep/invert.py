import re
import sys

def invert_match(pattern, filename):
    with open(filename, 'r') as file:
        for line in file:
            if not re.search(pattern, line):
                print(line, end='')

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <pattern> <filename>")
        sys.exit(1)

    pattern = sys.argv[1]
    filename = sys.argv[2]

    # Call the invert_match function
    invert_match(pattern, filename)
