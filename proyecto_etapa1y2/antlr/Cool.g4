grammar Cool;

program
    : ( klass SEMICOLON ) *
    ;

klass
    : KLASS TYPE ( 'inherits' TYPE )? '{' ( feature SEMICOLON )* '}'
    ;

feature
    : ID LPAR (formal (',' formal )*)? RPAR COLON TYPE '{' expr '}'
    | ID COLON TYPE ( ASSIGN expr )?
    ;

formal
    : ID COLON TYPE  #parameter
    ;

expr
    : ID ASSIGN expr #assign
    | expr (AT TYPE)? '.' ID LPAR(expr (',' expr)*)? RPAR    #objectCall
    | ID LPAR(expr (',' expr)*)? RPAR #simplecall
    | IF expr THEN expr ELSE expr FI   #if
    | WHILE expr LOOP expr POOL        #while
    | '{' (expr SEMICOLON)*'}'         #block
    | LET ID COLON TYPE ( ASSIGN expr )? (',' ID COLON TYPE ( ASSIGN expr )?)* IN expr #let
    | CASE expr OF (ID COLON TYPE CASEASSIGN expr SEMICOLON)* ESAC    #case
    | NEW TYPE                         #newobject
    | ISVOID expr                      #isvoid
    | expr op=ADD expr                 #suma
    | expr op=SUB expr                 #resta
    | expr op=MULT expr                #multiplicacion
    | expr op=DIV expr                 #division
    | INTCOMP expr                     #invert
    | expr LT expr                     #lt
    | expr LTEQ expr                   #le
    | expr EQUAL expr                  #equal
    | NOT expr                         #not
    | ID ASSIGN expr                   #assign
    | LPAR expr RPAR                   #parens
    | ID                               #Id
    | INTEGER                          #int
    | STRING                           #string
    | TRUE                             #true
    | FALSE                            #false
    ;

case_stat:
    ;

let_decl:
    ;

fragment A : [aA] ;
fragment B: [bB] ;
fragment C : [cC] ;
fragment D : [dD] ;
fragment E : [eE] ;
fragment F : [fF] ;
fragment H : [hH] ;
fragment I : [iI] ;
fragment L : [lL] ;
fragment M : [mM] ;
fragment N : [nN] ;
fragment O : [oO] ;
fragment P : [pP] ;
fragment R : [rR] ;
fragment S : [sS] ;
fragment T : [tT] ;
fragment V : [vV] ;
fragment W : [wW] ;
fragment Y : [yY] ;

KLASS : C L A S S ;
FI: F I;
IF: I F;
IN: I N;
INHERITS: I N H E R I T S;
ISVOID: I S V O I D;
LET: L E T;
LOOP: L O O P;
POOL: P O O L;
THEN: T H E N;
ELSE: E L S E;
WHILE: W H I L E;
CASE: C A S E;
ESAC: E S A C;
NEW: N E W;
OF: O F;
NOT: N O T;
TYPE: [A-Z][a-zA-Z_0-9]*;
ID: [a-z_][a-zA-Z0-9_]*;
TRUE: 'true';
FALSE: 'false';
COLON: ':';
SEMICOLON: ';';
ASSIGN: '<-';
CASEASSIGN: '=>';
MULT: '*';
DIV: '/';
ADD: '+';
SUB: '-';
EQUAL:'=';
INTCOMP: '~';
LPAR : '(';
RPAR : ')';
LT:'<';
LTEQ: '<=';
AT:'@';
INTEGER: [0-9]+ ;
STRING:'"' (('\\'|'\t'|'\r\n'|'\r'|'\n'|'\\"') | ~('\\'|'\t'|'\r'|'\n'|'"'))* '"';
COMMENT: '(*' .*? '*)' -> skip;
LINE_COMMENT: '--' ~[\r\n]* -> skip;
WHITESPACE : [ \t\n\r\u000c\u000b]+ -> skip;