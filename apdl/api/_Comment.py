
class Comment:
    content: str
    indent: int

    def __init__(self, content: str, indent: int = 0):
        self.content = content
        self.indent = indent

    def __str__(self) -> str:
        return " "*4*self.indent + f"! {self.content}"