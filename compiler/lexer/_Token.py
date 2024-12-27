import enum

class TokenType(enum.Enum):
    SYMBOLS: dict

    NUMBER = 0
    STRING = 1
    KEYWORD = 2
    IDENTIFIER = 3
    NEWLINE = 4

    ELLIPSIS = 5
    SEMICOLON = 6
    COMMA = 7
    COLON = 8
    DOT = 9
    LBRACE = 10
    RBRACE = 11
    LPAR = 12
    RPAR = 13
    LSQB = 14
    RSQB = 15
    SLASH = 16
    MINUSARROW = 17
    EQARROW = 18

    EQ = 19
    NE = 20
    NOT = 21

    PLUS = 22
    MINUS = 23
    STAR = 24
    SLASH = 25
    AT = 26
    PERCENT = 27
    DOUBLESTAR = 28
    DOUBLESLASH = 29
    AMPER = 30
    VBAR = 31
    CIRCUMFLEX = 32

    PLUSEQ = 33
    MINUSEQ = 34
    STAREQ = 35
    SLASHEQ = 36
    ATEQ = 37
    PERCENTEQ = 38
    DOUBLESTAREQ = 39
    DOUBLESLASHEQ = 40
    AMPEREQ = 41
    VBAREQ = 42
    CIRCUMFLEXEQ = 43

    LT = 44
    GT = 45
    LE = 46
    GE = 47

TokenType.SYMBOLS = {
    TokenType.ELLIPSIS: '...',
    TokenType.SEMICOLON: ';',
    TokenType.COMMA: ',',
    TokenType.COLON: ':',
    TokenType.DOT: '.',
    TokenType.LBRACE: '{',
    TokenType.RBRACE: '}',
    TokenType.LPAR: '(',
    TokenType.RPAR: ')',
    TokenType.LSQB: '[',
    TokenType.RSQB: ']',
    TokenType.SLASH: '/',
    TokenType.MINUSARROW: '->',
    TokenType.EQARROW: '=>',
    TokenType.EQ: '=',
    TokenType.NE: '!=',
    TokenType.NOT: '!',
    TokenType.PLUS: '+',
    TokenType.MINUS: '-',
    TokenType.STAR: '*',
    TokenType.SLASH: '/',
    TokenType.AT: '@',
    TokenType.PERCENT: '%',
    TokenType.DOUBLESTAR: '**',
    TokenType.DOUBLESLASH: '//',
    TokenType.AMPER: '&',
    TokenType.VBAR: '|',
    TokenType.CIRCUMFLEX: '^',
    TokenType.PLUSEQ: '+=',
    TokenType.MINUSEQ: '-=',
    TokenType.STAREQ: '*=',
    TokenType.SLASHEQ: '/=',
    TokenType.ATEQ: '@=',
    TokenType.PERCENTEQ: '%=',
    TokenType.DOUBLESTAREQ: '**=',
    TokenType.DOUBLESLASHEQ: '//=',
    TokenType.AMPEREQ: '&=',
    TokenType.VBAREQ: '|=',
    TokenType.CIRCUMFLEXEQ: '^=',

    TokenType.LT: '<',
    TokenType.GT: '>',
    TokenType.LE: '<=',
    TokenType.GE: '>='
}