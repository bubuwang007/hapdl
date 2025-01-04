from ._Ast import Ast

class Raise(Ast):
    _fields = ['exc', 'cause']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, exc, cause):
        self.exc = exc
        self.cause = cause

    def __repr__(self):
        return f"<Raise {self.exc} {self.cause}>"
