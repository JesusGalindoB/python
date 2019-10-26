def mostrar_mensaje(mensaje):
    mensaje = mensaje.title()

    def mostar():
        print(mensaje)

    return mostar
    
nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()