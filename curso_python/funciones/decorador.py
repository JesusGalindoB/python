# # a, b, c
# # a(b) -> c

def decorador(funcion):
    def division(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        """ esta es la documentacion de mi funcion """
        print("Bienvenido a la programacion con python")
        print("espero no llores")
        return resultado

    return division


@decorador
def saludo():
    print("Hola Mundo")

@decorador
def suma(val1, val2):
    return val1 + val2


saludo()

print("\n")

resultado = suma(10, 20)
print(resultado)

