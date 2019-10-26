diccionario = {'a': 1, 'b':2, 'c':3}
lista = ['a', 'b', 'c', 'd', 'z']
tupla = (1, 2, 3, 4, 5, 6)
string = 'colombia'
multiple = [(9, 8, 10), ['strings', 'strings', 'string'], (True, False, True), {'z':'Hola', 'y':'vemos', 'x':'no se'}]

for llave in diccionario:
    print(llave)

for letra in lista:
    print(letra)

for numero in tupla:
    print(numero)

for letra in string:
    print(letra)

for elemento1, elemento2, elemento3 in multiple:
    print(elemento1, elemento2, elemento3)