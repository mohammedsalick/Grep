import re

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()


            regex = re.compile(pattern)


            matching_lines = [line.strip() for line in lines if regex.search(line)]

            # Print matching lines
            for line in matching_lines:
                print(line)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pattern = input("Enter the pattern to search for: ")
    filename = input("Enter the filename to search in: ")

    grep(pattern, filename)
