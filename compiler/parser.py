from compiler.lexer import Lexer
from compiler.sdd import Node, is_terminal, E1, EL1, EL2, EL3, T1, TL1, TL2, TL3, P1, P2, PL1, PL2, F1, F2
from compiler.utils import reverse


class Parser:
    def __init__(self, source_code):
        self.lexer = Lexer(source_code)
        self.__construct_table()

    def parse_tree(self):
        stack = ['$', 'E']

        self.tree = Node('E')
        self.tree.set_rule(E1)
        node_stack = ['$', self.tree]

        cur_symbol = stack.pop()
        cur_token = self.lexer.get_token()
        node = node_stack.pop()

        # While the current symbol is not the last
        while cur_symbol != '$':
            # print(f'cur_symbol = {cur_symbol}')
            # print(f'cur_token = {cur_token.get_symbol()}')
            # print(f'node = {node.symbol}')
            # If the current symbol is not a terminal
            if not is_terminal(cur_symbol):
                # Get the rule for the current symbol and current token
                rule = self.table[cur_symbol][cur_token.get_symbol()]
                # Check if an entry for that pair exists
                if rule is None:
                    raise SyntaxError(f'A \"{cur_token.symbol}\" wasn\'t expected')
                # Define the node rule/type
                node.set_rule(rule[1])
                # Instantiates "blank" nodes for each child of the node according to the rule found
                for symbol in reverse(rule[0]):
                    new_node = Node(symbol)
                    node.add_child(new_node)
                    node_stack.append(new_node)
                    stack.append(symbol)
            # If current symbol is terminal
            else:
                # if current terminal matches current token, pop() token stack
                if cur_symbol == cur_token.get_symbol():
                    # if token has a value, set node value as well
                    if hasattr(cur_token, 'lexval'):
                        node.set_lexval(cur_token.lexval)
                    cur_token = self.lexer.get_token()
                elif cur_symbol != '&':
                    raise SyntaxError(
                        f'A \"{cur_token.get_symbol()}\" wasn\'t expected')
            node = node_stack.pop()
            cur_symbol = stack.pop()

        # print('Syntax analysis finished')

    def run(self):
        self.tree.rule(self.tree)
        
    def get_result(self):
        return self.tree.val

    def __construct_table(self):
        # Initialize the table

        self.table = {
            'E': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'E\'': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'T': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'T\'': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'P': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'P\'': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            },
            'F': {
                '$': None, 'num': None, '+': None, '-': None, '*': None,
                '/': None, '^': None, '(': None, ')': None, 'exp[': None
            }
        }

        # Add all table entries based on the rules
        self.table['E']['num'] = [['T', 'E\''], E1]
        self.table['E']['('] = [['T', 'E\''], E1]
        self.table['E']['exp'] = [['T', 'E\''], E1]

        self.table['E\'']['$'] = [['&'], EL3]
        self.table['E\'']['+'] = [['+', 'T', 'E\''], EL1]
        self.table['E\'']['-'] = [['-', 'T', 'E\''], EL2]
        self.table['E\''][')'] = [['&'], EL3]

        self.table['T']['num'] = [['P', 'T\''], T1]
        self.table['T']['('] = [['P', 'T\''], T1]
        self.table['T']['exp'] = [['P', 'T\''], T1]

        self.table['T\'']['$'] = [['&'], TL3]
        self.table['T\'']['+'] = [['&'], TL3]
        self.table['T\'']['-'] = [['&'], TL3]
        self.table['T\'']['*'] = [['*', 'P', 'T\''], TL1]
        self.table['T\'']['/'] = [['/', 'P', 'T\''], TL2]
        self.table['T\''][')'] = [['&'], TL3]

        self.table['P']['num'] = [['F', 'P\''], P1]
        self.table['P']['('] = [['F', 'P\''], P1]
        self.table['P']['exp'] = [['exp', '[', 'F', ']', 'P\''], P2]

        self.table['P\'']['$'] = [['&'], PL2]
        self.table['P\'']['+'] = [['&'], PL2]
        self.table['P\'']['-'] = [['&'], PL2]
        self.table['P\'']['*'] = [['&'], PL2]
        self.table['P\'']['/'] = [['&'], PL2]
        self.table['P\'']['^'] = [['^', 'F', 'P\''], PL1]
        self.table['P\''][')'] = [['&'], PL2]

        self.table['F']['num'] = [['num'], F2]
        self.table['F']['('] = [['(', 'E', ')'], F1]
