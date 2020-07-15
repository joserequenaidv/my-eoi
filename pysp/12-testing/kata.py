import re


def sum_numbers_in(expression: str) -> int:
    if expression is None or expression == "":
        return 0
    if "," in expression:
        tokens = expression.split(',')
        total = 0
        for token in tokens:
            total = total + parse_int(token)
        return total
    return parse_int(expression)


def parse_int(token):
    if re.match("^[0-9]+$", token):
        return int(token)
    return 0
