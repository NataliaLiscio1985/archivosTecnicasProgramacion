"""
Ejercicio 21 
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
"""
n1 = float(input("Ingrese el primer numero: "))
n2= float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

if n1 > n2 and n1 > n3:
    print("El mayor numero es: ", n1)
elif n2 > n1 and n2 > n3:
    print("El mayor numero es: ", n2)
else:   
    print("El mayor numero es: ", n3)
    
    