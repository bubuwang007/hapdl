from ._Ast import Ast

class AugAssign(Ast):
    _fields = ['target', 'op', 'value']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, target, op, value):
        self.target = target
        self.op = op
        self.value = value

    def __repr__(self):
        return f"<AugAssign {self.target} {self.op} {self.value}>"