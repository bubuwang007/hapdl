from ._TokenInfo import TokenInfo
from ._Token import TokenType
from typing import Any, Generator

class Lexer:

    def __init__(self, string: str):
        self.string = string

    @staticmethod
    def from_string(string: str) -> "Lexer":
        return Lexer(string)

    @staticmethod
    def from_file(file: str) -> "Lexer":
        with open(file, "r", encoding="u8") as f:
            return Lexer(f.read())

    def next_char(self, n: int=1) -> str:
        if self.current + n > len(self.string):
            return None
        else:
            return self.string[self.current+n-1]

    def token_get(self) -> Generator[TokenInfo, None, None]:
        self.current = 0
        self.line = 1
        self.column = 1

        while True:
            self.start = self.current
            self.start_column = self.column
            c = self.next_char()
            if c in [" ", "\t"]:
                self.current += 1
                self.column += 1
                continue
            elif c == "\n":
                self.current += 1
                self.line += 1
                self.column = 1
                continue

            if c is None:
                break

            if c == '#':
                yield self.__get_comment()
                continue



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

    def __get_three_char_symbol(self) -> TokenInfo:
        tok = self.string[self.current:self.current + 3]
        test = TokenType.THREECHAR.get(tok)
        if test is not None:
            token = TokenInfo(test, tok, self.line, self.column, self.end_column)
            self.current += 3
            return token
        else:
            return self.__get_two_char_symbol()
        
    def __get_two_char_symbol(self) -> TokenInfo:
        tok = self.string[self.current:self.current + 2]
        test = TokenType.TWOCHAR.get(tok)
        if test is not None:
            token = TokenInfo(test, tok, self.line, self.column, self.end_column)
            self.current += 2
            return token
        else:
            return self.__get_one_char_symbol()
        
    def __get_one_char_symbol(self) -> TokenInfo:
        tok = self.string[self.current]
        test = TokenType.ONECHAR.get(tok)
        if test is not None:
            token = TokenInfo(test, tok, self.line, self.column, self.end_line, self.end_column)
            self.current += 1
            return token
        else:
            raise ValueError(f"Unknown symbol: {tok}, at line {self.line}, column {self.column}")
