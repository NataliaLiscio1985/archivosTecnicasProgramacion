'''
Ejercicio 40 
Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron 
múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 
5 a la vez. Resolverlo empleando for.
'''
m5=0
m3=0

for i in range(10):
    n = int(input('Ingrese un número entero: '))
    if n%3 == 0:
        m3=m3+1
    if n%5 == 0:
        m5=m5+1
        
print('Cantidad de múltiplos de 3: ', m3)
print('Cantidad de múltiplos de 5: ', m5)

