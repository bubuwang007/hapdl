from ._Ast import Ast

class BinOp(Ast):
    _fields = ['left', 'op', 'right']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"<BinOp {self.left} {self.op} {self.right}>"