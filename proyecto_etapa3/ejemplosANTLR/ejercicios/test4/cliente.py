from antlr4 import *
from antlr.TestcuatroLexer import TestcuatroLexer
from antlr.TestcuatroParser  import TestcuatroParser 
from antlr.TestcuatroListener import TestcuatroListener


class GetAllTokens(TestcuatroListener):     
    tokens = []



def main(input):
    parser = TestcuatroParser(CommonTokenStream(TestcuatroLexer(FileStream(input))))

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
