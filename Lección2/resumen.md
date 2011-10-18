#Cadenas


Las cadenas, son simplemente sucesiones de caracteres, en python3 se aceptan
caracteres unicode, es decir, que podemos escribir en cualquier lenguaje sin
problemas


Son útiles para todo tipo de situaciones, como mostrar al usuario un mensaje, o
utilizarlas para describir un fichero, etc.


## Modos de declaración


Para declarar una cadena, simplemente se encierra entre comillas dobles o
simples:


```python
>>> "Se puede definir entre comillas"
>>> 'O tambien con comillas simples (apóstrofe)'
```


### Usar comillas entre cadenas


Como se observa, las cadenas deben abrirse y cerrarse con un mismo tipo de
comilla, ya sea simple o doble, en el caso de necesitar alguno de esos tipos
dentro de la misma cadena, podemos hacerlo de dos formas:

#### Abriendo y cerrando la cadena con comillas del tipo contrario:

```python
>>> "Esta es una cadena, que contiene 'comillas' simples en su interior"
>>> 'Esta es otra cadena, en este caso contiene "comillas" dobles en su interior'
```

#### Utilizando un caracter de escape


Las cadenas, en python, se procesan al momento de declararse, de manera
atomatica. Esto da la ventaja de que podemos usar dentro de las cadenas
caracteres especiales, uno de ellos es el caracter de escape '\' que se utiliza
para indicarle a python que no debe hacer caso de la funcionalidad específica
del siguiente caracter, en este caso las comillas.


```python
>>> "Esta cadena contiene \"dobles comillas\" con un caracter de escape"
>>> 'Esta cadena contiene \'comillas simples\' con un caracter de escape'
```


## Trabajando con cadenas

Muchos se van a sorprender por la simplicidad con la que Python maneja las cadenas, bueno, dejemonos de parloterio, a darle.

```python
>>> cadena = "esto es una cadena"
>>> cadena1 = 'esto tambien es una cadena'
>>> type(cadena)
< class 'str' >
>>> type(cadena1)
< class 'str' >
```

## Subcadenas


Vale decir que en un aspecto las cadenas de Python estan compuestas por una
susceción ordenada de caracteres, cada uno numerado por un índice que comienza a
contar de 0, tomando como ejemplo una cadena con las vocales, esto sería como 
se describe a continuación:


```
+-----------+---+---+---+---+---+
| indice    | 0 | 1 | 2 | 3 | 4 |
+-----------+---+---+---+---+---+
| caracter  | a | e | i | o | u |
+-----------+---+---+---+---+---+
```


Así por ejemplo, podemos seleccionar subcadenas, de la manera siguiente:


```python
>>> cadena = 'abcdefghijklmñopqrstuvwxyz'
>>> cadena
'abcdefghijklmñopqrstuvwxyz'
>>> cadena[1]
'b'
>>> cadena[2]
'c'
>>> cadena[3]
'd'
```


Usando "[]" podemos obtener una porción de la la cadena, si solo colocamos un
número, como en el ejemplo de arriba, obtendremos sólo un caracter.


Veamos lo siguiente:


```python
>>> cadena[0:3]
'abc'
>>> cadena[0:10]
'abcdefghij'
>>> cadena[5:10]
'fghij'
>>> cadena[10:20]
'klmñopqrst'
```

### (Explicación matemática)
Haciendo un equivalente a teoria de conjuntos, seria como definir el ingervalo
de elementos, (comenzando el conteo de 0) con un extremo cerrado y el otro
abierto, es decir [a, b), esta selección devuelve los caracteres de índice
i, expresado como {i | a <= i < b}


Así, vemos que python, en el primer ejemplo devuelve las primeras tres letras,
que corresponden a los índices 0, 1, y 2



Ahora, otro ejemplo.


```python
>>> cadena[0:20:1]
'abcdefghijklmñopqrst'
>>> cadena[0:20:2]
'acegikmoqs'
>>> cadena[0:20:3]
'adgjmps'
>>> cadena[0:20:4]
'aeimq'
>>> cadena[0:20:5]
'afkp'
>>> cadena[0:20:6]
'agms'
```

En ese caso seleccionamos el rango, con los dos primeros números, y el tercero
define si se van a seleccionar los caracteres de uno en uno, de dos en dos, etc.
