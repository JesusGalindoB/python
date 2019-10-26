tupla = (1, 2, 3, 4, 5, 6)
lista = [1, 2, 3, 4]
fusion = zip(tupla, lista)
fusion = tuple(fusion)
lista_dos = list(fusion)
print(fusion, lista_dos)


