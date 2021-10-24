import sys
from antlr.CoolLexer import *
from antlr.CoolParser import *
from antlr.CoolListener import *
from java.JavaLexer import *
from java.JavaParser import *
from java.JavaParserListener import *

from antlr4 import *

class Printer(JavaParserListener):
    in_class = False
    in_method = False
    type = ''

    def enterVariableDeclaratorId(self, ctx: JavaParser.VariableDeclaratorIdContext):
        print(ctx.IDENTIFIER())

    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        self.in_class = True
        print('\n  * * Class * * \n -------------- \n - Name --> ' + ctx.IDENTIFIER().getText() + '\n')
    
    def exitClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        self.in_class = False
    
    def enterFieldDeclaration(self, ctx: JavaParser.FieldDeclarationContext):
        print('\n  * * Attribute * * \n ------------------')
    
    def enterTypeType(self, ctx: JavaParser.TypeTypeContext):
        self.type = ctx.getText()

    def enterVariableDeclaratorId(self, ctx: JavaParser.VariableDeclaratorIdContext):
        if(self.in_class and not self.in_method):
           print(' - Attribute --> ' + ctx.IDENTIFIER().getText() + '\n   - Type --> ' + self.type)
        if(self.in_class and self.in_method):
            print(' - Parameter --> ' + ctx.IDENTIFIER().getText() + '\n   - Type --> ' + self.type)
    
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.in_method = True
        print('\n  * * Method * * \n ---------------' + '\n - Name --> ' + ctx.IDENTIFIER().getText() + '\n - Return Type --> ' + ctx.getChild(0).getText())

    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.in_method = False

''' class Printer(CoolListener):
   def exitEveryRule(self, ctx: ParserRuleContext):
       print("<{}>".format(ctx.getText()))

       return super().exitEveryRule(ctx) '''

def main():
    parser = JavaParser(CommonTokenStream(JavaLexer(FileStream("test.java"))))
    tree = parser.compilationUnit()
    printer = Printer()

    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
