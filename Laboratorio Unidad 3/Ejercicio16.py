"""
Ejercicio 16 
Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de 
ellos. 
"""

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

if n1 == n2 :
    print("Los numeros son iguales")
elif n1 > n2 :
    print(n1, "es mayor que", n2)
else:
    print(n2, "es mayor que", n1)
    
    