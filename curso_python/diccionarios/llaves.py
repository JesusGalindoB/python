diccionario = {"uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5}
valor = diccionario.keys() # el metodo .keys() nos permite obtener todas las llaves de un diccionario 
valor_dos = diccionario.values() # el metodo .values() nos permite obtener todos los valores de nuestras llaves 
todo = diccionario.items() # el metodo .items() nos permite obtener todas las llaves con sus respectivos valores 
convert_lista = list(todo) # la funcion list convierte el diccionario en una lista
convert_tupla = tuple(todo) # la funcion tuple convierte el diccionario en una tupla

print(valor)
print(valor_dos)
print(todo)
print(convert_lista)
print(convert_tupla)