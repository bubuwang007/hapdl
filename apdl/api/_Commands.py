from __future__ import annotations
from collections import UserList
from ._Command import Command
from ._Comment import Comment
from ._Processor import Processor

class Commands(UserList[Command|Comment]):
    indent: int = 0

    def append(self, cmd: Command|Processor|Comment|str, comment: str = ""):
        if isinstance(cmd, (Command, Comment)):
            cmd.indent += self.indent
            self.data.append(cmd)
        elif isinstance(cmd, Processor):
            self.data.append(Command(str(cmd.value), self.indent, comment))
        else:
            self.data.append(Command(str(cmd), self.indent, comment))

    def __lshift__(self, other: Command|Processor|Comment|str) -> Commands:
        self.append(other)
        return self

    def indent_up(self):
        self.indent += 1

    def indent_down(self):
        self.indent -= 1

    def add_blank(self):
        self.append(Command(""))

    def add_comment(self, content: str):
        self.append(Comment(content, self.indent))

    def add_block(self, content: str, star_num:int=55, line_length:int=55):
        self.add_blank()
        self.add_comment("*"*star_num)
        start, end, length = 0, 0, 0
        for i in content:
            if ord(i) < 128:
                length += 1
            else:
                length += 2
            if length >= line_length:
                self.add_comment(content[start:end])
                start = end
                length = 0
            end += 1
        else:
            self.add_comment(content[start:])
        self.add_comment("*"*star_num)
        self.add_blank()

    def __str__(self) -> str:
        return "\n".join([str(i) for i in self.data])

    def save(self, filename: str):
        with open(filename, "w", encoding="u8") as f:
            f.write(str(self))

    def extend(self, commands: Commands):
        for i in commands:
            i.indent = self.indent + i.indent
            self.append(i)