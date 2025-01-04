from ._Symbol import Symbol

class Symtable:

    name: str
    pre: "Symtable"
    names: dict[str, Symbol]

    def __init__(self, name="", pre: "Symtable" = None):
        self.name = name
        self.pre = pre
        self.names = {}

    def get(self, name: str) -> Symbol:
        if name in self.names:
            return self.names[name]
        elif self.pre is not None:
            return self.pre.get(name)
        else:
            return None

    def set(self, name: str, symbol: Symbol):
        self.names[name] = symbol

    def __str__(self) -> str:
        return "Symtable: " + str(self.names)
    
    def next(self, name: str="") -> "Symtable":
        return Symtable(name, self)
