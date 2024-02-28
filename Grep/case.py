import re


def grep(pattern, text, case_sensitive=True):
    flags = 0 if case_sensitive else re.IGNORECASE
    regex = re.compile(pattern, flags)

    matches = [line for line in text.split('\n') if regex.search(line)]
    return matches


# Take user input for pattern
pattern_to_search = input("Enter the pattern to search: ")

# Take user input for text content
print("Enter the text content (type 'EOF' on a new line to end input):")
text_lines = []
while True:
    line = input()
    if line == 'EOF':
        break
    text_lines.append(line)
text_to_search = '\n'.join(text_lines)

# Take user input for case sensitivity
case_sensitive_input = input("Perform case-sensitive search? (y/n): ")
case_sensitive = case_sensitive_input.lower() == 'y'

# Perform the search
result = grep(pattern_to_search, text_to_search, case_sensitive)

# Display the result
print("\nSearch result:")
print(result)
