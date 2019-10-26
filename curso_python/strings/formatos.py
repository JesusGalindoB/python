nombre = "  me llamo Pepe Guamo  "

inicio_mayus = nombre.capitalize() # el metodo capitalize convierte la primer letra del string en mayuscula
invertido = nombre.swapcase() # el metodo swapcase convierte todase las letras minusculas de nuestro string en mayusculas y viseversa
mayusculas = nombre.upper() # el metodo upper cambia todo el string a mayuscula
minusculas = nombre.lower() # el metodo lower cambia todo el string a minusculas
titulo = nombre.title() # el metodo title le da al string un formato de titulo (convierte las primeras letras de cada palabra en mayusculas)
remplazo = nombre.replace("Pepe","Antonio") # el metodo replace me permite remplazar un valor dentro del string
espacios = nombre.strip() # el metodo strip permite eliminar los epacios al l=inicio y al final del string

print(inicio_mayus)
print(invertido)
print(mayusculas)
print(minusculas)
print(titulo)
print(remplazo)
print(espacios)

# los metodos isupper y islower me permiten saber si un string esta en mayusculas o minusculas
print(minusculas.isupper())  
print(mayusculas.islower())

# podemos dejar {} en nuestros string para que tomen el valor de una variable 
ciudad = "bogota"
edad = "veinte"
resultado = "vivo en {} y tengo {}".format(ciudad, edad) 
print(resultado)
