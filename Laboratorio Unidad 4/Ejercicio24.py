'''
Ejercicio 24 
Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un 
segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista 
multiplicado por el valor entero enviado. 
Ejemplo: 
lista=[3, 7, 8, 10, 2] 
multiplicar(lista,3)
'''
lista = [3, 7, 8, 10, 2]

def multiplicar(lista, entero):
    for i in range (len(lista)):
        lista[i] *= entero
    return lista

print(f'La lista multiplicada por el entero es: {multiplicar(lista,3)}')
