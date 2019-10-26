digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# La funcion range nos permite recorrer una cantidad de numero es pecificada en los parentesis (), en los parentesis podemos colocar lo siguiente (desde, hasta, saltos) 
for numero in range(1, 101, 2):
    print(numero)

for indice in range( len(digitos)):
    print('Indice:', indice, 'Valor:', digitos[indice]) # ejemplo con la funcion range() y ayudandonos  con la funcion len()

for indice, valor in enumerate(digitos):
    print('Indice:', indice, 'Valor:', valor) # la funcion enumerate() nos muestra el indice y el valor
    

