"""
Ejercicio 12 
Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una 
cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
"""

cadena = input("Ingrese una cadena de digitos: ")
for i in cadena:
    if i == "0":
        print("x", end="")
        continue
    print(i, end="")