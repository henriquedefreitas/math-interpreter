from compiler.parser import Parser
from compiler.utils import print_tree
import argparse


def main():

    # Parse arguments
    parser = argparse.ArgumentParser(
        description='A compiler for simple math expressions')
    parser.add_argument('path',
                        type=str,
                        help='Path to the source code file')
    args = parser.parse_args()

    # Read input file
    with open(args.path) as file:
        source_code = file.read()

    # Analyse syntax and compute answer
    for line in source_code.split('\n'):
        print(line)
        parser = Parser(line)
        parser.parse_tree()
        # print('Syntax tree:')
        # print_tree(parser.tree)
        # print('\n\n')
        parser.execute()


main()
