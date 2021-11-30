import sys
from typing import Type
import unittest

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from structure import *
from tree import TreePrinter
from myexceptions import *
from etapa1Listener import Listener
from klassListener import KlassListener
from typecheck import Typecheck
from methodListener import  MethodListener

def parseAndCompare(caseName):
    parser = CoolParser(CommonTokenStream(CoolLexer(FileStream("../resources/semantic/input/%s.cool" % caseName))))
    tree = parser.program()
    walker = ParseTreeWalker()

    walker.walk(KlassListener(), tree)
    walker.walk(Typecheck(), tree)
    walker.walk(Listener(), tree)

    treePrinter = TreePrinter(type)
    walker.walk(treePrinter, tree)
    output = treePrinter.getOutput()

    expected = output.split('\n')
    with open('expected/semantic/%s.txt' % caseName) as f:
        for line1, line2 in zip(f, expected):
            if line1[:-1] != line2:
                print ("Diferencia!!! [%s]-[%s]" % (line1, line2))
                return False
    return True 

class BaseTest(unittest.TestCase):
    def setUp(self): 
        self.walker = ParseTreeWalker()

cases = ['simplearith',
        'basicclassestree',
        'expressionblock',
        'objectdispatchabort',
        'initwithself',
        'compare',
        'comparisons',
        'cycleinmethods',
        'letnoinit',
        'forwardinherits',
        'letinit',
        'newselftype',
        'basic',
        'overridingmethod',
        'letshadows',
        'neg',
        'methodcallsitself',
        'overriderenamearg',
        'isvoid',
        'overridingmethod3',
        'inheritsObject',
        'scopes',
        'letselftype',
        'if',
        'methodnameclash',
        'trickyatdispatch',
        'stringtest',
        'overridingmethod2',
        'simplecase',
        'assignment',
        'subtypemethodreturn',
        'dispatch',
        'io',
        'staticdispatch',
        'classes',
        'hairyscary',
        'cells',
        'list',
        ]

if __name__ == '__main__':
    methods = {}
    i = 0
    for caso in cases:
        methods['test%d' % i] = lambda self: self.assertTrue(parseAndCompare(caso))
        i = i+1
    CoolTests = type('CoolTests', (BaseTest,), methods)
    unittest.main()