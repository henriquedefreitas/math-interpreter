from enum import Enum


class Tag(Enum):
    INTEGER = 1
    REAL = 2
    ADD = 3
    SUB = 4
    MUL = 5
    DIV = 6
    EXP = 7
    PAR_BEGIN = 8
    PAR_END = 9
    EULER_BEGIN = 10
    EULER_END = 11


class Token:
    def __init__(self, tag):
        self.tag = tag


class Integer(Token):
    def __init__(self, num):
        super().__init__(Tag.INTEGER)
        self.num = num


class Real(Token):
    def __init__(self, num):
        super().__init__(Tag.REAL)
        self.num = num


class Add(Token):
    def __init__(self):
        super().__init__(Tag.ADD)


class Sub(Token):
    def __init__(self):
        super().__init__(Tag.SUB)


class Mul(Token):
    def __init__(self):
        super().__init__(Tag.MUL)


class Div(Token):
    def __init__(self):
        super().__init__(Tag.DIV)


class Exp(Token):
    def __init__(self):
        super().__init__(Tag.EXP)


class ParBegin(Token):
    def __init__(self):
        super().__init__(Tag.PAR_BEGIN)


class ParEnd(Token):
    def __init__(self):
        super().__init__(Tag.PAR_END)


class EulerBegin(Token):
    def __init__(self):
        super().__init__(Tag.EULER_BEGIN)


class EulerEnd(Token):
    def __init__(self):
        super().__init__(Tag.EULER_END)
