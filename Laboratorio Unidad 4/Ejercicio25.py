'''
Ejercicio 25 
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda 
función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del 
programa llamar a ambas funciones.
'''

def cargarLista():
    lista = []
    for i in range (5):
        lista.append(int(input('Ingrese un numero entero: ')))
    return lista

def mostrarMayores(lista):
    for i in range (len(lista)):
        if lista[i] > 10:
            print(lista[i])
            
lista = cargarLista()
print('Los valores mayores a 10 son: ')
mostrarMayores(lista)
