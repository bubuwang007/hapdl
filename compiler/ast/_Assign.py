from ._Ast import Ast

class Assign(Ast):
    _fields = ['targets', 'value']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, targets, value):
        self.targets = targets
        self.value = value

    def __repr__(self):
        return f"<Assign {self.targets} {self.value}>"