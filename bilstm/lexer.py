import ply.lex as lex

class CPPLexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self, input_string):
        self.lexer.input(input_string)
        tokens_list = []
        while True:
            tok = self.lexer.token()
            if not tok: break
            tokens_list.append(tok)
        return [(token.type, token.value) for token in tokens_list]

    tokens = [
        'IDENTIFIER', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMENT', 'LT', 'GT',
        'LE', 'GE', 'EQ', 'NE', 'AND', 'OR', 'NOT', 'BITWISE_AND', 'BITWISE_OR', 'BITWISE_XOR',
        'BITWISE_NOT', 'LSHIFT', 'RSHIFT', 'PLUSPLUS', 'MINUSMINUS', 'ARROW', 'PERIOD',
        'COMMA', 'COLON', 'QMARK', 'STRING_LITERAL', 'CHAR_LITERAL', 'HASH'
    ] + [
        # C++ keywords
        'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO',
        'DOUBLE', 'ELSE', 'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO', 'IF', 'INLINE',
        'INT', 'LONG', 'REGISTER', 'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 'STATIC',
        'STRUCT', 'SWITCH', 'TYPEDEF', 'UNION', 'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE'
    ]

    # Regular expressions for tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r'='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_SEMICOLON = r';'
    t_LT = r'<'
    t_GT = r'>'
    t_LE = r'<='
    t_GE = r'>='
    t_EQ = r'=='
    t_NE = r'!='
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_NOT = r'!'
    t_BITWISE_AND = r'&'
    t_BITWISE_OR = r'\|'
    t_BITWISE_XOR = r'\^'
    t_BITWISE_NOT = r'~'
    t_LSHIFT = r'<<'
    t_RSHIFT = r'>>'
    t_PLUSPLUS = r'\+\+'
    t_MINUSMINUS = r'--'
    t_ARROW = r'->'
    t_PERIOD = r'\.'
    t_COMMA = r','
    t_COLON = r':'
    t_QMARK = r'\?'
    t_HASH = r'\#'
    # Ignored whitespace tokens: space, tab
    t_ignore = ' \t'

    # Keyword map
    keyword_map = {
        'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE', 'char': 'CHAR',
        'const': 'CONST', 'continue': 'CONTINUE', 'default': 'DEFAULT', 'do': 'DO',
        'double': 'DOUBLE', 'else': 'ELSE', 'enum': 'ENUM', 'extern': 'EXTERN',
        'float': 'FLOAT', 'for': 'FOR', 'goto': 'GOTO', 'if': 'IF', 'inline': 'INLINE',
        'int': 'INT', 'long': 'LONG', 'register': 'REGISTER', 'return': 'RETURN',
        'short': 'SHORT', 'signed': 'SIGNED', 'sizeof': 'SIZEOF', 'static': 'STATIC',
        'struct': 'STRUCT', 'switch': 'SWITCH', 'typedef': 'TYPEDEF', 'union': 'UNION',
        'unsigned': 'UNSIGNED', 'void': 'VOID', 'volatile': 'VOLATILE', 'while': 'WHILE'
    }

    def t_IDENTIFIER(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.keyword_map.get(t.value, 'IDENTIFIER')  # Check for keywords
        return t

    def t_STRING_LITERAL(self, t):
        r'\"([^\\\n]|(\\.))*?\"'
        return t

    def t_CHAR_LITERAL(self, t):
        r'\'([^\\\n]|(\\.))*?\''
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_COMMENT(self, t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        pass 

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)
