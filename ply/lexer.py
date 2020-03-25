from ply import lex


class Lexer:
    states = (
        ('expr', 'exclusive'),
    )
    tokens = (
        'BR', 'DASH', 'EXPR', 'VAR', 'SIGN', 'SH', 'UN', 'NL'
    )

    t_ignore = ''
    t_expr_ignore = ''

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, inp):
        return self.lexer.input(inp)

    def token(self):
        return self.lexer.token()

    def t_BR(self, t):
        r"""<"""
        return t

    def t_DASH(self, t):
        r"""-"""
        return t

    def t_expr_VAR(self, t):
        r"""[!a-zA-Z][a-zA-Z\d]{0,15}"""
        return t

    def t_expr_SIGN(self, t):
        r"""[&|^]"""
        return t

    def t_EXPR(self, t):
        r"""[!a-zA-Z][a-zA-Z\d]{0,15}"""
        t.lexer.begin('expr')
        t.type = 'VAR'
        return t

    def t_ANY_SH(self, t):
        r"""\#"""
        t.lexer.begin('INITIAL')
        return t

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += t.value.count('\n')
        t.lexer.begin('INITIAL')
        t.type = 'NL'
        return t

    def t_expr_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += t.value.count('\n')
        t.lexer.begin('INITIAL')
        t.type = 'NL'
        return t

    def t_ANY_UN(self, t):
        r""".+"""
        return t

    def t_ANY_error(self, t):
        print("Illegal character '%s'\n" % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')


if __name__ == '__main__':
    lexer = Lexer()
    while True:
        line = input()
        lexer.input(line)
        for tok in lexer.lexer:
            print(tok)
    # lexer.input(input())
    # for tok in lexer.lexer:
    #     print(tok)
