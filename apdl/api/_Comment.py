
class Comment:
    content: str
    level: int

    def __init__(self, content: str, level: int = 0):
        self.content = content
        self.level = level

    def __str__(self) -> str:
        return " "*4*self.level + f"! {self.content}"