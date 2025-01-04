from ._Ast import Ast

class Call(Ast):
    _fields = ['func', 'args', 'keywords']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, func, args, keywords):
        self.func = func
        self.args = args
        self.keywords = keywords

    def __repr__(self):
        return f"<Call {self.func} {self.args} {self.keywords}>"