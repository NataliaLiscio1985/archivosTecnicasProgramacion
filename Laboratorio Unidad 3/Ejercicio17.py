"""
Ejercicio 17 
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al 
segundo informar su suma y diferencia, en caso contrario informar el producto y la división del 
primero respecto al segundo
    
"""
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

if n1 > n2 :
    print("La suma de los numeros es: ", n1 + n2)
    print("La diferencia de los numeros es: ", n1 - n2)
elif n1 != 0:   
    print("El producto de los numeros es: ", n1 * n2)
    print("La division de los numeros es: ", n1 / n2)
else: 
    print("El producto de los numeros es: ", n1 * n2)
    print("El primer numero ingresado es cero, no se puede realizar la opracion de division")