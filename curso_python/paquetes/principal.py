# import calculadora, de esta manera importamos un modulo (modulo: un archivo python)
# si tenemos (import *) significa que importaremos todas las funciones de nuestro modulo 
# (import suma) especifica que queremos trabajar con suma, (import suma, resta, division) podemos importar varios objetos que necesitemos
# from calculadora import suma, resta, division  

# import calculadora# la palabra reservada (as) nos permite renombrar un objeto 

# resultado = calculadora.suma(10, 20) # estamos llamando una funcion del modulo calculadora
# print(calculadora.__name__)
# print(__name__)

from animales.aves import Pinguino

pinguino = Pinguino()
pinguino.nadar()