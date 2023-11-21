'''
Ejercicio 57 
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de 
sueldos
'''

lista = []
acumulador = 0
for i in range(5):
    lista.append(float(input('Ingrese un sueldo : ')))
    acumulador += lista[i]

promedio = acumulador / len(lista)
print(lista)
print('El promedio de los sueldos es : ',promedio)
