'''
Ejercicio 41 
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la 
base y la altura de un triángulo. Resolverlo empleando for. 
El programa deberá informar: 
a) De cada triángulo la medida de su base, su altura y su superficie. 
b) La cantidad de triángulos cuya superficie es mayor a 12.
'''

n = int(input('Ingrese la cantidad de triángulos: '))
base=0
altura=0

for i in range(n):  
    base = float(input('Ingrese la base del triángulo: '))
    altura = float(input('Ingrese la altura del triángulo: '))
    superficie = (base*altura)/2
    print('Superficie del triángulo: ', superficie)
    if superficie > 12:
        print('La superficie es mayor a 12')
    else:
        print('La superficie es menor a 12')
    print('---------------------------')
    