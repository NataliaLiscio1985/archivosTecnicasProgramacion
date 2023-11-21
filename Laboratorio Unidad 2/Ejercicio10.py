"""
Ejercicio 10 
Realizar la carga del precio de un producto y la cantidad a llevar. 
Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto).
"""

cantprod = int (input("Ingrese la cantidad de productos a adquirir: "))
precio = int (input("Ingrese el precio unitario del producto: "))
total = cantprod * precio

print("El total a pagar es: $",total,".")


