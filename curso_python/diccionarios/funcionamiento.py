diccionario = {}
diccionario["nombre"] = "pepe" # de esta forma podemos agregar nuevas llaves a un diccionario con su respectivo valor 
valor = diccionario["nombre"] # de estas manera podemos saber el valor de una llave 
diccionario["nombre"] = "juan" # aparte de que podemos crear nuevas llaves de la forma (nombre["llave"] = "valor") tambien podemos cambiar el valor a las llaves
diccionario_dos = {"a":2, "b":3, "c":4, "a":5} # como se observa la llave "a" tiene dos valore (2, 5). el valor que obtendra "a" sera el valor mas reciente que este en el diccionario, en este caso es (5)

print(diccionario)
print(valor)
print(diccionario_dos)
