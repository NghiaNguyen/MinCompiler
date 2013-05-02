import re
from ast import *

## Tokens ##
ID = r'[a-zA-Z]+'
NUM = r'[0-9]+'
FOR = r'for'
IF = r'if'
TO = r'to'
PRINT = r'print'
STRING = r'\'.*\''
OPS = r'[+-]'
ASSIGN = r'='
EQUAL = r'=='
TOKENS = re.compile('|'.join([ID, NUM, FOR, TO, IF, PRINT, STRING, ASSIGN, EQUAL, OPS]))

def parse(text):
  """
  Our grammar (should be LL(k) grammar):
    prog : stmt* EOF
    stmt : for_stmt | assign_stmt | print_stmt | if_stmt
    for_stmt: FOR ID = NUM to NUM { stmt* }
    if_stmt : IF equal_expression { stmt* }
    equal_expression : ID == (ID|NUM)
    assign_stmt: ID EQUAL expression
    expression: ID | NUM | STRING | ID OP expression
    print_stmt: PRINT expression
  """

  EOF = ""
  tokens = TOKENS.findall(text)
  pos = 0

  def next(k=0):
    pos_k = pos + k
    if pos_k >= len(tokens):
      return EOF
    else:
      return tokens[pos_k]

  def scan(tok=None):
    if tok is not None and not re.match(tok, next()):
        raise SyntaxError
    nonlocal pos
    pos += 1

  def for_stmt():
    raise NotImplementedError

  def assign_stmt():
    raise NotImplementedError

  def if_stmt():
    raise NotImplementedError

  def print_stmt():
    raise NotImplementedError

  def stmt():
    if next() == FOR:
      return for_stmt()
    elif next() == IF:
      return if_stmt()
    elif next() == PRINT:
      return print_stmt()
    elif next() == ID:
      return assign_stmt()

  def prog():
    root = Prog_AST()
    while next():
      root.addChild(stmt())
    return root

  return prog()
