"""
Ejercicio 22 
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, 
negativo o nulo (es decir cero)
"""

n1 = int(input("Ingrese un numero: "))

if n1 == 0:
    print("El numero es nulo")
elif n1 > 0:
    print("El numero es positivo")
else:   
    print("El numero es negativo")
    