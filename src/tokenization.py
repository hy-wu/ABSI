import re
from numba import jit
from tqdm import tqdm

# Define token patterns
token_patterns = [
    ('S', r'\s+'),
    ('NEWLINE', r'\r+|\n+|(\r\n)+'),
    ('COMMENT', r'#.*'),
    ('L_PAREN', r'\('),
    ('R_PAREN', r'\)'),
    ('L_BRACKET', r'\['),
    ('R_BRACKET', r'\]'),
    ('L_BRACE', r'\{'),
    ('R_BRACE', r'\}'),
    ('COMMA', r','),
    ('SEMICOLON', r';'),
    
    ('DEFAULT', r'\.\.\.'),
    ('RETURN', r'>>>'),
    ('IMPORT', r'>>'),
    ('YIELD', r'->>'),
    ('BREAK', r'->\|'),
    ('CONTINUE', r'->>'),
    ('RAISE', r'!!!'),  # or r'->!'
    
    ('DOT', r'\.'),
    ('COLON', r':'),
    ('QUESTION', r'\?'),
    ('AT', r'@'),
    
    ('TRUE', r'_\+'),
    ('FALSE', r'_\-'),
    ('NIL', r'_~'),
    
    ('IS', r'==='),
    ('EQ', r'=='),
    
    
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MUL', r'\*'),
    ('DIV', r'/'),
    ('ASSIGN', r'='),
    ('LT', r'<'),
    ('GT', r'>'),
    ('LTE', r'<='),
    ('GTE', r'>='),
    ('NE', r'!='),
    ('BIT_NOT', r'~~'),
    ('BIT_AND', r'&&'),
    ('BIT_OR', r'\|\|'),
    ('BIT_XOR', r'\^\^'),
    ('AND', r'&'),
    ('OR', r'\|'),
    ('EXPONENT', r'\^'),
    
    ('TILDE', r'~'),
    
    ('NOT', r'!'),
    
    ('NUMBER', r'\d+'),
    ('STRING', r'"[^"]*"'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
]
regexes = [(re.compile(pattern), token_type) for token_type, pattern in token_patterns]

# Tokenizer
# @jit(nopython=True)
def tokenize(source_code):
    tokens = []
    # while source_code:
    #     match = None
    #     for token_type, pattern in token_patterns:
    #         try:
    #             regex = re.compile(pattern)
    #         except:
    #             raise SyntaxError(f"Invalid regex pattern: {pattern}")
    #         match = regex.match(source_code)
    #         if match:
    #             value = match.group(0)
    #             tokens.append((token_type, value))
    #             source_code = source_code[match.end():]
    #             break
    #     if not match:
    #         raise SyntaxError(f"Unexpected character: {source_code[0]}")
    # for line in tqdm(source_code.splitlines()):
    for line in source_code.splitlines():
        while line:
            match = None
            for regex, token_type in regexes:
                match = regex.match(line)
                if match:
                    value = match.group(0)
                    tokens.append((token_type, value))
                    line = line[match.end():]
                    break
            if not match:
                raise SyntaxError(f"Unexpected character: {line[0]} in line: {line}")
    
    return tokens
