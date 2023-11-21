"""
Ejercicio 17 
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> 
y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la 
división entera respectivamente.  
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
c = num1 // num2
r = num1 % num2

print("El cociente de la division entre ",num1," y ",num2," es: ",c,"\nEl resto de la division entre ",num1," y ",num2," es: ",r,".")

