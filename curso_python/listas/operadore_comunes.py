lista = [20, 890, 17.5, 1.36, 76, 1]
lista.sort()  # el metodo sort ordena los elementos de una lista de forma ascendete
lista.sort(reverse=True) # el metodo sort con el valor(reverse=True) ordena los elmentos de una lista de forma descendente
menor = min(lista) # la funcion min es traer el valor mas pequeno de la lista 
mayor = max(lista) # la funcion min es traer el valor mas grande de la lista 
longuitud = len(lista) # da como resultado el numero de elementos que hay en una lista
resultado = 20 in lista # me ayuda a saber si un elemento esta o no dentro de la lista
indice = lista.index(20) # el metodo index me da como resultado el indice del elemento que yo quiera
contar = lista.count(20) # el metodo count nos permite saber cuantas veces esta un elemento dentro de nuestra lista
insertar = lista.insert(5, 123) # el metodo insert nos permite anadir un elemento en un indice especifico
print(lista, menor, mayor, longuitud, resultado, indice, contar)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
 
lista2.append(9) # permite anadir elementos a una  lista
lista2.remove(4) # permite quitar elemntos de una lista
print(lista2)