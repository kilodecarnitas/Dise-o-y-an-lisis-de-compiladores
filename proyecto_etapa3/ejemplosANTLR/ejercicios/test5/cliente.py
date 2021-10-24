from antlr4 import *
from antlr.SmallLexer import SmallLexer
from antlr.SmallParser import SmallParser 
from antlr.SmallListener import SmallListener
import sys

'''
Implementar este listener que vaya guardando los identificadores y números y su conteo en sendos diccionarios, al final se imprime el conteo

'''
class Counter(SmallListener):
    identifiers = {}
    numbers = {}

def main(input):
    parser = SmallParser(CommonTokenStream(SmallLexer(FileStream(input))))
    tree = parser.program()

    walker = ParseTreeWalker()
    counter = Counter()

    walker.walk(counter, tree)

    print(counter.identifiers)
    print(counter.numbers)

if __name__ == '__main__':
    main("test1.txt")
