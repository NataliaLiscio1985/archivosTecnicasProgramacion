"""
Ejercicio 11 
Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los 
caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e 
imprimir la parte antes de @ en una línea
"""

direccion = input("Ingrese una direccion de correo valida: ")
for i in direccion:
    if i == "@":
        break
    print(i, end="")
    
