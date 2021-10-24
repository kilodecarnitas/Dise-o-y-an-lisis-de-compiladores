#Diego Ramírez Levy - A01367771
#Omar Robledo Rodríguez - A01338010
#Aldo Fernando Ortiz Mejía -  A01654725

from antlr4 import FileStream, ParseTreeWalker, CommonTokenStream
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser

from declare import Declarations
from typecheck import Typecheck


def main():
  input_file = FileStream('./resources/semantic/input/simplearith.cool')

  lexer = CoolLexer(input_file)
  parser = CoolParser(CommonTokenStream(lexer))
  tree = parser.program()

  walker = ParseTreeWalker()
  typecheck = Typecheck()
  # walker.walk(typecheck, tree)

  declare = Declarations()
  walker.walk(typecheck, tree)
  walker.walk(declare, tree)
  
main()