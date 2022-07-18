import math
from compiler.utils import is_terminal


class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.terminal = True if is_terminal(symbol) else False
        self.children = []

    def set_lexval(self, lexval):
        self.lexval = lexval

    def add_child(self, child):
        self.children.insert(0, child)

    def set_rule(self, rule):
        self.rule = rule


def E1(node):
    node.children[0].rule(node.children[0])
    node.children[1].inh = node.children[0].val
    node.children[1].rule(node.children[1])
    node.val = node.children[1].syn


def EL1(node):
    node.children[1].rule(node.children[1])
    node.children[2].inh = node.inh + node.children[1].val
    node.children[2].rule(node.children[2])
    node.syn = node.children[2].syn


def EL2(node):
    node.children[1].rule(node.children[1])
    node.children[2].inh = node.inh - node.children[1].val
    node.children[2].rule(node.children[2])
    node.syn = node.children[2].syn


def EL3(node):
    node.syn = node.inh


def T1(node):
    node.children[0].rule(node.children[0])
    node.children[1].inh = node.children[0].val
    node.children[1].rule(node.children[1])
    node.val = node.children[1].syn


def TL1(node):
    node.children[1].rule(node.children[1])
    node.children[2].inh = node.inh * node.children[1].val
    node.children[2].rule(node.children[2])
    node.syn = node.children[2].syn


def TL2(node):
    node.children[1].rule(node.children[1])
    node.children[2].inh = node.inh / node.children[1].val
    node.children[2].rule(node.children[2])
    node.syn = node.children[2].syn


def TL3(node):
    node.syn = node.inh


def P1(node):
    node.children[0].rule(node.children[0])
    node.children[1].inh = node.children[0].val
    node.children[1].rule(node.children[1])
    node.val = node.children[1].syn


def P2(node):
    node.children[2].rule(node.children[2])
    node.children[4].inh = math.e ** node.children[2].val
    node.children[4].rule(node.children[4])
    node.val = node.children[4].syn


def PL1(node):
    node.children[1].rule(node.children[1])
    node.children[2].inh = node.inh ** node.children[1].val
    node.children[2].rule(node.children[2])
    node.syn = node.children[2].syn


def PL2(node):
    node.syn = node.inh


def F1(node):
    node.children[1].rule(node.children[1])
    node.val = node.children[1].val


def F2(node):
    node.val = node.children[0].lexval


'''
<E>  -> <T> {E'.inh = T.val} <E'> {E.val = E'.syn}
<E'> -> +<T> {E'.inh = E'.inh + T.val} <E'> {E'.syn = E'.syn}
<E'> -> -<T> {E'.inh = E'.inh - T.val} <E'> {E'.syn = E'.syn}
<E'> -> & {E'.syn = E'.inh}
<T>  -> <P> {T'.inh = P.val} <T'> {T.val = T'.syn}
<T'> -> *<P> {T'.inh = T'.inh * P.val} <T'> {T'.syn = T'.syn}
<T'> -> /<P> {T'.inh = T'.inh / P.val} <T'> {T'.syn = T'.syn}
<T'> -> & {T'.syn = T'.inh}
<P>  -> <F> {P'.inh = F.val} <P'> {P.val = P'.syn}
<P>  -> exp[<F> {P'.inh = F.val }]<P'> {P.val = P'.syn}
<P'> -> /<F> {P'.inh = P'.inh / F.val} <P'> {P'.syn = P'.syn}
<P'> -> & {P'.syn = P'.inh}
<F>  -> (<E> {F.val = E.val} )
<F>  -> id {F.val = id.lexval}
'''
