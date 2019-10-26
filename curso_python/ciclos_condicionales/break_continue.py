pais = 'Colombia Tierra Querida'

for caracter in pais:
    if caracter == 'T':
        break            # la palabra reservada break termina el flujo del ciclo (rompe el ciclo)
    print(caracter)

for caracter in pais:
    if caracter == 'Q':
        continue        # la palabra reservada continue, sigue a la siguiente iteracion sin continuar las acciones que esten despues de continue 
    print(caracter)