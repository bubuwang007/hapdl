import enum
from ._BasicType import BasicType

class Keywords(enum.Enum):
    mapping: dict

    TRUE = 'true'
    FALSE = 'false'
    NONE = 'none'

    LET = 'let'
    DEL = 'del'
    BREAK = 'break'
    CONTINUE = 'continue'

    AND = 'and'
    OR = 'or'

    IMPORT = 'import'
    FROM = 'from'
    AS = 'as'

    ENUM = 'enum'
    STRUCT = 'struct'
    TRAIT = 'trait'
    IMPL = 'impl'

    FUNC = 'func'
    INLINE = 'inline'
    RETURN = 'return'

    IF = 'if'
    ELSE = 'else'
    ELIF = 'elif'
    WHILE = 'while'
    FOR = 'for'
    IN = 'in'
    MATCH = 'match'

    RAISE = 'raise'
    TRY = 'try'
    EXCEPT = 'except'
    FINALLY = 'finally'

    EXTERN = 'extern'
    GLOBAL = 'global'
    PUB = 'pub'
    NONLOCAL = 'nonlocal'
    CONST = 'const'

    @classmethod
    def get(cls, name: str) -> bool:
        kw = cls.mapping.get(name)
        if kw is None:
            kw = BasicType.get(name)
        return kw

    def __str__(self) -> str:
        return "Keywords." + self.name

Keywords.mapping = {
    value.value: value for value in Keywords.__members__.values()
}