#!/usr/bin/python3
import sys
from parser import parse

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
