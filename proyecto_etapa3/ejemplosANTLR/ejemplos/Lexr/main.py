import sys
from antlr4 import *
from LexrLexer import LexrLexer
from LexrParser import LexrParser
from LexrListener import LexrListener

class treePrinter(LexrListener):
    def enterEveryRule(self, ctx):
        #import pdb;pdb.set_trace()
        print("{}<{}>".format(ctx.__class__, ctx.getText()))

def main(argv):
    parser = LexrParser(CommonTokenStream(LexrLexer(FileStream('input.txt'))))
    tree = parser.secuencia_de_cosas()
    testListener = treePrinter()

    walker = ParseTreeWalker()
    walker.walk(testListener, tree)

if __name__ == '__main__':
    main(sys.argv)

