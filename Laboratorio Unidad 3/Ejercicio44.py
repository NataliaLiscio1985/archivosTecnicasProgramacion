'''
Ejercicio 44 
Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de 
multiplicar del mismo (los primeros 10 términos) Resolverlo empleando for. 
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 
'''
n= int(input('Ingrese un número del 1 al 10: '))

for i in range(1,11,1):
    print(n, ' x ', i, ' = ', n*i)
    