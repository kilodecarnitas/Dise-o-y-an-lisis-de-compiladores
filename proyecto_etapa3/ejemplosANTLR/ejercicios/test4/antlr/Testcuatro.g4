grammar Testcuatro;

/*
    Define la siguientes reglas de la gramática para expresiones:

    * asignación id <= valor
    * creación de objeto:
        dame_un clase tomando {atributo:valor, atributo:valor, ...} ya!
    * el valor puede ser cualquier expr, los atributos y nombre de clase son ids

 */

prog:   (expr)+ ;

expr: DUMMY
    ;


DAMEUN  : 'dame_un' ;
TOMANDO : 'tomando' ;
YA      : 'ya!';
DUMMY   : 'dummy';

ID      : [a-zA-Z]+ ;
INT     : [0-9]+ ;
STRING  : '"' .*? '"' ;
WS : [ \t\n\r]+ -> skip ;