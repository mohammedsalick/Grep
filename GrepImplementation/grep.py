import os
import re
import argparse
from colorama import Fore, Style

def grep(pattern, files, options):
    matched_lines = []
    line_numbers = []

    pattern_flags = re.IGNORECASE if not options.case_sensitive else 0
    pattern_regex = re.compile(pattern, flags=pattern_flags) if options.regex else re.compile(re.escape(pattern))

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, start=1):
                    if options.whole_word:
                        line = f' {line} '

                    if pattern_regex.search(line) and (options.case_sensitive or pattern.lower() in line.lower()):
                        matched_lines.append(line)
                        line_numbers.append(line_number)

        except (OSError, UnicodeDecodeError) as e:
            print(f"Error reading file {file}: {e}")

    for i, line in enumerate(matched_lines):
        if options.invert_match:
            line = Fore.GREEN + line + Style.RESET_ALL
        elif options.colorize:
            line = re.sub(pattern_regex, Fore.RED + r'\g<0>' + Style.RESET_ALL, line)

        print(f"{Fore.CYAN}{line_numbers[i]}:{Style.RESET_ALL} {line}", end='')

def main():
    parser = argparse.ArgumentParser(description='A simplified version of the grep command.')
    parser.add_argument('pattern', help='The pattern to search for')
    parser.add_argument('files', nargs='+', help='Files to search in')
    parser.add_argument('-r', '--recursive', action='store_true', help='Search recursively through directories')
    parser.add_argument('-i', '--ignore-case', dest='case_sensitive', action='store_false', help='Case-insensitive search')
    parser.add_argument('-n', '--line-number', action='store_true', help='Display line numbers')
    parser.add_argument('-c', '--count', action='store_true', help='Display only the count of matching lines')
    parser.add_argument('-w', '--word', dest='whole_word', action='store_true', help='Search only whole words')
    parser.add_argument('-v', '--invert-match', action='store_true', help='Invert the match, display non-matching lines')
    parser.add_argument('--color', dest='colorize', action='store_true', default=False, help='Colorize matching text for improved visibility')
    parser.add_argument('--regex', action='store_true', help='Interpret the pattern as a regular expression')
    args = parser.parse_args()

    if args.recursive:
        files = [os.path.join(dirpath, filename)
                 for dirpath, _, filenames in os.walk(args.files)
                 for filename in filenames]
    else:
        files = args.files

    grep(args.pattern, files, args)

if __name__ == "__main__":
    main()
