import enum

class BasicType(enum.Enum):
    mapping: dict

    TYPE = 'type'
    NUM = 'num'
    COMPLEX = 'complex'
    STR = 'str32'
    BOOL = 'bool'
    TABLE = 'table'
    ARRAY = 'array'
    LIST = 'list'
    DYNLIST = 'dynlist'
    STR8ARRAY = 'str8array'
    STR32ARRAY = 'str32array'
    STRARRAY = 'strarray'
    FUNCTION = 'function'

    @classmethod
    def get(cls, name: str) -> bool:
        return cls.mapping.get(name)
    
    def __str__(self) -> str:
        return "Keywords.BasicType." + self.name

BasicType.mapping = {
    value.value: value for value in BasicType.__members__.values()
}
