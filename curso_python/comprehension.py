# lista = []

# for x in range(0, 101):
#     lista.append(x)

# print(lista)

estructura = [ x for x in range(0, 101) ] 
estructura_tupla = tuple( ( x for x in range(0, 101) ) )
condicionado = tuple( ( x for x in range(0, 101) if x % 2 == 0 ) )
diccionario = { indice:valor for indice, valor in  enumerate(estructura) }

print(estructura)
print(estructura_tupla)
print(condicionado)
print(diccionario)

