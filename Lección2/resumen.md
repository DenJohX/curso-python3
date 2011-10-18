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
>>> 'Esta es otra cadena, en este caso cintiene "comillas" dobles en su interior'
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

```
>>> cadena = "esto es una cadena"
>>> cadena1 = 'esto tambien es una cadena'
>>> type(cadena)
< class 'str' >
>>> type(cadena1)
< class 'str' >
```

## Subcadenas
Vale decir que en un aspecto las cadenas de Python son parecidas a las de C, vamos a ver porque.


```
>>> cadena[2]
'n'
```


Como se dieron cuenta, si usamos "[]" podemos obtener solamente 1 letra de la cadena, las cadenas se almacenan en arrays, asi que poniendo el indice de la letra que queremos entre corchetes podemos tener una subcadena, vale aclarar que los indices empiezan de 0.

Vamos a ver lo siguiente.



```
>>> cadena[2:3]
'n'
>>> cadena[2:5]
'nso'
>>> cadena[0:8]
'sonsos'
>>> cadena[0:7]
'sonsos'
>>> cadena[0:6]
'sonsos'
>>> cadena[0:5]
'sonso'
```



Podemos quitar mas de 1 letra al mismo tiempo, hacemos lo siguiente, el primer numero, va a ser el indice de la primera letra, y el segundo numero, el indice de la ultima letra +1, porque, si se fijan de "sonsos" hicimos [0:2], nos tendria que devolver la letra en posicion 0,1 y 2 no?, en Python esto no funciona de esa manera, siempre le resta una posicion al segundo indice, en el caso de [0:2] nos devolvio la letra en posicion 0 y 1.



```
>>> cadena[0:6:2]
'sno'
>>> cadena[0:6:1]
'sonsos'
>>> cadena[0:6:3]
'ss'
```


Tambien podemos hacer que vaya de 2 en 2, o 3 en 3, simplemente poniendo un tercer numero separado con doble punto del segundo.

Listas
Los que hayan trabajado con otros lenguajes como ser Pascal o C, conocen los que son los vectores, o arreglo unidimensionales, en si, las listas son eso, pero, con una pequeña diferencia, carece de una caracteristica para ser llamados vectores, no son de un solo tipo, mejor veamos con un ejemplo.
?
1
2
3
4
5
6
7
>>> lista = ["sonsos",3,3.5]
>>> type(lista)
<class 'list'>
>>> lista[1]
3
>>> lista[2]
3.5
Las listas se definen con "[]", y como se dieron cuenta, es como un vector, pero, sin la limitacion de siempre usar el mismo tipo, y tambien cada elemento de una lista puede contener otra lista.
?
1
2
3
4
5
6
>>> lista = ["a",2.5,40]
>>> lsita1 = ["sonsos",80,[lista]]
>>> lsita1
['sonsos', 80, [['a', 2.5, 40]]]
>>> lsita1[2]
[['a', 2.5, 40]]

Entrada/Salida
Mucha consola interactiva, mucho variables, listas, pero, como le pido datos al usuario? como le informo los resultados?, como de costumbre, Python tiene funciones para eso, print e input, respectivamente.
[CONTINUARA ... ]

