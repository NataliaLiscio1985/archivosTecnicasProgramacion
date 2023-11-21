'''
Ejercicio 54 
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan 
un valor superior a 100
'''

lista = [101, 2, 3, 400, 5, 6, 7, 8]
contador = 0

for i in lista:
    if i > 100:
        contador += 1

print('La cantidad de valores que son superiores a 100 son : ',contador)