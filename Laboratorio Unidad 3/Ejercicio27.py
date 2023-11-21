'''
Ejercicio 27 
Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en 
pantalla la leyenda "Todos los números son menores a diez".
'''

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 < 10 and n2 < 10 and n3 < 10:
    print("Todos los números son menores a diez")
else:   
    print("No todos los números son menores a diez")