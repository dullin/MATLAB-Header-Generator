parser grammar MATLABHeaderParser;

options { tokenVocab=MATLABHeaderLexer;}

headerDecl:
    m1Line
    description?
    syntax
    inputs?
    outputs?
    example?
    other?
    also?
    EOF
;

emptyLine:
    COMMENT
;

m1Line:
    COMMENT UNICODE_ID SEPARATOR restOfLine emptyLine?
;

description:
    textLine+ emptyLine
;

syntax:
    COMMENT SYNTAX restOfLine emptyLine
;

inputs:
    COMMENT INPUTS
    paraBlock+?
    emptyLine
;

outputs:
    COMMENT OUTPUTS
    paraBlock+?
    emptyLine
;

example:
    COMMENT EXAMPLE
    textLine+?
    emptyLine
;

other:
    COMMENT OTHERM nameList
    emptyLine
;

also:
    COMMENT ALSO nameList
;

paraBlock:
    firstParaLine
    textLine??
;

firstParaLine:
    COMMENT UNICODE_ID LBRACK UNICODE_ID RBRACK SEPARATOR restOfLine
;

nameList:
    UNICODE_ID (COMMA UNICODE_ID)*
;

textLine:
    COMMENT .*?
;

restOfLine:
    .*?
;  