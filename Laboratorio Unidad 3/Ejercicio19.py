"""
Ejercicio 19 
Se ingresa por teclado un número entero positivo de uno o dos dígitos (1..99) mostrar un mensaje 
indicando si el número tiene uno o dos dígitos. 
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""

n1 = int(input("Ingrese un numero entero positivo de uno o dos digitos: "))
if n1 >= 10:
    print("El numero tiene dos digitos")
else:
    print("El numero tiene un digito")
    

