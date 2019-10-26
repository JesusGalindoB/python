def tabla_multiplicar(numero):
    for posicion in range(1, 11):
        yield numero * posicion # la palabra reservada yield crea una coleccion de datos. yield retorna un valor sin terminar la funcion

for resultado in tabla_multiplicar(5):
    print(resultado)