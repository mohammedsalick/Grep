import sys, os
from argparse import ArgumentParser

def basic_search(string, pattern):
    index = string.find(pattern)
    return index

def grep_file(filename, pattern):
    text = sys.stdin if filename == '(standard input)' else open(filename, 'r')
    line = text.readline()
    while line:
        index = basic_search(line, pattern)
        if index != -1:
            print(line, end='')

        # Read the next line
        line = text.readline()

    text.close()

def grep_files(paths, pattern, recurse):
    for path in paths:
        if os.path.isfile(path) or path == '(standard input)':
            grep_file(path, pattern)
        else:
            if recurse:
                more_paths = [path + '/' + child for child in os.listdir(path)]
                grep_files(more_paths, pattern, recurse)
            else:
                print(f'grep: {path}: Is a directory')

def setup_parser():
    parser = ArgumentParser(description='Find occurrences of a pattern in lines of file(s).', add_help=False)
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('pattern', type=str, help='the pattern to find')
    parser.add_argument('files', metavar='FILES', nargs='*', default=['-'], help='the file(s) to search')
    parser.add_argument('-R', '-r', '--recursive', action='store_true', help='recursively search directories')
    return parser

def main():
    parser = setup_parser()
    args = parser.parse_args()
    pattern = args.pattern

    files = [f if f != '-' else '(standard input)' for f in args.files]
    grep_files(files, pattern, args.recursive)

if __name__ == '__main__':
    main()
