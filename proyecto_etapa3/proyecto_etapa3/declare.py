from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from myexceptions import *


class Declarations(CoolListener):
  idTable = {}
  inClass = False
  hasMain = False
  inMain = False
  primitiveNames = {'Int', 'String', 'Bool', 'Object', 'SELF_TYPE'}
  classname = ""
  letTable = {'self'}

  def enterProgram(self, ctx:CoolParser.ProgramContext):
    print(ctx.typesTable)