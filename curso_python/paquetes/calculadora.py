"""Documentación del módulo.
Esta es una anotación la cual debe de encontrarse
en la parte superior de nuestro script.
Esta anotación tiene cómo objetivo describir el módulo"""

""" posteriormente escribimos los siguientes  metadatos ( encontramos ocho metadatos, los cuales son los mas comune). 
todo metadato comiensa con doble guion bajo __"""
__author__ = "Jesus Esteban Barreto Galindo"
__copyright__ = "Copyright 2019"
__credits__ = ["Jesus Galindo"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "LGSUS"
__email__ = "LgSus@gmail.com"
__status__ = "Production"


def suma(val1, val2):
    return val1 + val2

def resta(val1, val2):
    return val1 - val2

def multiplicacion(val1, val2):
    return val1 * val2

def division(val1, val2):
    return val1 / val2

if __name__ == "__main__":
    print("Soy un mensaje de calculadora")
else:
    print("Estoy siendo usado como modulo")