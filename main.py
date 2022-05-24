#from parser import parser
import argparse

def main():
    
    # Prase arguments
    parser = argparse.ArgumentParser(description='Compiler')
    parser.add_argument('path',
                        type=str,
                        help='Path to the source code file')
    args = parser.parse_args()

    # Read input file
    with open(args.path) as file:
        source_code = file.read()
        
    # Syntax analisys
    parser = Parser(source_code)
    
    parse_tree = parser.parse()
    
    # Semantic analisys

    # Intemediate code generator

    # Write output file
    
main()