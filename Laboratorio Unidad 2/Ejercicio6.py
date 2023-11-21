"""
Ejercicio 6 
Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. 
Tu tarea es completar el código para evaluar la siguiente expresión: 3x3 - 2x2 + 3x - 1  
El resultado debe ser asignado a y. Ayuda: cambia el tipo de dato para asegurarnos de que x es del tipo float. 
"""

x = float(input("Ingrese un numero: "))
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1

print("x = ",x,"\ny = ",y)
