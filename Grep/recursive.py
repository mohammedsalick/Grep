import os
import re

def recursive_grep(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if re.search(pattern, line):
                            print(f'{file_path}:{line_number}: {line.strip()}')
            except (OSError, UnicodeDecodeError):
                # Handle exceptions such as permission errors or decoding issues
                pass

# Example usage:
directory_to_search = 'file.txt'
search_pattern = r'example'

recursive_grep(directory_to_search, search_pattern)
