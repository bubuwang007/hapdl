from __future__ import annotations

class Command:
    cmd: str
    indent: int

    def __init__(self, cmd: str, indent: int = 0, comment=""):
        self.cmd = cmd
        self.indent = indent
        self.comment = comment

    def __str__(self) -> str:
        return f"{' '*4*self.indent}{self.cmd}{'' if self.comment == '' else ' ! ' + self.comment}"

    def __iadd__(self, other: Command) -> Command:
        self.cmd += "$" + other.cmd
        self.comment = ""
        return self

    def __add__(self, other: Command) -> Command:
        return Command(self.cmd + "$" + other.cmd, self.indent, None)