'''
Ejercicio 63 
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego 
de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de 
edad (mayores o iguales a 18 años) 
'''

nombres = []
edades = []

for i in range(5):
    edades.append(int(input("Ingrese la edad de la persona: ")))
    nombres.append(input("Ingrese el nombre de la persona: "))

print('Las personas mayores de edad son: ')
print('---------------------------------')
print('')

for i in range(len(edades)):
    if edades[i] >= 18:
        print(nombres[i],' tiene ', edades[i], ' años')
        

