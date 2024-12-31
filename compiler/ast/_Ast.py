
class Ast:
    _fields: list["Ast"]
    lineno: int
    col_offset: int
    end_lineno: int
    end_col_offset: int
