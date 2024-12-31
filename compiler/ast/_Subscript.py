from ._Ast import Ast

class Subscript(Ast):
    _fields = ['value', 'slice']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, value, slice):
        self.value = value
        self.slice = slice

    def __repr__(self):
        return f"<Subscript {self.value} {self.slice}>"