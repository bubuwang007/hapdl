from ._Ast import Ast

class Import(Ast):
    _fields = ['names']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, names):
        self.names = names

    def __repr__(self):
        return f"<Import {self.names}>"
