Bueno, siguiendo con el tema de las clases de programación, cada semana va a haber un resumen en este blog sobre lo que se explico en el IRC ...

#Que es python? Como se usa?

#Según wikipato, "Se trata de un lenguaje de programación multiparadigma ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje 
#interpretado, usa tipado dinámico, es fuertemente tipado y multiplataforma."

#Aja .. y eso que mierda quiere decir? , vamos por partes entonces:
#Multiparadigma: Como dice en la misma definición, porque soporta: Orientación a objetos, programación imperativa y programación funcional.
#Interpretado: Python lo haces funcionar con un interprete, no se compila como C por ejemplo, puede tener de ventaja no tener que re-compilar el programa para probar algún cambio, esto a cambio 
#de un rendimiento levemente menor.
#Fuertemente tipado: En algunos lenguajes, se permite que un tipo sea tratado como otro, en
#circunstancias especiales, por ejemplo: sumar un caracter y un entero: '1' +
#1 = 2 esto se conoce como débilmente tipado.
#En el caso de Python, esto no se permite, y se le conoce como
#fuertemente tipado, por lo que no se permite realizar operaciones entre tipos
#diferentes, a no ser que específicamente dentro del códigouno de los tipos
#sea convertido, para ajustarse al otro.
#Multiplataforma: Que se puede ejecutar en mas de 1 SO sin grandes cambios.

Bien, empezando con python, la consola interactiva ...

Python tiene 2 formas de usarse, mediante su consola interactiva y mediante archivos *.py, cosa que veremos mas adelante.
Bueno, la consola interactiva se inicia lanzando el interprete de python, mediante "python3.2", recuerden que usamos la versión 3 de Python.
Al lanzar el interprete, nos saldrá esto:

	
Python 3.2.2 (default, Sep 17 2011, 01:16:16)
[GCC 4.5.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>

hermoso no?, dirán, "que es esto?" , pues, es la consola interactiva, esta a la espera de ordenes, primero, vamos a experimentar, al ser un lenguaje de alto nivel, puedes usar esta consola como 
calculadora, por ejemplo

	
>>> 2+2
4
>>> 4-2
2
>>> 6*8
48
>>> 6/2
3.0
>>> 3**3
27

Practico no?, a veces suele ser mas simple que usar una calculadora gráfica ...

Variables, tipos y forma de asignación

Python, como todo lenguaje de programación, tiene variables, ahora vamos a ver como asignamos cada una,
	
>>> a = 2 #esta es una asignación de un entero, como veran, se hace simplemente así ...
>>> type(a) #type nos sirve para saber que tipo de variable se trata, en este caso "a"
<class 'int'>
>>> b = 2.5 #para asignar un numero de punto flotante, basta con poner el punto ...
>>> type(b)
<class 'float'>
>>> c = "hola mundo" #para asignar una cadena de texto o "string" como se conoce, se pone el texto entre comillas
>>> type(c)
<class 'str'>

Como se habran dado cuenta, las variables en python no hace falta declarar el tipo, que pasa cuando es una suma por ejemplo?, la misma cosa, si por ejemplo, sumas un entero + un float, la 
variable que contiene el resultado sera float.

Operadores de comparacion

Vale aclarar a estas alturas del partido, que se supone que tienen un conocimiento minimo de programacion, por esa razon obvio explicaciones mas detalladas ...
Operadores de comparacion, mayor que, menor que, igual que ... etc etc ... vamos, los conocidos por todos ... en Python, tambien existen ;)
vamos a ver como se portan ...
	
>>> 2 > 3
False
>>> 3 > 2
True
>>> 2 == 3 #notese que se usan 2 signos de "igual", ya que uno, es una asignación ...
False
>>> 2 != 3
True
>>> 2 >= 3
False
>>> 2 <= 3
True

Todo lindo, pero como salgo de aca??

Bueno, simplemente para salir de la consola
	
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit



Bueno, eso es todo por ahora amigos .. ya saben, si queren explicaciones mejores, les esperamos en el IRC, vale aclarar, que los martes estamos con explicaciones nuevas, toda la semana estamos 
para consultas particulares ...


PD: Pongo la definicion de dinamicamente tipado, para evitar dudas
Dinamicamente tipado

Esto significa que las secciones de memoria para las variables
no necesitan ser reservadas específicamente para un tipo, como sería el caso
en C, en el que se definen los tipos de variables durante la compilación, y
éstas no pueden cambiar durante la ejecución, por ejemplo, el resultado
de una funcion que devuelve una cadena no podría asignarse a una variable
previamente definida como un entero.

En python no se tiene esta restricción, ya que es dinamicamente tipado, no
necesita definir previamente el tipo de una variable, sino que se va dando
dinamicamente durante el tiempo de ejecución. En python una variable puede
cambiar de tipo en diferentes puntos de la ejecución.

Se dice entonces, que en python, los tipos tienen una definición estricta,
pero las variables no.
