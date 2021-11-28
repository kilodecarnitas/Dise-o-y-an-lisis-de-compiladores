#Diego Ramírez Levy - A01367771
#Omar Robledo Rodríguez - A01338010
#Aldo Fernando Ortiz Mejía -  A01654725

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser

from declare import Declarations
from typecheck import Typecheck
from letListener import Listener


def main(file):
  parser = CoolParser(CommonTokenStream(CoolLexer(FileStream(file))))
  tree = parser.program()

  walker = ParseTreeWalker()
  letchecker = Listener()
  walker.walk(letchecker, tree)
  
if __name__ == '__main__':
    main("../resources/semantic/input/letself.cool")