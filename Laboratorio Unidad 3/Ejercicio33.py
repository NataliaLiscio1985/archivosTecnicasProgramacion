'''
Ejercicio 33 
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas 
mayores o iguales a 7 y cuántos menores. 
'''
promocionados = 0


for i in range(10):
    nota = int(input("Ingrese la nota del alumno: "))
    if nota >= 7:
        promocionados = promocionados + 1

print("La cantidad de alumnos promocionados es: ", promocionados)
print("La cantidad de alumnos que no promocionaron es: ", 10 - promocionados)
    

