import re
from ast import *

## Tokens ##
IDENTIFIER = r'[a-zA-Z]+'
NUM = r'[0-9]+'
FOR = r'for'
IF = r'if'
TO = r'to'
PRINT = r'print'
STRING = r'\'.*\'|\".*\"'
OPS = r'[+-]'
ASSIGN = r'='
EQUAL = r'=='
TOKENS = re.compile('|'.join([IDENTIFIER, NUM, FOR, TO, IF, PRINT, STRING, ASSIGN, EQUAL, OPS]))

def parse(text):
  """
  Our grammar (should be LL(k) grammar):
    prog : stmt* EOF
    stmt : for_stmt | assign_stmt | print_stmt | if_stmt
    for_stmt: FOR IDENTIFIER = NUM to NUM { stmt* }
    if_stmt : IF equal_expression { stmt* }
    equal_expression : IDENTIFIER == (IDENTIFIER|NUM)
    assign_stmt: IDENTIFIER EQUAL expression
    expression: atom | atom OPS expression
    atom : IDENTIFIER | STRING | NUM
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

  def isNext(tok, k=0):
    return re.match(tok, next(k))

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
    scan(PRINT)
    return Print_AST(expression())

  def expression():
    #TODO: handle the case with OP
    return atom()

  def atom():
    if isNext(IDENTIFIER):
      print("identifier")
      return Identifier_AST(scan(IDENTIFIER))
    elif isNext(STRING):
      return String_AST(scan(STRING))
    elif isNext(NUM):
      return Num_AST(scan(NUM))
    else:
      raise SyntaxError

  def stmt():
    if isNext(FOR):
      return for_stmt()
    elif isNext(IF):
      return if_stmt()
    elif isNext(PRINT):
      return print_stmt()
    elif isNext(IDENTIFIER):
      return assign_stmt()

  def prog():
    root = Prog_AST()
    while next():
      root.addChild(stmt())
    return root

  return prog()
