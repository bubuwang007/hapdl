from ._Ast import Ast

class Slice(Ast):
    _fields = ['value', 'lower', 'upper', 'step']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, value, lower, upper, step):
        self.value = value
        self.lower = lower
        self.upper = upper
        self.step = step

    def __repr__(self):
        return f"<Slice {self.value} {self.lower} {self.upper} {self.step}>"