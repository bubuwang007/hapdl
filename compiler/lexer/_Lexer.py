import os
from ._TokenInfo import TokenInfo
from ._Token import TokenType
from ._Keywords import Keywords
from typing import Generator

class Lexer:

    def __init__(self, string: str, file: str=None):
        self.file = os.path.abspath(file) if file is not None else "<string>"
        self.string = string

    @staticmethod
    def from_string(string: str) -> "Lexer":
        return Lexer(string)

    @staticmethod
    def from_file(file: str) -> "Lexer":
        with open(file, "r", encoding="u8") as f:
            return Lexer(f.read(), file)

    def next_char(self, n: int=1) -> str:
        if self.current + n > len(self.string):
            return None
        else:
            return self.string[self.current+n-1]

    def __posinfo(self) -> str:
        return f"File \"{self.file}\", line {self.line}, col {self.start_column}"

    @staticmethod
    def is_potential_identifier_start(c: str) -> bool:
        return c.isalpha() or c == "_"
    
    @staticmethod
    def is_potential_identifier(c: str) -> bool:
        return c.isalnum() or c == "_"

    def token_get(self) -> Generator[TokenInfo, None, None]:
        self.current = 0
        self.line = 1
        self.column = 1

        while True:
            self.start = self.current
            self.start_column = self.column
            c = self.next_char()

            if c is None:
                break

            if c in [" ", "\t"]:
                self.current += 1
                self.column += 1
                continue
            elif c == "\n":
                self.current += 1
                self.line += 1
                self.column = 1
                continue

            if c == '#':
                yield self.__get_comment()
                continue
            
            if c == '"':
                yield self.__get_string()
                continue

            if self.is_potential_identifier_start(c):
                yield self.__get_identifier_or_keywords()
                continue

            if c.isdigit():
                yield self.__get_number()
                continue

            tok = self.__get_symbol(c)
            if tok is not None:
                yield tok
                continue

            raise Exception(f"Invalid character at {self.__posinfo()}: {c}")
            self.current += 1
            self.column += 1

    def __get_comment(self) -> TokenInfo:
        self.current += 1
        self.column += 1
        while True:
            c = self.next_char()
            if c is None or c == "\n":
                return TokenInfo(TokenType.COMMENT, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            self.current += 1
            self.column += 1

    def __get_string(self) -> TokenInfo:
        self.current += 1
        self.column += 1
        s = []
        while True:
            c = self.next_char()
            if c is None or c == "\n":
                raise Exception(f"Unterminated string at {self.__posinfo()}")
            elif c == "\\":
                self.current += 1
                self.column += 1
                t = self.next_char()
                match t:
                    case "n":
                        s.append("\n")
                    case "t":
                        s.append("\t")
                    case "\\":
                        s.append("\\")
                    case '"':
                        s.append('\"')
                    case "0":
                        s.append("\0")
                    case "r":
                        s.append("\r")
                    case "b":
                        s.append("\b")
                    case "f":
                        s.append("\f")
                    case "v":
                        s.append("\v")
                    case "a":
                        s.append("\a")
                    case _:
                        self.start_column = self.column
                        raise Exception(f"Invalid escape sequence at {self.__posinfo()}: \\{t}")
            elif c == '"':
                self.current += 1
                self.column += 1
                return TokenInfo(TokenType.STRING, "".join(s), 
                         self.line, self.start_column, self.column-1)
            else:
                s.append(c)
            self.current += 1
            self.column += 1

    def __get_number(self) -> TokenInfo:
        return self.__get_integer()

    def __get_integer(self) -> TokenInfo:

        while True:
            c = self.next_char()
            if c == '.':
                self.current += 1
                self.column += 1
                return self.__get_float()
            elif c == 'e' or c == 'E':
                self.current += 1
                self.column += 1
                return self.__get_scientific()
            elif c == 'j' or c == 'J':
                self.current += 1
                self.column += 1
                return TokenInfo(TokenType.IMAGE, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            elif c is None or not c.isdigit():
                return TokenInfo(TokenType.INTEGER, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            elif c.isdigit():
                self.current += 1
                self.column += 1

    def __get_float(self) -> TokenInfo:
        while True:
            c = self.next_char()
            if c == 'e' or c == 'E':
                self.current += 1
                self.column += 1
                return self.__get_scientific()
            elif c == 'j' or c == 'J':
                self.current += 1
                self.column += 1
                return TokenInfo(TokenType.IMAGE, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            elif c is None or not c.isdigit():
                return TokenInfo(TokenType.FLOAT, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            elif c.isdigit():
                self.current += 1
                self.column += 1

    def __get_scientific(self) -> TokenInfo:
        c = self.next_char()
        if c == '+' or c == '-':
            self.current += 1
            self.column += 1
        while True:
            c = self.next_char()
            if c == 'j' or c == 'J':
                self.current += 1
                self.column += 1
                return TokenInfo(TokenType.IMAGE, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            elif c is None or not c.isdigit():
                return TokenInfo(TokenType.FLOAT, self.string[self.start:self.current], 
                         self.line, self.start_column, self.column-1)
            elif c.isdigit():
                self.current += 1
                self.column += 1

    def __get_identifier_or_keywords(self) -> TokenInfo:
        while True:
            c = self.next_char()
            if c is None or not self.is_potential_identifier(c):
                tok = self.string[self.start:self.current]
                kw = Keywords.get(tok)
                if kw is not None:
                    return TokenInfo(kw, tok, self.line, self.start_column, self.column-1)
                else:
                    return TokenInfo(TokenType.IDENTIFIER, tok, self.line, self.start_column, self.column-1)
            self.current += 1
            self.column += 1
      
    def __get_symbol(self, c: str) -> TokenInfo:
        return self.__get_three_char_symbol(c)

    def __get_three_char_symbol(self, c1: str) -> TokenInfo:
        c2 = self.next_char(2)
        c3 = self.next_char(3)
        tok = TokenType.get_three_char_symbol(c1, c2, c3)
        if tok is not None:
            self.current += 3
            self.column += 3
            return TokenInfo(tok, tok.value, self.line, self.start_column, self.column-1)
        else:
            return self.__get_two_char_symbol(c1, c2)

    def __get_two_char_symbol(self, c1: str, c2: str) -> TokenInfo:
        tok = TokenType.get_two_char_symbol(c1, c2)
        if tok is not None:
            self.current += 2
            self.column += 2
            return TokenInfo(tok, tok.value, self.line, self.start_column, self.column-1)
        else:
            return self.__get_one_char_symbol(c1)
        
    def __get_one_char_symbol(self, c1: str) -> TokenInfo:
        tok = TokenType.get_one_char_symbol(c1)
        if tok is not None:
            self.current += 1
            self.column += 1
            return TokenInfo(tok, tok.value, self.line, self.start_column, self.column-1)
        else:
            return None
