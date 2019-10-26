def nombre(apellido):
    print("Hola Mundo")
    print(apellido)

variable_funcion = nombre # de esta manera se asigna una funcion a una variable 
variable_funcion("perez")

"""
la plabra reservada lambda me permite crear un funcion dentro de una variable
(la condicion para hacer esto es que la funcion debe de ser pequena preferiblemente de una sola linea)"""
mi_funcion = lambda grados : grados * 1.8 + 32 

resultado = mi_funcion(32)
print(resultado)

lista = [1, 2, 3, 4, 5]
resultado = map(lambda numero: numero * numero , lista) # la funcion map() nos permite aplicar una funcion a los items de un objeto iterable(lista, tupla, diccionario) 

lista_resultado = list(resultado)
print(lista_resultado)


