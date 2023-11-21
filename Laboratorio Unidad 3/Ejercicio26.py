'''
Ejercicio 26 
Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde 
a Navidad. 
'''

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
ano = int(input("Ingrese el año: "))

if dia == 25 and mes == 12:
    print("Es Navidad") 
else:
    print("No es Navidad")
    