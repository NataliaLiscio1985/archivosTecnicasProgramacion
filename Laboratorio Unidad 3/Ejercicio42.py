'''
Ejercicio 42 
Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 
valores ingresados. Resolverlo empleando for.
'''
suma = 0

for i in range(10):
    n = int(input('Ingrese un número: '))
    if i > 5:
        suma += n

print('La suma de los últimos 5 números es: ', suma)
