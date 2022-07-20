import math


class TableEntry:
    def __init__(self, symbols, func):
        self.symbols = symbols
        self.func = func

    def get_symbols(self):
        return self.symbols

    def get_func(self):
        return self.func


# Define the sdd as functions
def E1(node):
    node.children[0].rule(node.children[0])
    node.children[1].set_inh(node.children[0].get_val())
    node.children[1].rule(node.children[1])
    node.set_val(node.children[1].get_syn())


def EL1(node):
    node.children[1].rule(node.children[1])
    node.children[2].set_inh(node.get_inh() + node.children[1].get_val())
    node.children[2].rule(node.children[2])
    node.set_syn(node.children[2].get_syn())


def EL2(node):
    node.children[1].rule(node.children[1])
    node.children[2].set_inh(node.get_inh() - node.children[1].get_val())
    node.children[2].rule(node.children[2])
    node.set_syn(node.children[2].get_syn())


def EL3(node):
    node.set_syn(node.get_inh())


def T1(node):
    node.children[0].rule(node.children[0])
    node.children[1].set_inh(node.children[0].get_val())
    node.children[1].rule(node.children[1])
    node.set_val(node.children[1].get_syn())


def TL1(node):
    node.children[1].rule(node.children[1])
    node.children[2].set_inh(node.get_inh() * node.children[1].get_val())
    node.children[2].rule(node.children[2])
    node.set_syn(node.children[2].get_syn())


def TL2(node):
    node.children[1].rule(node.children[1])
    node.children[2].set_inh(node.get_inh() / node.children[1].get_val())
    node.children[2].rule(node.children[2])
    node.set_syn(node.children[2].get_syn())


def TL3(node):
    node.set_syn(node.get_inh())


def P1(node):
    node.children[0].rule(node.children[0])
    node.children[1].set_inh(node.children[0].get_val())
    node.children[1].rule(node.children[1])
    node.set_val(node.children[1].get_syn())


def P2(node):
    node.children[2].rule(node.children[2])
    node.children[4].set_inh(math.e ** node.children[2].get_val())
    node.children[4].rule(node.children[4])
    node.set_val(node.children[4].get_syn())


def PL1(node):
    node.children[1].rule(node.children[1])
    node.children[2].set_inh(node.get_inh() ** node.children[1].get_val())
    node.children[2].rule(node.children[2])
    node.set_syn(node.children[2].get_syn())


def PL2(node):
    node.set_syn(node.get_inh())


def F1(node):
    node.children[1].rule(node.children[1])
    node.set_val(node.children[1].get_val())


def F2(node):
    node.set_val(node.children[0].get_lexval())


OPERATORS = ['+', '-', '*', '/', '^', '(', ')', '[', ']']
TERMINAL = ['num', '+', '-', '*', '/', '^',
            '(', ')', '[', ']', 'exp', '&', '$']
NON_TERMINAL = ['E', 'EL', 'T', 'TL', 'P', 'PL', 'F']

TABLE = {
    'E': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    },
    'EL': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    },
    'T': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    },
    'TL': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    },
    'P': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    },
    'PL': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    },
    'F': {
        '$': None, 'num': None, '+': None, '-': None, '*': None,
        '/': None, '^': None, '(': None, ')': None, 'exp[': None
    }
}

# Add all table entries based on the rules
TABLE['E']['num'] = TableEntry(['T', 'EL'], E1)
TABLE['E']['('] = TableEntry(['T', 'EL'], E1)
TABLE['E']['exp'] = TableEntry(['T', 'EL'], E1)

TABLE['EL']['$'] = TableEntry(['&'], EL3)
TABLE['EL']['+'] = TableEntry(['+', 'T', 'EL'], EL1)
TABLE['EL']['-'] = TableEntry(['-', 'T', 'EL'], EL2)
TABLE['EL'][')'] = TableEntry(['&'], EL3)

TABLE['T']['num'] = TableEntry(['P', 'TL'], T1)
TABLE['T']['('] = TableEntry(['P', 'TL'], T1)
TABLE['T']['exp'] = TableEntry(['P', 'TL'], T1)

TABLE['TL']['$'] = TableEntry(['&'], TL3)
TABLE['TL']['+'] = TableEntry(['&'], TL3)
TABLE['TL']['-'] = TableEntry(['&'], TL3)
TABLE['TL']['*'] = TableEntry(['*', 'P', 'TL'], TL1)
TABLE['TL']['/'] = TableEntry(['/', 'P', 'TL'], TL2)
TABLE['TL'][')'] = TableEntry(['&'], TL3)

TABLE['P']['num'] = TableEntry(['F', 'PL'], P1)
TABLE['P']['('] = TableEntry(['F', 'PL'], P1)
TABLE['P']['exp'] = TableEntry(['exp', '[', 'F', ']', 'PL'], P2)

TABLE['PL']['$'] = TableEntry(['&'], PL2)
TABLE['PL']['+'] = TableEntry(['&'], PL2)
TABLE['PL']['-'] = TableEntry(['&'], PL2)
TABLE['PL']['*'] = TableEntry(['&'], PL2)
TABLE['PL']['/'] = TableEntry(['&'], PL2)
TABLE['PL']['^'] = TableEntry(['^', 'F', 'PL'], PL1)
TABLE['PL'][')'] = TableEntry(['&'], PL2)

TABLE['F']['num'] = TableEntry(['num'], F2)
TABLE['F']['('] = TableEntry(['(', 'E', ')'], F1)
