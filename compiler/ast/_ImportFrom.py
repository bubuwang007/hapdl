from ._Ast import Ast

class ImportFrom(Ast):
    _fields = ['module', 'names', 'level']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, module, names, level):
        self.module = module
        self.names = names
        self.level = level

    def __repr__(self):
        return f"<ImportFrom {self.module} {self.names} {self.level}>"