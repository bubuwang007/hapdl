import os
import unittest

from hapdl.compiler.lexer import Lexer
from hapdl.compiler.parser import Parser

class TestParser(unittest.TestCase):

    def test_parser(self):
        lexer = Lexer.from_string("a = 1")
        parser = Parser(lexer)
        for i in parser.lexer.token_get():
            print(i)

if __name__ == "__main__":
    unittest.main()