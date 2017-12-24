from antlr4 import *

from gen.MATLABHeaderLexer import MATLABHeaderLexer
from gen.MATLABHeaderParser import MATLABHeaderParser
from gen.MATLABHeaderParserListener import MATLABHeaderParserListener


def parse(string):
    input_stream = InputStream(string)
    lexer = MATLABHeaderLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MATLABHeaderParser(stream)
    tree = parser.