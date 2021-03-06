
VOID_TYPE = 'void_type'
STRING_TYPE = 'string_type'
NUM_TYPE = 'num_type'
UNKNOWN_TYPE = 'unknown_type'

class StringMapper(object):
  def __init__(self, startAddress):
    self.stringMap = dict()
    self.counter = startAddress

  def addString(self, text):
    if text not in self.stringMap:
      self.stringMap[text] = counter
      self.counter = self.counter + len(text)

  def getAddress(self, text):
    return self.stringMap[text]

class AST(object):

  def __init__(self, children=None, type=VOID_TYPE):
    if children is None:
      self.children = []
    else:
      self.children = children
    self.type = type
    # a global map of constant string addresses across the whole program
    self.stringMapper = StringMapper(10)

  def getType():
    return self.type

  def addChild(self, child):
    self.children.append(child)

  def getChildren(self):
    return self.children

  def annotate(self):
    for child in self.children:
      child.annotate()

  def codeGenerate(self, buffer):
    for child in self.children:
      child.codeGenerate(buffer)

class Prog_AST(AST):

  def generateCode(self):
    buffer = []
    self.codeGenerate(buffer)
    return ''.join(buffer)

class Print_AST(AST):

  def __init__(self, expr):
    AST.__init__(self, [expr])
    self.expr = expr

  def codeGenerate(self, buffer):
    buffer.append('print: ')
    self.expr.codeGenerate(buffer)

class String_AST(AST):

  def __init__(self, text):
    AST.__init__(self, [], STRING_TYPE)
    self.text = text.strip(r"\"|'")
    self.address =

  def codeGenerate(self, buffer):
    buffer.append(self.text)

class Num_AST(AST):

  def __init__(self, num):
    AST.__init__(self, [], NUM_TYPE)
    self.num = num

class Identifier_AST(AST):

  def __init__(self, id):
    AST.__init__(self, [], UNKNOWN_TYPE)
    self.id = id
