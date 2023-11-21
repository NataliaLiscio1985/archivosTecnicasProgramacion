'''
Ejercicio 34 
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las 
personas.
'''

contador = 0
suma = 0

n = int(input("Ingrese la cantidad de personas: "))

for i in range(n):
    altura = float(input("Ingrese la altura de la persona: "))
    suma = suma + altura
    contador = contador + 1
    
promedio = suma / contador
print("El promedio de altura de las personas es: ", promedio)

