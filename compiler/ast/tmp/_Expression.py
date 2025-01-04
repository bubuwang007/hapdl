from ._Ast import Ast

class Expression(Ast):
    _fields = ['value']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"<Expression {self.value}>"