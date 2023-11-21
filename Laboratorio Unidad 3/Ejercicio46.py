'''
Ejercicio 46 
Dada una lista de cinco números: 1, 2, 3, 4, y 5. 
 
a) escribir una línea de código que solicite al usuario que reemplace el número central en la lista con 
un número entero ingresado por el usuario (Paso 1) 
b) escribir una línea de código que elimine el último elemento de la lista (Paso 2) 
c) escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
'''

lista = [1, 2, 3, 4, 5]

lista[2] = int(input('Ingrese un número: '))
lista.pop()
print(len(lista))
print(lista)
