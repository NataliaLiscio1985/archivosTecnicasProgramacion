'''
Ejercicio 59 
Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la 
lista. 
'''

lista = []
for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))

lista.sort()
print("El mayor valor de la lista es: ", lista[-1])


# Otra forma de hacerlo

lista = []
for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))

mayor = lista[0]
for i in range(1, len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]

print("El mayor valor de la lista es: ", mayor)

