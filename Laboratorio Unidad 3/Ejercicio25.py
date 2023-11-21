'''
Ejercicio 25 
Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer 
trimestre del año (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.
'''

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
ano = int(input("Ingrese el año: "))

if mes >= 1 and mes <= 3:
    print("Corresponde al primer trimestre")
else:   
    print("No corresponde al primer trimestre")
    