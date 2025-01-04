from ._Ast import Ast
from ._Name import Name

class VarDef(Ast):
    lineno = 0
    col_offset = 0
    end_lineno = 0
    end_col_offset = 0

    name: Name
    type: Name
    expr: Ast

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"<VarDef {','.join(map(repr, self._fields))}>"