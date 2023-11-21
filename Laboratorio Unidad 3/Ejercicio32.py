'''
Ejercicio 32 
Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor 
ingresado de uno en uno. Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 
30
'''

a = 1
b = int(input("Ingrese un valor positivo: "))

while a <= b:
    print(a)
    a = a + 1
    
    