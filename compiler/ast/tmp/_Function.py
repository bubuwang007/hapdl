from ._Ast import Ast

class Function(Ast):
    _fields = ['name', 'args', 'body', 'decorator_list', 'returns']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, name, args, body, decorator_list, returns):
        self.name = name
        self.args = args
        self.body = body
        self.decorator_list = decorator_list
        self.returns = returns

    def __repr__(self):
        return f"<Function {self.name} {self.args} {self.body} {self.decorator_list} {self.returns}>"