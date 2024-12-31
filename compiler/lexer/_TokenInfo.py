import dataclasses
from ._Token import TokenType
from ._BasicType import BasicType
from ._Keywords import Keywords

@dataclasses.dataclass
class TokenInfo:
    type: TokenType | BasicType | Keywords
    value: str
    line: int
    column: int
    end_column: int

    def __str__(self) -> str:
        return f"TokenInfo({self.type}, {self.value!r}, {self.line}, {self.column}, {self.end_column})"
