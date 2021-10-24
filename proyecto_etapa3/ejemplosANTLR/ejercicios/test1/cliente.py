from antlr4 import *
from antlr.TestunoLexer import TestunoLexer
from antlr.TestunoParser  import TestunoParser 
from antlr.TestunoListener import TestunoListener


class GetAllTokens(TestunoListener):     
    tokens = []

    def exitToken(self, ctx: TestunoParser.TokenContext):
        self.tokens.append(ctx.getText())


def main(input):
    parser = TestunoParser(CommonTokenStream(TestunoLexer(FileStream(input))))

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
