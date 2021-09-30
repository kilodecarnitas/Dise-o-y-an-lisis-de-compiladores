# Generated from c:\Users\aorti\OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\Neunte teil\Diseño de compiladores\DC - Repositorio del profesor\proyecto_etapa1y2\antlr\Cool.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete generic visitor for a parse tree produced by CoolParser.

class CoolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoolParser#program.
    def visitProgram(self, ctx:CoolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#klass.
    def visitKlass(self, ctx:CoolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#feature.
    def visitFeature(self, ctx:CoolParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#parameter.
    def visitParameter(self, ctx:CoolParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#suma.
    def visitSuma(self, ctx:CoolParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#parens.
    def visitParens(self, ctx:CoolParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#string.
    def visitString(self, ctx:CoolParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#isvoid.
    def visitIsvoid(self, ctx:CoolParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#lt.
    def visitLt(self, ctx:CoolParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#while.
    def visitWhile(self, ctx:CoolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#division.
    def visitDivision(self, ctx:CoolParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#not.
    def visitNot(self, ctx:CoolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#block.
    def visitBlock(self, ctx:CoolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#let.
    def visitLet(self, ctx:CoolParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#newobject.
    def visitNewobject(self, ctx:CoolParser.NewobjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#if.
    def visitIf(self, ctx:CoolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#case.
    def visitCase(self, ctx:CoolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#multiplicacion.
    def visitMultiplicacion(self, ctx:CoolParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#simplecall.
    def visitSimplecall(self, ctx:CoolParser.SimplecallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#invert.
    def visitInvert(self, ctx:CoolParser.InvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#false.
    def visitFalse(self, ctx:CoolParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#int.
    def visitInt(self, ctx:CoolParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#equal.
    def visitEqual(self, ctx:CoolParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#objectCall.
    def visitObjectCall(self, ctx:CoolParser.ObjectCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#true.
    def visitTrue(self, ctx:CoolParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#le.
    def visitLe(self, ctx:CoolParser.LeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Id.
    def visitId(self, ctx:CoolParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#resta.
    def visitResta(self, ctx:CoolParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#assign.
    def visitAssign(self, ctx:CoolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#case_stat.
    def visitCase_stat(self, ctx:CoolParser.Case_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#let_decl.
    def visitLet_decl(self, ctx:CoolParser.Let_declContext):
        return self.visitChildren(ctx)



del CoolParser