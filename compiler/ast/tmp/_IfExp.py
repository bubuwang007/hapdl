from ._Ast import Ast

class IfExp(Ast):
    _fields = ['test', 'body', 'orelse']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, test, body, orelse):
        self.test = test
        self.body = body
        self.orelse = orelse

    def __repr__(self):
        return f"<IfExp {self.test} {self.body} {self.orelse}>"
