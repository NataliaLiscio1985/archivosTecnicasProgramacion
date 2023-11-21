'''
Ejercicio 21 
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
Llamarla desde el bloque principal del programa
'''

def ingresoString():
    string = input("Ingrese un string: ")
    return string

def cantidadVocales(string):
    vocales = ['a','e','i','o','u']
    contador = 0
    for i in string:
        if i in vocales:
            contador += 1
    return contador

palabra = ingresoString()
print(f'La cantidad de vocales en {palabra} es:',cantidadVocales(palabra))
