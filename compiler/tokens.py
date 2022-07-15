from enum import Enum


class Tag(Enum):
    NUM = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    EXP = 5
    OPEN_PAR = 6
    CLOSE_PAR = 7
    OPEN_BRACKET = 8
    CLOSE_BRACKET = 9
    EULER = 10
    END = 11


class Token:
    def __init__(self, tag, buffer=''):
        self.tag = tag

        if tag == Tag.NUM:
            self.symbol = 'num'
            self.lexval = float(buffer)
        if tag == Tag.ADD:
            self.symbol = '+'
        if tag == Tag.SUB:
            self.symbol = '-'
        if tag == Tag.MUL:
            self.symbol = '*'
        if tag == Tag.DIV:
            self.symbol = '/'
        if tag == Tag.EXP:
            self.symbol = '^'
        if tag == Tag.OPEN_PAR:
            self.symbol = '('
        if tag == Tag.CLOSE_PAR:
            self.symbol = ')'
        if tag == Tag.OPEN_BRACKET:
            self.symbol = '['
        if tag == Tag.CLOSE_BRACKET:
            self.symbol = ']'
        if tag == Tag.EULER:
            self.symbol = 'exp'
        if tag == Tag.END:
            self.symbol = '$'

    def get_symbol(self):
        return self.symbol
