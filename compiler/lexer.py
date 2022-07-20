from compiler.exceptions import SyntaxError
from compiler.token import Token
from compiler.language import OPERATORS


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
                if symbol == '$':
                    return Token('$')
                if symbol in [' ', '\n']:
                    self.cursor += 1
                    continue
                if symbol in OPERATORS:
                    self.cursor += 1
                    return Token(symbol)
                if symbol.isnumeric():
                    buffer += symbol
                    self.state = 1
                    self.cursor += 1
                    continue
                if symbol == 'e':
                    self.state = 4
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError(f'Col {self.cursor + 1}. Found a symbol that doesn\'t belong to the language: \"{symbol}\"')

            if self.state == 1:
                if symbol.isnumeric():
                    buffer += symbol
                    self.cursor += 1
                    continue
                if symbol == '.':
                    self.state = 2
                    buffer += symbol
                    self.cursor += 1
                    continue
                else:
                    return Token('num', buffer)

            if self.state == 2:
                if symbol.isnumeric():
                    self.state = 3
                    buffer += symbol
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError(f'Col {self.cursor + 1}. Expected a digit after \".\". Found a \"{symbol}\"')

            if self.state == 3:
                if symbol.isnumeric():
                    buffer += symbol
                    self.cursor += 1
                    continue
                else:
                    return Token('num', buffer)

            if self.state == 4:
                if symbol == 'x':
                    self.state = 5
                    self.cursor += 1
                    continue
                else:
                    raise SyntaxError(f'Col {self.cursor + 1}. Expected a \"x\". Found a \"{symbol}\"')

            if self.state == 5:
                if symbol == 'p':
                    self.cursor += 1
                    return Token('exp')
                else:
                    raise SyntaxError(f'Col {self.cursor + 1}. Expected a \"p\". Found a \"{symbol}\"')
