# pala realizar una anotacion seguimos el iguiente formato (parametro : tipo_dato_entrada) -> tipo_dato_salida :
def saludo(nombre : str) -> None:
    print("Hola " + nombre)

# podemos colocar despues de colocar el tipo de entrada esperado, podemos colocar un valor por default
def suma(val1 : int, val2 : int = 100) -> int: 
    return val1 + val2

nombre = "Jesus"
saludo(nombre)

print(suma(10))