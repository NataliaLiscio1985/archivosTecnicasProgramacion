'''
Ejercicio 55 
Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir 
la lista generada.
'''

lista = []
for i in range(5):
    lista.append(int(input('Ingrese un numero : ')))
    
print(lista)
