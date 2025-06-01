import re

token_spec = [
    ('COMMENT', r'#.*'),
    ('SELECT', r'\bselect\b'),
    ('WHERE', r'\bwhere\b'),
    ('LIMIT', r'\blimit\b'),
    ('VAR', r'\?[A-Za-z]\w*'),
    ('STRING', r'"[^"]*"'),
    ('IRI', r'[A-Za-z]+:[\w]+'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('DOT', r'\.'),
    ('NUMBER', r'\d+'),
    ('SKIP', r'\s+'),
    ('MISMATCH', r'.')
]

tok_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_spec), re.IGNORECASE)

def tokenize(code):
    for mo in tok_regex.finditer(code):
        tipo = mo.lastgroup
        valor = mo.group()
        if tipo == 'SKIP':
            continue
        elif tipo == 'MISMATCH':
            yield ('ERRO', valor)
        else:
            yield (tipo, valor)

with open('in', 'r', encoding='utf-8') as f:
    codigo = f.read()

tokens = list(tokenize(codigo))

with open('out', 'w', encoding='utf-8') as f:
    for t in tokens:
        f.write(f'{t[0]}: {t[1]}\n')
