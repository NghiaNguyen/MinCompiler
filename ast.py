class AST(object):

  def __init__(self):
    self.children = []

  def addChild(self, child):
    self.children.append(child)

  def getChildren(self):
    return self.children

  def annotate(self):
    for child in self.children:
      child.annotate()

  def codeGenerate(self, buffer):
    for child in self.children:
      child.codeGenerate(self, buffer)

class Prog_AST(AST):
  pass
