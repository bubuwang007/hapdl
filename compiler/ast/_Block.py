from ._Ast import Ast

class Block(Ast):
    _fields = ['body']
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return f"<Block {self.body}>"

