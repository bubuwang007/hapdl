from ._Ast import Ast

class Name(Ast):
    _fields = ['id']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0
    id: str

    def __init__(self, id, level=0):
        self.level = level
        self.id = id

    def __repr__(self):
        return f"{'\t'*self.level}<Name id:{self.id}>"