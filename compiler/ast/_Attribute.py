from ._Ast import Ast

class Attribute(Ast):
    _fields = ['value', 'attr', 'ctx']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, value, attr, ctx):
        self.value = value
        self.attr = attr
        self.ctx = ctx

    def __repr__(self):
        return f"<Attribute {self.value} {self.attr} {self.ctx}>"