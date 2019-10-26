def add_binary(a, b):
    suma = a + b 
    division = suma 
    binary = ""

    while division >= 1:
        module = division % 2
        division = int(division / 2) 
        binary = binary + str(module)
    result = binary[::-1]
    return result 

resultado = add_binary( 35452661122539821, 38437560936102726)
print(resultado)

