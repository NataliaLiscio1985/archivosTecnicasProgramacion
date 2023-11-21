'''
Ejercicio 66 
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.
'''

lista = []

for i in range(5):
    lista.append(int(input("Ingrese un sueldo: ")))

lista.sort()
print("La lista ordenada de menor a mayor es: ", lista)
