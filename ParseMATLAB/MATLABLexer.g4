lexer grammar MATLABLexer;

channels {
  COMMENTS_CHANNEL
}

// Keywords
FUNCTION : 'function' ;

CLASSDEF : 'classdef' ;

PROPERTIES : 'properties' ;

METHODS : 'methods' ; 

END : 'end' ;

IF  : 'if' ;

ELSEIF : 'elseif' ;

ELSE : 'else' ;

WHILE : 'while' ;

SWITCH : 'switch' ;

CASE : 'case' ; 

OTHERWISE : 'otherwise' ;

// Symbols
EQUALS : '=' ;

EQUALTO : '==' ;

GT : '>' ;

LT : '<' ;

GE : '>=' ;

LE : '<=' ;

PLUS : '+' ;

MINUS : '-' ;

DOT : '.' ;

VECAND : '&' ;

VECOR : '|' ;

SCALAND : '&&' ;

SCALOR : '||' ;

LPAREN : '(' ;

RPAREN : ')' ;

LBRACE : '{' ;

// RBRACE : '}' ;

LBRACK : '[' ;

// RBRACK : ']' ;

MTIMES : '*' ;

TIMES : '.*' ;

RDIVIDE : '/' ;

LDIVIDE : '\\' ;

MRDIVIDE : './' ;

MLDIVIDE : '.\\' ;

POW : '.^' ;

MPOW : '^' ;

NOT : '~' ;

COLON : ':' ;

TRANS : '.\'' ;

CTRANS : '\'' ;

// General rules
NL  : '\r'?'\n' ;

fragment
LINECONTINUE
    : '...' ;

COMMENT
    : ('%' | LINECONTINUE) .*? NL -> channel(COMMENTS_CHANNEL) ;

fragment
LETTER  : [a-zA-Z] ; 
fragment
DIGIT   : [0-9] ; 
fragment
ESC : '\'\'' ;

INT : DIGIT+;

FLOAT : DIGIT+ '.' DIGIT*
      | '.' DIGIT+
      ;

SCI : (INT|FLOAT) 'e' INT ;

ID  : LETTER (LETTER|DIGIT|'_')* ;
STRING : '\'' (ESC|.)*? '\'' ;

RBRACK : ']' ;
RBRACE : '}' ;

// HCAT : (COMMA); // | SPACE ) ;

// VCAT : (SEMI | NL ) ;

// ARRAYELSEP : (HCAT| VCAT ) ; // SPACE+ ;

COMMA : ',' ;

SEMI  : ';' ;

WS  : SPACE+ -> skip ;

fragment
SPACE : [ \t] ;

