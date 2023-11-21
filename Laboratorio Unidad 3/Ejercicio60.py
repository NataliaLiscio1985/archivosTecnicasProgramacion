'''
Ejercicio 60 
Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor 
valor de la lista y la posición donde se encuentra.
'''

lista = []
for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))

lista.sort()
print("El menor valor de la lista es: ", lista[0], " y se encuentra en la posicion: ", lista.index(lista[0])+1)



# Otra forma de hacerlo

for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))

menor = lista[0]
for i in range(1, len(lista)):
    if lista[i] < menor:
        menor = lista[i]

print("El menor valor de la lista es: ", lista[0], " y se encuentra en la posicion: ", lista.index(lista[0])+1)