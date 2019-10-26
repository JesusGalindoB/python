class Usuario:

    # la siguiente es la forma correcta de crear atributos para un objeto 
    def __init__(self, username="", email="", name=""):
        self.username = username
        self.email = email
        self.name = name

    def saluda(self): # cuando se cree un Metodo siempre es obligatorio colocar el parametro self
        return "Hola, soy un usuario " + self.name

"""   def crear_nombre(self, nombre): # de esta manera se crea un atributo para un objeto dentro de la clase 
        self.nombre = nombre """

codi = Usuario("codi", "codi@codigofailcilito.com", "codigo") # se crea una instancia (crear una instancia es crear un objeto)
""" codi.username = "codi" # de esta manera se pueden crear atributos pa un objeto fuera de la clase
codi.email = "codi@gmail.com" """

facilito = Usuario()
""" facilito.username = "facilito"  # de esta manera se pueden crear atributos pa un objeto fuera de la clase
facilito.email = "facilito@gmail.com" """

resultado = codi.saluda()
print(resultado)