from ._Ast import Ast

class BoolOp(Ast):
    _fields = ['op', 'values']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, op, values):
        self.op = op
        self.values = values

    def __repr__(self):
        return f"<BoolOp {self.op} {self.values}>"