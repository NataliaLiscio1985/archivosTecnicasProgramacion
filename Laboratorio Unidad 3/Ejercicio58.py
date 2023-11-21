'''
Ejercicio 58 
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 
por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados 
agrupados en dos listas. 
Imprimir las dos listas de sueldos.
'''

lista_maniana = []
lista_tarde = []

for i in range(4):
    sueldo = float(input('Ingrese el sueldo del empleado del turno mañana : '))
    lista_maniana.append(sueldo)

for i in range(4):
    sueldo = float(input('Ingrese el sueldo del empleado del turno tarde : '))
    lista_tarde.append(sueldo)
    
print('Lista de sueldos de la mañana : ',lista_maniana)
print('Lista de sueldos de la tarde : ',lista_tarde)
    
    