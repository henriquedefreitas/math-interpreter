from interpreter.language import TERMINAL


def reverse(rule):
    new_rule = []
    for i in range(len(rule) - 1, -1, -1):
        new_rule.append(rule[i])
    return new_rule


def is_terminal(string):
    return True if string in TERMINAL else False


def print_tree(tree):
    # print('Syntax tree:')
    print(tree.symbol)
    for child in tree.children:
        print_child(child, 1)


def print_child(node, depth):
    for _ in range(depth):
        print('|\t', end='')
    print(node.symbol)
    for child in node.children:
        print_child(child, depth + 1)
