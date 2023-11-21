'''
Ejercicio 13 
Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3). 
'''

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3= {}
d3.update(d1)
d3.update(d2)
print(d3)
