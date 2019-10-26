lista = ["dart", "php", "javascript", "java", "c", "html", "css", "r"]
# indices   0      1         2           3     4      5      6     7  
#          -8     -7        -6          -5    -4     -3     -2    -1    indices negativo        
indice = lista[5]
indice_negativo = lista[-2]
sub_lista = lista[1:6]
desde = lista[:4]
hasta = lista[4:]
todos = lista[:]
salto = lista[0:7:2]
reversa = lista[::-1]
print(indice)
print(indice_negativo)
print(sub_lista)
print(desde)
print(hasta)
print(todos)
print(salto)
print(reversa)
