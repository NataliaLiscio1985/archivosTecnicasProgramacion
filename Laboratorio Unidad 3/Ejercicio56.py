'''
Ejercicio 56 
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros 
al ingresar el cero. Mostrar finalmente la lista y su tamaño. 
'''

lista = []
i = True

while i:
    numero = int(input('Ingrese un numero, 0 para finalizar: '))
    if numero == 0:
        i = False
    else:
        lista.append(numero)

print(lista)
print('El tamaño de la lista es : ',len(lista))
