diccionario = {"a":1, "b":2, "d":3}
valor = diccionario.get("a", "La llave no existe") # el metodo .get() sirve para saver si una llave existe o no en un diccionario ("a"), si no existe nos muestra el string ("La llave no existe")
valor_dos = diccionario.setdefault("e", 4) # el metodo .setdefault() sirve para saver si una llave existe o no en un diccionario ("e"), si no existe crea esa llave dentro del diccionario, junto con su valor (4)

print(diccionario)

