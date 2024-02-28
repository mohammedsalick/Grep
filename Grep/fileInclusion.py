import os
import re

def grep(pattern, path, include=None, exclude=None):
    result = []

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # Check inclusion
            if include and not any(fnmatch(file, include) for fnmatch in include):
                continue

            # Check exclusion
            if exclude and any(fnmatch(file, exclude) for fnmatch in exclude):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if re.search(pattern, line):
                            result.append((file_path, i + 1, line.strip()))
            except (UnicodeDecodeError, PermissionError):
                # Handle potential decoding or permission errors
                pass

    return result

# Example Usage:
pattern_to_search = r'your_pattern'
path_to_search = '/path/to/search'
include_files = ['*.txt', '*.py']
exclude_files = ['*.log']

result = grep(pattern_to_search, path_to_search, include=include_files, exclude=exclude_files)

for match in result:
    print(f"File: {match[0]}, Line: {match[1]}, Content: {match[2]}")
