animal = "leon" # variable global

def animales():
    global animal # funcion gobal me permite declarar una variable global dentro de una funcion 
    animal = "ballena" # variable local
    print(animal)

animales()
print(animal)