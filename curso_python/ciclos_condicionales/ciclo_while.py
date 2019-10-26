# Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.
numero_uno = int(input("Escriba un numero\n"))
print("Escriba un numero mayor que", numero_uno)
numero_dos = int(input())
while numero_dos <= numero_uno:
    print(numero_dos, "No es mayor que", numero_uno)
    numero_dos = int(input("Intentelo de nuevo\n"))

print("Los numeros que ha escrito son", numero_uno, numero_dos)