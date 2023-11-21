"""
Ejercicio 23 
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y 
muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de 
cifras es mayor. 
"""
n1 = int(input("Ingrese un numero menor a 1000: "))

if n1 < 10:
    print("El numero tiene una cifra")
elif n1 < 100:
    print("El numero tiene dos cifras")
elif n1 < 1000:
    print("El numero tiene tres cifras")
else:
    print("ERROR \nEl numero tiene mas de tres cifras")
    