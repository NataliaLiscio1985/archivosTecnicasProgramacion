'''
Ejercicio 45 
Realizar un programa que lea los lados de n triángulos, Resolverlo empleando for, e informar: 
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados 
iguales), o escaleno (ningún lado igual) 
b) Cantidad de triángulos de cada tipo
'''

n = int(input('Ingrese la cantidad de triángulos: '))

for i in range(1, n+1, 1):
    print('Ingrese los lados del triángulo ', i)
    lado1 = int(input('Lado 1: '))
    lado2 = int(input('Lado 2: '))
    lado3 = int(input('Lado 3: '))
    
    if lado1 == lado2 and lado1 == lado3:
        print('El triángulo ', i, ' es equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('El triángulo ', i, ' es isósceles')
    else:
        print('El triángulo ', i, ' es escaleno')

