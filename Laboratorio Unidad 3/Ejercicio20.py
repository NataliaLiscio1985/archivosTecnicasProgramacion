"""
Ejercicio 20 
Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e 
imprima alguno de estos mensajes: 
Si el promedio es >=7 mostrar "Promocionado". 
Si el promedio es >=4 y <7 mostrar "Regular". 
Si el promedio es <4 mostrar "Reprobado". 
"""

n1 = float(input("Ingrese la primera nota: "))
n2= float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercer nota: "))

promedio = (n1+n2+n3)/3

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4:
    print("Regular")
else:   
    print("Reprobado")
    