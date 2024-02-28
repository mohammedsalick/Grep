import re
import argparse

def grep(pattern, files, ignore_case=False):
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags=flags)

    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if regex.search(line):
                        print(f"{file_path}:{line_number}:{line.strip()}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except PermissionError:
            print(f"Permission denied: {file_path}")
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='A simplified grep command in Python.')
    parser.add_argument('pattern', help='Pattern to search')
    parser.add_argument('files', nargs='+', help='Files to search in')
    parser.add_argument('-i', '--ignore-case', action='store_true', help='Case-insensitive search')

    args = parser.parse_args()
    grep(args.pattern, args.files, args.ignore_case)

if __name__ == "__main__":
    main()
