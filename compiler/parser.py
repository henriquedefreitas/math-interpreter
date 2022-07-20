from compiler.lexer import Lexer
from compiler.utils import reverse, is_terminal
from compiler.node import Node
from compiler.language import TABLE, E1


class Parser:
    def __init__(self, source_code):
        self.lexer = Lexer(source_code)
        self.table = TABLE

    def parse_tree(self):
        stack = ['$', 'E']

        self.tree = Node('E')
        self.tree.set_rule(E1)
        node_stack = [self.tree]

        cur_symbol = stack.pop()
        node = node_stack.pop()
        cur_token = self.lexer.get_token()

        while cur_symbol != '$' or cur_token.get_tag() != '$':
            if not is_terminal(cur_symbol):
                entry = self.table[cur_symbol][cur_token.get_tag()]
                if entry is None:
                    raise SyntaxError(
                        f'A \"{cur_token.get_tag}\" wasn\'t expected')
                node.set_rule(entry.get_func())
                for symbol in reverse(entry.get_symbols()):
                    new_node = Node(symbol)
                    node.add_child(new_node)
                    node_stack.append(new_node)
                    stack.append(symbol)
            else:
                if cur_symbol == cur_token.get_tag():
                    if cur_token.has_value():
                        node.set_lexval(cur_token.get_val())
                    cur_token = self.lexer.get_token()
                elif cur_symbol != '&':
                    raise SyntaxError(
                        f'A \"{cur_token.get_tag()}\" wasn\'t expected')
            cur_symbol = stack.pop()
            if len(node_stack) != 0:
                node = node_stack.pop()

        # print('Syntax analysis finished')

    def run(self):
        self.tree.rule(self.tree)

    def get_result(self):
        return self.tree.val
