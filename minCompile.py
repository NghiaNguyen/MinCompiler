#!/usr/bin/python3
import sys, re

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
  Our grammar:
    prog : stmt* EOF
    stmt : for_stmt | assign_stmt | print_stmt | if_stmt
    for_stmt: FOR ID = NUM to NUM { stmt* }
    if_stmt : IF equal_expression { stmt* }
    equal_expression : ID == (ID|NUM)
    assign_stmt: ID EQUAL expression
    expression: ID|NUM|STRING|ID OP expression
    print_stmt: PRINT (ID|NUM|STRING)
  """

  EOF = ""
  tokens = TOKENS.findall(text)
  pos = 0

  def next():
    if pos >= len(tokens):
      return EOF
    else:
      return tokens[pos]

  def scan(tok=None):
    if tok is not None and not re.match(tok, next()):
        raise SyntaxError
    nonlocal pos
    pos += 1

  def for_stmt():
    scan(FOR)

  def stmt():
    if next() == FOR:
      for_stmt()

  def prog():
    while next():
      stmt()

  return prog()

#TODO: implement me
class AST(object):
  pass

def main(argv=None):
  if argv is None:
    argv = sys.argv
  if len(argv) != 3:
    print("Usage: <inputFile> <outputFile>")
  inputName = argv[1]
  outputName = argv[2]
  inFile = open(inputName, 'r')
  sourceCode = inFile.read()
  try:
    tree = parse(sourceCode)
  except SyntaxError:
    print("Syntax error.  Rest of tokens:", tokens[pos:])
    sys.exit(1)


if __name__ == "__main__":
  sys.exit(main())
