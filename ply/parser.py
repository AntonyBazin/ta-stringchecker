import ply.yacc as yacc
from lexer import Lexer
from ply.lex import LexError


class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self._lexer = Lexer()
        self._parser = yacc.yacc(module=self)

    def check_string(self, target):
        try:
            return self._parser.parse(target)
        except LexError:
            pass
            print('LexError')

    def p_begin(self, p):
        """begin : BR DASH VAR exp SH NL"""
        p[0] = p[4]
        p[0][p[3]] = 1 if p[3] not in p[0].keys() else p[0][p[3]] + 1

    def p_expr_rec(self, p):
        """exp : SIGN VAR exp"""
        p[0] = {p[2]: 1}

        for i in p[3].items():
            p[0][i[0]] = i[1] if i[0] not in p[0].keys() else p[0][i[0]] + i[1]

    def p_expr_empty(self, p):
        """exp : """
        p[0] = {}

    def p_error(self, p):
        pass


if __name__ == '__main__':
    while True:
        parser = Parser()
        print(parser.check_string(input()))
    # parser = Parser()
    # with open('data0.txt', 'r') as dt:
    #     for line in dt:
    #         print(parser.check_string(line))
