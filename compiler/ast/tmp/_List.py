from ._Ast import Ast

class List(Ast):
    _fields = ['elts']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, elts):
        self.elts = elts

    def __repr__(self):
        return f"<List {self.elts}>"