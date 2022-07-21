from interpreter.parser import Parser
from interpreter.utils import print_tree
from interpreter.exceptions import SyntaxError
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='A interpreter for computing simple math expressions')
    parser.add_argument(
        'path',
        type=str,
        help='path to the source code file'
    )
    parser.add_argument(
        '-t',
        '--show-tree',
        action='store_true',
        help='print the syntax tree'
    )
    parser.add_argument(
        '-e',
        '--show-exp',
        action='store_true',
        help='show the expression'
    )
    args = parser.parse_args()

    # Read input file
    with open(args.path) as file:
        source_code = file.read()

    # Analyse line syntax and run its code
    for i, line in enumerate(source_code.split('\n')):
        # If line isn't a blank line
        line = line.strip()
        if line != '':
            if args.show_exp is True:
                print(line)
            parser = Parser(line)
            try:
                parser.parse_tree()
            except SyntaxError as e:
                raise SyntaxError(f'Line {i + 1}; ' + str(e))
            if args.show_tree is True:
                print_tree(parser.tree)
            parser.run()
            result = parser.get_result()
            print(result)


if __name__ == '__main__':
    main()
