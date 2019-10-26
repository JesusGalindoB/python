lenguajes_pmcion = "php: java: python: dart: javascript: c#"
lista = lenguajes_pmcion.split(":")
string_nuevo = " ".join(lista)
espacios = """un texto
pero que 
esta 
con saltos de
linea"""
lista_espacio = espacios.splitlines()
print(lista, string_nuevo, lista_espacio)
