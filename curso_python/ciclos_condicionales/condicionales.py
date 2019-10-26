comida = input("Te gusta mas la pizza o la hamburguesa?\n")
if comida == "pizza":
    pizza = input("te gusta mas hawaiiana o de champiniones?\n") 
    if pizza == "hawaiiana":
        print("Excelentes gustos")
    elif pizza == "champiniones":
        print("Te recomiendo que escojas mejor")
    else:
        print("Error")
elif comida == "hamburguesa":
    hamburguesa = input("Te gusta con cebolla (si/no)?\n")
    if hamburguesa == "si":
        print("Que raro eres")
    elif hamburguesa == "no":
        print("Excelente eleccion") 
    else:
        print("Error")
else: 
    print("Error")

