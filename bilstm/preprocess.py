import json
import re
from lexer import *

from constants import ENCODING_TABLE

def remove_unnecessary_elements(code: str) -> str:
    # Remove comments
    code = re.sub(r'//.*?\n', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove newlines, tabs, and extra spaces
    code = re.sub(r'\s+', ' ', code).strip()
    return code

def tokenize_source_code(code: str) -> list:
    lexer = CPPLexer()
    tokens = lexer.tokenize(code)
    return tokens

def encode_tokens(tokens: list) -> list:
    encoded_ids = []
    for token in tokens:
        encoded_ids.append(ENCODING_TABLE.get(token[1], -1))
    for i in range(0, len(encoded_ids)):
        print(f'token: {tokens[i][1]}, id: {encoded_ids[i]}')
    return encoded_ids

code1 = '''
#include <iostream> 
using namespace std; 
int gcd(int a, int b) { 
    while (b != 0) { 
        int temp = b;
        b = a % b; 
        a = temp;
    } 
    return a; 
} 
int main() { 
    int a, b; 
    cin >> a >> b; 
    cout << gcd(a, b) << endl; 
    return 0; 
}
'''

tokens = tokenize_source_code(code1)
encoded_ids = encode_tokens(tokens)

# for x in encoded_ids:
#     print(x)

# code2 = '#include <iostream> using namespace std; int gcd(int a, int b) { while (b != 0) { int temp = b; b = a % b; a = temp; } return a; } int main() { int a, b; cin >> a >> b; cout << gcd(a, b) << endl; return 0; }'
