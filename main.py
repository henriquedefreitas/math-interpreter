from compiler.parser import Parser
from compiler.utils import print_tree
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='A compiler for simple math expressions')
    parser.add_argument(
        'path',
        type=str,
        help='Path to the source code file'
    )
    parser.add_argument(
        '-t',
        '--show-tree',
        action='store_true',
        help='Print the syntax tree'
    )
    parser.add_argument(
        '-e',
        '--show-exp',
        action='store_true',
        help='Show the expression'
    )
    args = parser.parse_args()

    # Read input file
    with open(args.path) as file:
        source_code = file.read()

    # Analyse line syntax and run its code
    for line in source_code.split('\n'):
        if args.show_exp is True:
            print(line)
        parser = Parser(line)
        parser.parse_tree()
        if args.show_tree is True:
            print('Syntax tree:')
            print_tree(parser.tree)
        parser.run()
        result = parser.get_result()
        print(result)


if __name__ == '__main__':
    main()
