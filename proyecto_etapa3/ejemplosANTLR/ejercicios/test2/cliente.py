from antlr4 import *
from antlr.TestdosLexer import TestdosLexer 
from antlr.TestdosParser  import TestdosParser 
from antlr.TestdosListener import TestdosListener

class GetAllTokens(TestdosListener):     
    tokens = []

    def exitToken(self, ctx: TestdosParser.TokenContext):
        self.tokens.append(ctx.getText())


def main(input):
    parser = TestdosParser(CommonTokenStream(TestdosLexer(FileStream(input))))

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
