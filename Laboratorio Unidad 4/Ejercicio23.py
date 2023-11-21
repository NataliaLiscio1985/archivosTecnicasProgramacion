'''
Ejercicio 23 
Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres 
funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista 
y retorna el mayor valor y la última recibe la lista y retorna el menor.
'''

lista = [1,2,3,4,5,6,7,8,9,10]

def suma(lista):
    for i in range (len(lista)):
        suma = sum(lista)
    return suma

def mayor(lista):
    mayor = max(lista)
    return mayor

def menor(lista):
    menor = min(lista)
    return menor

print(f'La suma de todos los elementos de la lista es: {suma(lista)}')
print(f'El mayor valor de la lista es: {mayor(lista)}')
print(f'El menor valor de la lista es: {menor(lista)}')
