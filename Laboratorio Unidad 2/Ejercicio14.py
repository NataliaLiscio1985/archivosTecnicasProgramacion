"""
Ejercicio 14 Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.
"""
canthoras = int (input("Ingrese la cantidad de horas trabajadas: "))
valor = int (input("Ingrese el valor de la hora: "))
salario = canthoras * valor

print("El sueldo a cobrar es: $",salario,".")
