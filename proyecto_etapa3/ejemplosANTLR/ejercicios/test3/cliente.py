from antlr4 import *
from antlr.TesttresLexer import TesttresLexer
from antlr.TesttresParser  import TesttresParser 
from antlr.TesttresListener import TesttresListener


class GetAllTokens(TesttresListener):     
    tokens = []



def main(input):
    parser = TesttresParser(CommonTokenStream(TesttresLexer(FileStream(input))))

    # El resultado del parsing es un árbol
    tree = parser.prog()
    
    # Definido arriba, hereda de Listener
    listener = GetAllTokens()

    # Esto viene del api de ANTLR
    walker = ParseTreeWalker()

    # El listener recorre el árbol
    walker.walk(listener, tree)

    # Podemos examinar nuestro objeto
    print(listener.tokens)

if __name__ == '__main__':
    main('ejemplo.txt')
