grammar Testuno;

/*
    Define los siguientes tokens:

    Números flotantes, como una serie de uno o más dígitos separados por punto.
    Nombre de función, debe ser una secuencia de dígitos ascii que comience con 'fun_'
    Nombre de variable, debe ser una secuencia de dígitos ascii que comience con 'var_'

    Se deben ignorar los espacios y cambios de línea.
 */

prog:   (token)+ ;

token:
    DUMMY
    ;


DUMMY :  'a';