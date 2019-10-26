def comienso(lista):

    def continuacion():
        nonlocal lista 
        lista = [1, 2, 3, 4]
        for val in lista:
            print(val)

    continuacion() # solo se puede llamar una funcion que esta anidada, dentro de la funcion globlal (nunca por fuera)
    print(lista)
    
lista = ['uno', 'dos', 'tres', 'cuatro']
comienso(lista)

