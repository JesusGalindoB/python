class Triangulo:

    numero = 2
    # a este tipo de metodos se les llama Metodos estaticos (por que no dependen de ninguna instancia)
    @staticmethod 
    def aerea(base, altura): # en un metodo de clase no se escribe el parametro self
        return (base * altura) / Triangulo.numero

resultado = Triangulo.aerea(10, 20)
print(resultado) 