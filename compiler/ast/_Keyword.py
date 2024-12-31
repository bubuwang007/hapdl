from ._Ast import Ast

class Keyword(Ast):
    _fields = ['arg', 'value']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, arg, value):
        self.arg = arg
        self.value = value

    def __repr__(self):
        return f"<Keyword {self.arg} {self.value}>"