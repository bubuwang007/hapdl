from ._Ast import Ast

class Name(Ast):
    _fields = ['id', 'ctx']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, id, ctx):
        self.id = id
        self.ctx = ctx

    def __repr__(self):
        return f"<Name {self.id} {self.ctx}>"