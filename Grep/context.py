import re

def grep(file_path, pattern, before=0, after=0):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    pattern_re = re.compile(pattern)

    result = []
    for i, line in enumerate(lines):
        if pattern_re.search(line):
            start = max(0, i - before)
            end = min(len(lines), i + after + 1)
            result.extend(lines[start:end])

    return result

# Example usage:
file_path = 'file.txt'
pattern_to_search = 'example'
num_lines_before = 2
num_lines_after = 2

result_lines = grep(file_path, pattern_to_search, num_lines_before, num_lines_after)

for line in result_lines:
    print(line.strip())
