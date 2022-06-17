from compiler.exceptions import SyntaxError
from compiler.tokens import Integer, Real, Add, Sub, Mul, Div, Exp, ParBegin, ParEnd, EulerBegin, EulerEnd


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
                    return None
                if symbol == 'e':
                    self.state = 3
                    self.cursor += 1
                    continue
                if symbol in ['+', '-', '*', '/', '^', '(', ')', ']']:
                    self.cursor += 1
                    if symbol == '+':
                        return Add()
                    if symbol == '-':
                        return Sub()
                    if symbol == '*':
                        return Mul()
                    if symbol == '/':
                        return Div()
                    if symbol == '^':
                        return Exp()
                    if symbol == '(':
                        return ParBegin()
                    if symbol == ')':
                        return ParEnd()
                    if symbol == ']':
                        return EulerEnd()

                if symbol.isnumeric():
                    buffer += symbol
                    self.state = 1
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError('Expected an operator or a digit')

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
                    return Integer(int(buffer))

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
                    return Real(float(buffer))

            if self.state == 3:
                if symbol == 'x':
                    self.state = 4
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError('Expected an \"x\"')

            if self.state == 4:
                if symbol == 'p':
                    self.state = 5
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError('Expected an \"p\"')

            if self.state == 5:
                if symbol == '[':
                    self.cursor += 1
                    return EulerBegin()
                else:
                    raise SyntaxError('Expected an \"[\"')
