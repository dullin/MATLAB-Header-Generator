lexer grammar MATLABHeaderLexer;

//Keywords
SYNTAX : 'Syntax:';

INPUTS : 'Inputs:';

OUTPUTS : 'Outputs:';

EXAMPLE : 'Example:';

OTHERM : 'Other m-files:';

ALSO : 'See also:';

COMMENT : '%';

LBRACK : '[';

RBRACK : ']';

SEPARATOR : '-';

COMMA : ',';

SYNTAX_ID: [=()];

NL  : '\r'?'\n' -> skip;

WS  : SPACE+ -> skip ;

fragment
SPACE : [ \t] ;

UNICODE_ID : [\p{Alnum}\p{General_Category=Other_Letter}_]*;

ANY : .;