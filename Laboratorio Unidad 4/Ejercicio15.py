'''
Ejercicio 15 
Escribe un programa que convierta la tupla colors en un diccionario. 
'''

colors = (('green', '#008000'), ('blue', '#0000FF'), ('yellow', '#FFFF00'))
diccionario ={}
diccionario = dict(colors)
print(diccionario)
print(type(diccionario))
