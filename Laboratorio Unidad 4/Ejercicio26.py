'''
Ejercicio 26 
Con funciones, desarrollar un programa que permita cargar 5 nombres de personas y sus edades 
respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las 
personas mayores de edad (mayores o iguales a 18 años) 
Imprimir la edad promedio de las personas. 
'''

def cargarLista():
    nombres = []
    edades = []
    for i in range (5):
        nombres.append(input('Ingrese un nombre: '))
        edades.append(int(input('Ingrese la edad: ')))
    return nombres, edades

def mayoresEdad(nombres, edades):
    for i in range (len(edades)):
        if edades[i] >= 18:
            print(nombres[i])
            
def edadPromedio(edades):
    promedio = sum(edades) / len(edades)
    return promedio

nombres, edades = cargarLista()
print('Los mayores de edad son: ')
mayoresEdad(nombres, edades)
print(f'La edad promedio es: {edadPromedio(edades)}')

