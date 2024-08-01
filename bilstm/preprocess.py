import json
import re
from pygments import lex
from pygments.lexers import CppLexer

from constants import ENCODING_TABLE

def remove_unnecessary_elements(code: str) -> str:
    # Remove comments
    code = re.sub(r'//.*?\n', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove newlines, tabs, and extra spaces
    code = re.sub(r'\s+', ' ', code).strip()
    return code

def tokenize_source_code(code: str) -> list:
    lexer = CppLexer()
    tokens = lex(code, lexer)
    token_list = []
    for token in tokens:
        _, token_value = token
        if token_value != ' ':
            token_list.append(token_value)
    return token_list

def encode_tokens(tokens: list) -> list:
    encoded_ids = []
    for token in tokens:
        if token == ' ': continue
        encoded_ids.append(ENCODING_TABLE.get(token, -1))
    return encoded_ids

print(tokenize_source_code("#include <iostream> #include <vector> #include <math.h> using namespace std; int findMaxArraySameNum(vector<int> &v1, vector<int> &v2) { int res; int i = 0, j = 0; while (i < v1.size() && j < v2.size()) { if (v1[i] == v2[j]) { res = v1[i]; i++; j++; } else { if (v1[i] > v2[j]) { j++; } else { i++; } } } return res; } vector<int> divisorNum(int n) { vector<int> res; for (int i = 1; i <= n; i++) { if(n % i == 0) { res.push_back(i); } } return res; } int findMaxCommondivisor(int a, int b) { vector<int> v1 = divisorNum(a); vector<int> v2 = divisorNum(b); int res = findMaxArraySameNum(v1, v2); return res; } int main() { int a, b; cin >> a >> b; cout << findMaxCommondivisor(a, b); }"))