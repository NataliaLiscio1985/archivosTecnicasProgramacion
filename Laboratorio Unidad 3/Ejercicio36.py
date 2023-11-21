'''
Ejercicio 36 
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores 
fueron pares y cuántos impares. 
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto 
de la división de dos valores, por ejemplo 11%2 retorna un 1, if valor%2==0: )
'''

n = int(input("Ingrese la cantidad de numeros enteros: "))
contador1 = 0
contador2 = 0
if n > 0:
    for i in range(n):
        numero = int(input("Ingrese un numero entero: "))
        if numero % 2 == 0:
            contador1 = contador1 + 1
        else:
            contador2 = contador2 + 1
    print("La cantidad de numeros pares es: ", contador1)
    print("La cantidad de numeros impares es: ", contador2)
    
    