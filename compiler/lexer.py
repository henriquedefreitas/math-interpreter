from compiler.exceptions import SyntaxError
from compiler.tokens import Tag, Token


class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.source_code += '$'
        self.cursor = 0

    def get_token(self):
        self.state = 0
        buffer = ''
        while(True):
            symbol = self.source_code[self.cursor]

            if self.state == 0:
                if symbol in [' ', '\n']:
                    self.cursor += 1
                    continue
                if symbol == '$':
                    return Token(Tag.END)
                if symbol == 'e':
                    self.state = 3
                    self.cursor += 1
                    continue
                if symbol in ['+', '-', '*', '/', '^', '(', ')', '[', ']']:
                    self.cursor += 1
                    if symbol == '+':
                        return Token(Tag.ADD)
                    if symbol == '-':
                        return Token(Tag.SUB)
                    if symbol == '*':
                        return Token(Tag.MUL)
                    if symbol == '/':
                        return Token(Tag.DIV)
                    if symbol == '^':
                        return Token(Tag.EXP)
                    if symbol == '(':
                        return Token(Tag.OPEN_PAR)
                    if symbol == ')':
                        return Token(Tag.CLOSE_PAR)
                    if symbol == '[':
                        return Token(Tag.OPEN_BRACKET)
                    if symbol == ']':
                        return Token(Tag.CLOSE_BRACKET)

                if symbol.isnumeric():
                    buffer += symbol
                    self.state = 1
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError(f'Expected an operator, digit,\
                        parenthesis or bracket, instead found a \"{symbol}\"')

            if self.state == 1:
                if symbol.isnumeric():
                    buffer += symbol
                    self.cursor += 1
                    continue
                if symbol == '.':
                    self.state = 6
                    buffer += symbol
                    self.cursor += 1
                    continue
                else:
                    return Token(Tag.NUM, buffer)

            if self.state == 6:
                if symbol.isnumeric():
                    buffer += symbol
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError('Expected a digit after \".\"')

            if self.state == 2:
                if symbol.isnumeric():
                    buffer += symbol
                    self.cursor += 1
                    continue
                else:
                    return Token(Tag.NUM, buffer)

            if self.state == 3:
                if symbol == 'x':
                    self.state = 4
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError('Expected an \"x\"')

            if self.state == 4:
                if symbol == 'p':
                    self.cursor += 1
                    return Token(Tag.EULER)
                else:
                    raise SyntaxError('Expected an \"p\"')
