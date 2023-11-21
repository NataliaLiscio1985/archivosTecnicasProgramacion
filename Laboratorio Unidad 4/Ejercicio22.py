'''
Ejercicio 22 
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor 
de un lado
'''
def ingresoLado():
    lado = float(input("Ingrese un entero: "))
    return lado

def calculoPerimetro(lado):
    return lado*4

lado=ingresoLado()
print(f'El perimetro del cuadrado cuyo lado es {lado} es: ',calculoPerimetro(lado))

