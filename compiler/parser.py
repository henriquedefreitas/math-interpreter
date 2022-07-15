from compiler.lexer import Lexer


def is_terminal(string):
    if string in ['E', 'E\'', 'T', 'T\'', 'P', 'P\'', 'F']:
        return False
    return True


def reverse(rule):
    new_rule = []
    for i in range(len(rule) - 1, -1, -1):
        new_rule.append(rule[i])
    return new_rule


class Node:
    def __init__(self, symbol, rule):
        self.symbol = symbol
        self.terminal = True if is_terminal(symbol) else False
        self.children = []
        self.rule = rule

    def add_child(self, child):
        self.children.insert(0, child)


class Parser:
    def __init__(self, source_code):
        self.lexer = Lexer(source_code)
        self.__construct_table()

    def parse_tree(self):
        stack = ['$', 'E']

        tree = Node('E')
        node_stack = ['$', tree]

        cur_symbol = stack.pop()
        cur_token = self.lexer.get_token()

        node = node_stack.pop()

        while cur_symbol != '$':
            # print(f'stack = {stack}')
            # print(f'cur_symbol = {cur_symbol}')
            # print(f'cur_token = {cur_token.get_symbol()}')
            # print()
            # If current symbol is non terminal
            if not is_terminal(cur_symbol):
                rule = self.table[cur_symbol][cur_token.get_symbol()]
                # print(f'rule = {rule}')
                if rule is None:
                    raise SyntaxError(f'\"{cur_token.symbol}\" mispositioned')
                else:
                    # print(rule)
                    for symbol in reverse(rule):
                        new_node = Node(symbol, rule)
                        node.add_child(new_node)
                        if not is_terminal(symbol):
                            node_stack.append(new_node)
                        stack.append(symbol)
                    node = node_stack.pop()
            # If current symbol is terminal
            else:
                if cur_symbol == '&':
                    cur_symbol = stack.pop()
                    continue
                if cur_symbol == cur_token.get_symbol():
                    cur_token = self.lexer.get_token()
                else:
                    raise SyntaxError(
                        f'\"{cur_token.get_symbol()}\" mispositioned')

            cur_symbol = stack.pop()

        print('Syntax analysis finished')

        return tree

    def __construct_table(self):
        # Initialize the table
        self.table = {
            'E': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'E\'': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'T': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'T\'': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'P': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'P\'': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'F': {
                '$': None, 'id': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            }
        }

        # Add all table entries based on the rules
        self.table['E']['id'] = [['T', 'E\'']]
        self.table['E']['('] = ['T', 'E\'']
        self.table['E']['exp'] = ['T', 'E\'']

        self.table['E\'']['$'] = ['&']
        self.table['E\'']['+'] = ['+', 'T', 'E\'']
        self.table['E\'']['-'] = ['-', 'T', 'E\'']
        self.table['E\''][')'] = ['&']

        self.table['T']['id'] = ['P', 'T\'']
        self.table['T']['('] = ['P', 'T\'']
        self.table['T']['exp'] = ['P', 'T\'']

        self.table['T\'']['$'] = ['&']
        self.table['T\'']['+'] = ['&']
        self.table['T\'']['-'] = ['&']
        self.table['T\'']['*'] = ['*', 'P', 'T\'']
        self.table['T\'']['/'] = ['/', 'P', 'T\'']
        self.table['T\''][')'] = ['&']

        self.table['P']['id'] = ['F', 'P\'']
        self.table['P']['('] = ['F', 'P\'']
        self.table['P']['exp'] = ['exp', '[', 'F', ']', 'P\'']

        self.table['P\'']['$'] = ['&']
        self.table['P\'']['+'] = ['&']
        self.table['P\'']['-'] = ['&']
        self.table['P\'']['*'] = ['&']
        self.table['P\'']['/'] = ['&']
        self.table['P\'']['^'] = ['^', 'F', 'P\'']
        self.table['P\''][')'] = ['&']

        self.table['F']['id'] = ['id']
        self.table['F']['('] = ['(', 'E', ')']
