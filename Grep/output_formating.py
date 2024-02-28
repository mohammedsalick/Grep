import re

def grep(pattern, file_path, show_line_numbers=True, show_count=False):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    matching_lines = [i + 1 for i, line in enumerate(lines) if re.search(pattern, line)]

    if show_count:
        print(f"Number of matching lines: {len(matching_lines)}")
    else:
        for line_number in matching_lines:
            line = lines[line_number - 1].strip()
            if show_line_numbers:
                print(f"{line_number}: {line}")
            else:
                print(line)

# Example usage:
pattern_to_search = "example"
file_to_search = "D:\\Users\\pythonProject\\Grep\\file.txt"

# Display matching lines with line numbers
grep(pattern_to_search, file_to_search, show_line_numbers=True, show_count=False)

# Display only the count of matching lines
grep(pattern_to_search, file_to_search, show_line_numbers=False, show_count=True)
