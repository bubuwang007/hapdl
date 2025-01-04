from ._Ast import Ast

class Compare(Ast):
    _fields = ['left', 'ops', 'comparators']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, left, ops, comparators):
        self.left = left
        self.ops = ops
        self.comparators = comparators

    def __repr__(self):
        return f"<Compare {self.left} {self.ops} {self.comparators}>"
