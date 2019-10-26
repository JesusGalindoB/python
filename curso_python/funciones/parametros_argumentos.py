def saludo(nombre):
    return "Hola {}, bienvenido a colombia".format(nombre)

def suma(valor1, valor2, valor3):
    return valor1 + valor2 +valor3

def curso():
    return "Hola, bienvenido", "a la universidad", 2.0


nuevo_saludo = saludo("juan")
print(nuevo_saludo)

resultado = suma(10, 20, 30)
print(resultado)

uno, dos, tres = curso()
print(uno, dos, tres)