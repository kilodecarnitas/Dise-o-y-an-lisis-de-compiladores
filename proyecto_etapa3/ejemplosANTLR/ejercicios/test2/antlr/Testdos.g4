grammar Testdos;

/*
    Define los siguientes tokens:

    Dirección IP, como una serie de cuatro números separados por un punto.
    Operadores, donde el operador debe comenzar con 'op' y seguido de una de las 4 operaciones aritméticas básicas.
    Email, podemos tener cualquier combinación de palabras separadas por punto, y dos de esas secuencias separadas por arroba.

    Se deben ignorar los espacios y cambios de línea.
 */

prog:   (token)+ ;

token:
    DUMMY
    ;


DUMMY :  'a';