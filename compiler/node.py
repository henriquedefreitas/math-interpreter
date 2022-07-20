from compiler.utils import is_terminal


class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.terminal = True if is_terminal(symbol) else False
        self.children = []

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def set_syn(self, syn):
        self.syn = syn

    def get_syn(self):
        return self.syn

    def set_inh(self, inh):
        self.inh = inh

    def get_inh(self):
        return self.inh

    def set_lexval(self, lexval):
        self.lexval = lexval

    def get_lexval(self):
        return self.lexval

    def add_child(self, child):
        self.children.insert(0, child)

    def set_rule(self, rule):
        self.rule = rule
