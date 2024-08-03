from abc import ABC, abstractmethod
from numpy import double

class Expression(ABC):
    @abstractmethod
    def calc(self) -> double:
        pass

class Num(Expression):
    def __init__(self, value):
        self.value = value

    def calc(self) -> double:
        return double(self.value)

class BinExp(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

class Plus(BinExp):
    def calc(self) -> double:
        return self.left.calc() + self.right.calc()

class Minus(BinExp):
    def calc(self) -> double:
        return self.left.calc() - self.right.calc()

class Mul(BinExp):
    def calc(self) -> double:
        return self.left.calc() * self.right.calc()

class Div(BinExp):
    def calc(self) -> double:
        return self.left.calc() / self.right.calc()

class UnaryMinus(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def calc(self) -> double:
        return -self.expr.calc()

def parser(expression: str) -> double:
    def parse_expression(tokens, index):
        result, index = parse_term(tokens, index)
        while index < len(tokens) and tokens[index] in ['+', '-']:
            op, index = tokens[index], index + 1
            right, index = parse_term(tokens, index)
            result = Plus(result, right) if op == '+' else Minus(result, right)
        return result, index

    def parse_term(tokens, index):
        result, index = parse_factor(tokens, index)
        while index < len(tokens) and tokens[index] in ['*', '/']:
            op, index = tokens[index], index + 1
            right, index = parse_factor(tokens, index)
            result = Mul(result, right) if op == '*' else Div(result, right)
        return result, index

    def parse_factor(tokens, index):
        if tokens[index] == '(':
            result, index = parse_expression(tokens, index + 1)
            if index < len(tokens) and tokens[index] == ')':
                return result, index + 1
        elif tokens[index] == '-':
            result, index = parse_factor(tokens, index + 1)
            return UnaryMinus(result), index
        else:
            try:
                return Num(float(tokens[index])), index + 1
            except ValueError:
                raise ValueError(f"Invalid token: {tokens[index]}")

    tokens = tokenize(expression)
    result, _ = parse_expression(tokens, 0)
    return result.calc()

def tokenize(expression: str) -> list:
    import re
    tokens = re.findall(r'\d+\.\d+|\d+|[()+*/-]', expression)
    return tokens
