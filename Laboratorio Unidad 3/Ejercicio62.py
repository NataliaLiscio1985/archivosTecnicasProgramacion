'''
Ejercicio 62 
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista 
(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
'''

lista = []
contador = 0
for i in range(5):
    lista.append(int(input("Ingrese un numero: ")))

mayor = lista[0]
for i in range(1, len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]

for i in lista:
    if i == mayor:
        contador += 1

if contador >= 2:
    print("El mayor valor de la lista es: ", mayor, " y se repite ", contador, " veces")
else:
    print("El mayor valor de la lista es: ", mayor, " y no se repite")
    
    
