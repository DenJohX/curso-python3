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

*Explicación matemática:* Haciendo un equivalente a teoria de conjuntos, 
seria como definir el intervalo de elementos, (comenzando el conteo de 0) 
con un extremo cerrado y el otro
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



## Operaciones con Cadenas


Python tambien permite hacer operaciones con cadenas, entre ellas sumas y
multiplicaciones


### Suma

```python
>>> 'cadena' + 'cadena'
'cadenacadena'
>>> 'cadena1' + 'cadena2'
'cadena1cadena2'
```

La suma solo puede realizarse entre dos variables de tipo cadena


### Multiplicación


```python
>>> 'cadena1' * 3
'cadena1cadena1cadena1'
>>> 'cadena2' * 8
'cadena2cadena2cadena2cadena2cadena2cadena2cadena2cadena2'
```

La multiplicación siempre debe realizarse con una cadena y un número entero
positivo.




# Listas


Las listas son un tipo especialmente útil en python, puden ser usadas como
equivalente al array de otros lenguajes, pero con la ventaja de que cada
elemento de la lista puede ser de cualquier tipo, incluyendo otra lista.



## Declaración


Una lista se declara escribiendo los elementos dentro de corchetes __[ ]__
separando cada uno por una coma __,__


Ejemplo:

```python
>>> [0, 1, 2, 3, 4, 5, 6]
```

Cada uno de los elementos en el ejemplo anterior es un número, pero tambien
podemos incluír otros tipos, como por ejemplo cadenas, u otras listas


```python
>>> [0, 1, 'cadena', 'otra cadena', 3, 4]
>>> ['a continuacion una lista', ['elementos','dentro','de otra','lista']]
>>> [6, 2, [2.4, 3.2, ['a','b','c'], 1.5]]
```


## Trabajo con listas


Al igual que con las cadenas, las listas tienen elementos numerados desde el 0,
y podemos accesar a los mismos de la misma forma que una cadena.


```python
>>> lista = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
>>> lista[0]
'cero'
>>> lista[3]
'tres'
>>> lista[6]
'seis'
```


En el caso de las listas, a diferencia de  una cadena, podemos tambien modificar
los elementos a nustro gusto, por ejemplo:


```python
>>> lista = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
>>> lista[6] = 6
>>> lista[1] = 1
>>> lista
['cero', 1, 'dos', 'tres', 'cuatro', 'cinco', 6]
```

Como se observa en el ejemplo, hemos asignado números a los índices 1 y 6
respectivamente, y al final mostramos el contenido de la variable, observando
los cambios.


Tambien es simple cortar trozos de la lista, como se observa a continuación:


```python
>>> lista[2:4]
['dos', 'tres']
>>> lista[0:4]
['cero', 1, 'dos', 'tres']
>>> lista[4:1]
[]
>>> lista[0:6:1]
['cero', 1, 'dos', 'tres', 'cuatro', 'cinco']
>>> lista[0:6:2]
['cero', 'dos', 'cuatro']
>>> lista[0:6:3]
['cero', 'tres']
```


### Trabajo con listas anidadas


Ya que pyton permite definir una lista dentro de otra, esto conocido como listas
anidadas, o listas de varias dimensiones. También nos permite trabajar
directamente sobre las listas internas, como vemos a continuación.

```python
>>> lista1 = [0, 1, 2]
>>> lista2 = [3, 4, 5]
>>> lista3 = [6, 7, 8]
>>> lista = [lista1, lista2, lista3]
>>> lista
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]

```


Como se puede ver, hemos definido una lista, que contiene 3 listas mas, ahora
veamos como acceder a los elementos de la primera lista (primer elemento, índice
0)


```python
>>> lista[0]
[0, 1, 2]
>>> lista[0][0]
0
>>> lista[0][1]
1
>>> lista[0][2]
2
```


Y de la misma forma, podemos acceder a las otras listas (elementos 1 y 2)

```python
>>> lista[1]
[3, 4, 5]
>>> lista[2]
[6, 7, 8]
>>> lista[2][1]
7
>>> lista[2][2]
8
```


Python también nos permite hacer selecciones mas complejas:

``` python
>>> lista[2][1:3]
[7, 8]
>>> lista[1][0:3]
[3, 4, 5]
>>> lista[1][0:2]
[3, 4]
```


## Operaciones con listas


Las listas tambien pueden operarse, al igual que las cadenas, con sumas y
multiplicaciones


```python
>>> lista = [0, 1, 2]
>>> lista2 = [3, 4, 5]
>>> lista * 5
[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
>>> lista + lista2
[0, 1, 2, 3, 4, 5]
```

Al igual que con las cadenas, las sumas se realizan entre dos listas y las
multiplicaciones entre una lista y un numero entero positivo.
