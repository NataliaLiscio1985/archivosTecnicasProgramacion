'''
Ejercicio 20 
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere 
calcular y mostrar su perímetro o su superficie. 
'''

def ingresoLado():
    lado = float(input("Ingrese un entero: "))
    return lado

def perimetro(lado):
    return lado*4

def superficie(lado):
    return lado**2

def eleccion():
    print("1. Perimetro")
    print("2. Superficie")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def calculo():
    lado = ingresoLado()
    opcion = eleccion()    
    if opcion == 1:
        print("El perimetro es:",perimetro(lado))
    elif opcion == 2:
        print("La superficie es:",superficie(lado))
    else:
        print("Opcion incorrecta")
        
calculo()
