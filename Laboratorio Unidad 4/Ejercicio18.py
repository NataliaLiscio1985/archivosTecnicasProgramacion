'''
Ejercicio 18 
 Información Privada 
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el 
cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los 
mismos. LLamar desde el bloque del programa principal a ambas funciones.
'''

def ingresoEntero():
    entero = int(input("Ingrese un entero: "))
    return entero

def potencia(entero):
    return entero**2    

def retornoPotencia():
    entero = ingresoEntero()
    print(f'La potencia de {entero} es:',potencia(entero))
    
def multiplicacion():
    num1 = ingresoEntero()
    num2 = ingresoEntero()
    print(f'El producto de {num1} y {num2} es {num1*num2}')

retornoPotencia()
multiplicacion()
