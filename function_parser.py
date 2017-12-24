from antlr4 import *

from gen.MATLABLexer import MATLABLexer
from gen.MATLABParser import MATLABParser
from gen.MATLABParserListener import MATLABParserListener


class FunctionDeclarationListener(MATLABParserListener):
    def __init__(self, tokens):
        self.list_function = []
        # For comment tokens
        self.tokens = tokens

    def enterFunctionDecl(self, ctx):
        if ctx.partialFunctionDecl().outArgs() is not None:
            if isinstance(ctx.partialFunctionDecl().outArgs().ID(), list):
                outArgs = [x.getText() for x in ctx.partialFunctionDecl().outArgs().ID()]
            else:
                outArgs = ctx.partialFunctionDecl().outArgs().ID().getText()
        else:
            outArgs = None

        if ctx.partialFunctionDecl().inArgs() is not None:
            if isinstance(ctx.partialFunctionDecl().inArgs().ID(), list):
                inArgs = [x.getText() for x in ctx.partialFunctionDecl().inArgs().ID()]
            else:
                inArgs = ctx.partialFunctionDecl().inArgs().ID().getText()
        else:
            inArgs = None

        fcn_names = ctx.partialFunctionDecl().ID().getText()

        comment_tokens = self.tokens.getHiddenTokensToLeft(ctx.partialFunctionDecl().endStat().stop.tokenIndex)
        if comment_tokens is not None:
            comment = [token.text for token in self.tokens.getHiddenTokensToLeft(ctx.partialFunctionDecl().endStat().stop.tokenIndex)]
        else:
            comment = None

        self.list_function.append({'name':fcn_names, 'input': inArgs, 'output':outArgs,'start_line':ctx.start.line, 'start_indent':ctx.start.column, 'comment': comment})


def parse(filename):
    # TODO use InputStream instead of FileStream for string parsing
    input_stream = FileStream(filename)
    lexer = MATLABLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MATLABParser(stream)
    tree = parser.fileDecl()
    fcn_listener = FunctionDeclarationListener(stream)
    walker = ParseTreeWalker()
    walker.walk(fcn_listener, tree)
    return {'filename':filename, 'functions': fcn_listener.list_function}
