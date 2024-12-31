import os
import unittest
from hapdl.compiler.lexer import Lexer

class TestLexer(unittest.TestCase):

    def test_is_potential_identifier_start(self):
        tests = {
            "a": True,
            "A": True,
            "_": True,
            "1": False,
            " ": False,
            "\n": False,
            "\t": False,
            "*": False,
            "(": False,
            ")": False,
            "[": False,
            "]": False,
            "{": False,
            "}": False,
            "黄": True,
            "$": False,
        }
        for k, v in tests.items():
            self.assertEqual(Lexer.is_potential_identifier_start(k), v)

    def test_is_potential_identifier(self):
        tests = {
            "a": True,
            "A": True,
            "_": True,
            "1": True,
            "2": True,
            "9": True,
            " ": False,
            "\n": False,
            "\t": False,
            "*": False,
            "(": False,
            ")": False,
            "[": False,
            "]": False,
            "{": False,
            "}": False,
            "黄": True,
            "$": False,
        }
        for k, v in tests.items():
            self.assertEqual(Lexer.is_potential_identifier(k), v)

    def test_comment(self):
        lexer = Lexer.from_string("# this is a comment\n")
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "comment")
        self.assertEqual(tok.value, "# this is a comment")

    def test_identifier(self):
        lexer = Lexer.from_string("_a b_ c1")
        tokenizer = lexer.token_get()
        tok = next(tokenizer)
        self.assertEqual(tok.type.value, "id")
        self.assertEqual(tok.value, "_a")
        tok = next(tokenizer)
        self.assertEqual(tok.type.value, "id")
        self.assertEqual(tok.value, "b_")
        tok = next(tokenizer)
        self.assertEqual(tok.type.value, "id")
        self.assertEqual(tok.value, "c1")

    def test_string(self):
        lexer = Lexer.from_string('"this is a string"')
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "str")
        self.assertEqual(tok.value, 'this is a string')

        lexer = Lexer.from_string(r'"this is a \tstring\n"')
        tok = next(lexer.token_get())
        self.assertEqual(tok.type.value, "str")
        self.assertEqual(tok.value, 'this is a \tstring\n')

    def test_symbol(self):
        lexer = Lexer.from_string("...;,:.{}()[]->=>=!=!+*-/@%**//&|^<><=>=>=<=<=")
        res = ['...', ';', ',', ':', '.', '{', '}', 
               '(', ')', '[', ']', '->', '=>', '=',
               '!=', '!', '+', '*', '-', '/', '@', 
               '%', '**', '//', '&', '|', '^', '<', 
               '>', '<=', '>=', '>=', '<=', '<=']
        tokenizer = lexer.token_get()
        for r in res:
            tok = next(tokenizer)
            self.assertEqual(tok.type.value, r)
            self.assertEqual(tok.value, r)

    def test_lexer(self):
        p = os.path.abspath('./test.hapdl')
        lexer = Lexer.from_file(p)
        count = 0
        for tok in lexer.token_get():
            print(tok)
            count += 1


if __name__ == '__main__':
    unittest.main()
