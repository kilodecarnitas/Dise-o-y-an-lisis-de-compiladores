grammar Testtres;

/*
    Define la siguientes reglas de la gramática para expresión:

    * Variable 
    * Entero (id)
    * Asignación var :- int
    * If terciario 
       ID :- cuando << expr >> expr si_no expr

 */

prog:   (expr)+ ;

expr:
                                          #cuando
    |                                     #asignacion
    |                                     #litint
    |                                     #var
    ;


CUANDO  : 'cuando' ;
SI_NO   : 'si_no' ;
YA      : 'ya';

ID      : [a-zA-Z]+ ;
INT     : [0-9]+ ;
STRING  : '"' .*? '"' ;
WS : [ \t\n\r]+ -> skip ;