class Circulo:
    pi = 3.14159265
    
    # este es un Metodo de clase y normanlemnte se utilizan cuando necesitemos utilizar variables de clase 
    @classmethod
    def area(cls, radio):
        return cls.pi * radio**2

resultado = Circulo.area(10)
print(resultado)