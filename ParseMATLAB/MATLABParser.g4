parser grammar MATLABParser;

options { tokenVocab=MATLABLexer;}

fileDecl  
    : (functionDecl | classDecl)? (functionDecl* | partialFunctionDecl*)
    | partialFunctionDecl+
    | statBlock+ // Script
    | EOF
    ;

endStat
    : (NL|COMMA|SEMI) NL*
    ;

endStatNL 
    : NL+
    ;

// Function declaration without the closing end
partialFunctionDecl
    : FUNCTION outArgs? ID inArgs? endStat statBlock* 
    ; 

// Normal function declaration including closing end
functionDecl
    : partialFunctionDecl END endStatNL NL*
    ;

// Functions inside method blocks can be comma or semi separated 
methodDecl
    : partialFunctionDecl END endStat
    ;

classDecl
    : CLASSDEF ID endStat 
      (propBlockDecl|methodBlockDecl)* 
      END (EOF|endStat) NL*
    ;

propBlockDecl
    : PROPERTIES endStat prop* END endStat
    ;

methodBlockDecl
    : METHODS endStat methodDecl* END endStat
    ;

outArgs
    : ID EQUALS
    | LBRACK ID (COMMA ID)* RBRACK EQUALS
    ;

inArgs
    : LPAREN ID (COMMA ID)* RPAREN
    | LPAREN RPAREN
    ;

prop
    : ID (EQUALS expr)? endStat
    ;

dotRef
    : ID (DOT ID)*
    ;

statBlock
    : (stat endStat)
    ;

ifStat
    : IF expr endStat statBlock* 
      (ELSEIF expr endStat statBlock*)* 
      (ELSE endStat? statBlock*)?
      END
    ;

whileStat
    : WHILE expr endStat statBlock* END
    ;

caseStat
    : SWITCH expr endStat 
      (CASE expr endStat statBlock*)*
      (OTHERWISE endStat statBlock*)?
      END
    ;

stat
    : dotRef EQUALS expr
    | ifStat
    | whileStat
    | caseStat
    | expr
    | NL
  //  | COMMENT
    ;

arrayExpr
    : LBRACK exprArrayList RBRACK
    | LBRACK RBRACK
    ;

cellExpr
    : LBRACE exprArrayList RBRACE
    | LBRACE RBRACE
    ;

expr
    : expr LPAREN exprList RPAREN
    | expr (TRANS|CTRANS)
    | expr (MPOW|POW) expr
    | (PLUS|MINUS|NOT) expr
    | expr (MTIMES|TIMES|MLDIVIDE|LDIVIDE|MRDIVIDE|RDIVIDE) expr
    | expr (PLUS|MINUS) expr
    | expr COLON expr
    | expr (NOT|EQUALTO|GT|LT|GE|LE) expr
    | expr VECAND expr
    | expr VECOR expr
    | expr SCALAND expr
    | expr SCALOR expr
    | dotRef
    | INT | FLOAT | SCI  
    | STRING
    | arrayExpr
    | cellExpr
    | LPAREN expr RPAREN
    ;

exprList
    : expr (',' expr)*
    ;

exprArrayList
    : expr (COMMA? exprArrayList)*    #hcat
    | expr ((SEMI|NL) exprArrayList)* #vcat
    ;
