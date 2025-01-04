from ._Ast import Ast

class Module(Ast):
    _fields = ['stmts']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, level=0):
        self.level = level
        self.stmts = []

    def __repr__(self):
        return f"<Module {','.join(map(repr, self.stmts))}>"

    def append(self, stmt):
        self.stmts.append(stmt)