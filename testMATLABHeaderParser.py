from antlr4 import *
from gen.MATLABHeaderLexer import MATLABHeaderLexer
from gen.MATLABHeaderParser import MATLABHeaderParser

if __name__ == '__main__':
    string = '''%FCN1 - ONELINEDESCRIPTION
%MOREDESCRIPTION
%
% Syntax: [outputArg1] = fcn1(inputArg1)
%
% Inputs:
%    inputArg1 [TYPE] - DESCRIPTION tesé
% 
% Outputs:
%    outputArg1 [TYPE] - DESCRIPTION
% 
% Example:
%    EXAMPLE
%
% Other m-files: OTHER
%
% See also: OTHERFUNCTION
'''
    # TODO use InputStream instead of FileStream for string parsing
    input_stream = InputStream(string)
    lexer = MATLABHeaderLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MATLABHeaderParser(stream)
    tree = parser.headerDecl()
    print(tree)