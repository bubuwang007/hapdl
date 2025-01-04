from ._Ast import Ast

class UnaryOp(Ast):
    _fields = ['op', 'operand']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def __repr__(self):
        return f"<UnaryOp {self.op} {self.operand}>"